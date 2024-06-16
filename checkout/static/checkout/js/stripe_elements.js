document.addEventListener("DOMContentLoaded", function () {
  // Retrieve the Stripe public key and client secret from the HTML
  const stripePublicKey = document.getElementById(
    "id_stripe_public_key"
  ).textContent;
  const clientSecret = document.getElementById("id_client_secret").textContent;

  // Initialize Stripe with the public key
  const stripe = Stripe(stripePublicKey);

  // Create an instance of Stripe Elements
  const elements = stripe.elements();

  // Define custom styling for the Stripe card element
  const style = {
    base: {
      color: "#000",
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4",
      },
    },
    invalid: {
      color: "#dc3545",
      iconColor: "#dc3545",
    },
  };

  // Create a card element and mount it to the HTML element with id "card-element"
  const card = elements.create("card", { style: style });
  card.mount("#card-element");

  // Listen for changes on the card element and display any errors
  card.on("change", function (event) {
    const displayError = document.getElementById("card-errors");
    displayError.textContent = event.error ? event.error.message : "";
  });

  // Get the form element
  const form = document.getElementById("payment-form");

  // Add a submit event listener to the form
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Confirm the card payment using the client secret and card details
    stripe
      .confirmCardPayment(clientSecret, {
        payment_method: {
          card: card,
          billing_details: {
            name: form.full_name.value,
            address: {
              line1: form.street_address1.value,
              line2: form.street_address2.value,
              city: form.town_or_city.value,
              state: form.county.value,
              postal_code: form.postcode.value,
              country: form.country.value,
            },
          },
        },
      })
      .then(function (result) {
        if (result.error) {
          // Display any errors that occur during the payment process
          const errorElement = document.getElementById("card-errors");
          errorElement.textContent = result.error.message;
        } else if (result.paymentIntent.status === "succeeded") {
          // If the payment is successful, submit the form
          form.submit();
        }
      })
      .catch(function (error) {
        // Handle network or server errors
        const errorElement = document.getElementById("card-errors");
        errorElement.textContent = "An error occurred. Please try again.";
      });
  });
});
