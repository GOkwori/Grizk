document.addEventListener("DOMContentLoaded", function () {
  // Get Stripe publishable key and client secret
  const stripePublicKey = document
    .getElementById("id_stripe_public_key")
    .textContent.slice(1, -1);
  const clientSecret = document
    .getElementById("id_client_secret")
    .textContent.slice(1, -1);

  // Initialize Stripe
  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();

  // Style for the Stripe card element
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

  // Create the card element
  const card = elements.create("card", { style: style });
  card.mount("#card-element");

  // Handle real-time validation errors from the card element
  card.addEventListener("change", function (event) {
    const displayError = document.getElementById("card-errors");
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = "";
    }
  });

  // Handle form submission
  const form = document.getElementById("payment-form");
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    stripe
      .confirmCardPayment(clientSecret, {
        payment_method: {
          card: card,
          billing_details: {
            name: form.full_name.value,
            phone: form.phone_number.value,
            address: {
              country: form.country.value,
              postal_code: form.postcode.value,
              city: form.town_or_city.value,
              line1: form.street_address1.value,
              line2: form.street_address2.value,
              state: form.county.value,
            },
          },
        },
      })
      .then(function (result) {
        if (result.error) {
          const displayError = document.getElementById("card-errors");
          displayError.textContent = result.error.message;
        } else {
          if (result.paymentIntent.status === "succeeded") {
            form.submit();
          }
        }
      });
  });
});
