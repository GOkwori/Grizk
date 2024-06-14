// Wait until the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", function () {
  // Retrieve the Stripe public key and client secret from the HTML
  var stripePublicKey = document.getElementById(
    "id_stripe_public_key"
  ).textContent;
  var clientSecret = document.getElementById("id_client_secret").textContent;

  // Initialize Stripe with the public key
  var stripe = Stripe(stripePublicKey);

  // Create an instance of Stripe Elements
  var elements = stripe.elements();

  // Define custom styling for the Stripe card element
  var style = {
    base: {
      color: "#000", // Set base text color
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif', // Set font family
      fontSmoothing: "antialiased", // Smooth font edges
      fontSize: "16px", // Set base font size
      "::placeholder": {
        color: "#aab7c4", // Placeholder text color
      },
    },
    invalid: {
      color: "#dc3545", // Text color for invalid input
      iconColor: "#dc3545", // Icon color for invalid input
    },
  };

  // Create a card element and mount it to the HTML element with id "card-element"
  var card = elements.create("card", { style: style });
  card.mount("#card-element");

  // Listen for changes on the card element and display any errors
  card.on("change", function (event) {
    var displayError = document.getElementById("card-errors");
    if (event.error) {
      displayError.textContent = event.error.message; // Show error message
    } else {
      displayError.textContent = ""; // Clear error message
    }
  });

  // Get the form element
  var form = document.getElementById("payment-form");

  // Add a submit event listener to the form
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    // Confirm the card payment using the client secret and card details
    stripe
      .confirmCardPayment(clientSecret, {
        payment_method: {
          card: card, // Use the card element
          billing_details: {
            name: form.full_name.value, // Get the full name from the form
            address: {
              line1: form.street_address1.value, // Get the first address line from the form
              line2: form.street_address2.value, // Get the second address line from the form
              city: form.town_or_city.value, // Get the city from the form
              state: form.county.value, // Get the state from the form
              postal_code: form.postcode.value, // Get the postal code from the form
              country: form.country.value, // Get the country from the form
            },
          },
        },
      })
      .then(function (result) {
        if (result.error) {
          // Display any errors that occur during the payment process
          var errorElement = document.getElementById("card-errors");
          errorElement.textContent = result.error.message;
        } else {
          // If the payment is successful, submit the form
          if (result.paymentIntent.status === "succeeded") {
            form.submit();
          }
        }
      });
  });
});
