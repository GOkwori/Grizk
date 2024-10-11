document.addEventListener("DOMContentLoaded", function () {
  
  // Initialize Bootstrap toasts
  var toastElList = [].slice.call(document.querySelectorAll(".toast"));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
  });
  toastList.forEach((toast) => toast.show());

  // Initialize the wishlist removal functionality
  initializeWishlistRemoval();

  // Initialize cart progress bar
  updateProgressBar();
});

// Initialize event listeners for wishlist removal buttons
function initializeWishlistRemoval() {
  document.querySelectorAll(".remove-item").forEach(function (button) {
    button.addEventListener("click", function () {
      var productId = button.getAttribute("data-product_id");
      var csrfToken = getCookie("csrftoken");
      removeFromWishlist(productId, csrfToken);
    });
  });
}

// Update the delivery progress bar based on the cart totals
function updateProgressBar() {
  var totalElement = document.getElementById("cart-totals");
  var progressElement = document.getElementById("delivery-progress");
  if (totalElement && progressElement) {
    var total = parseFloat(totalElement.getAttribute("data-total"));
    var threshold = parseFloat(totalElement.getAttribute("data-threshold"));
    if (!isNaN(total) && !isNaN(threshold) && threshold > 0) {
      var progress = Math.min((total / threshold) * 100, 100);
      progressElement.style.width = progress + "%";
      progressElement.setAttribute("aria-valuenow", progress);
    }
  }

  // Offcanvas cart progress
  var offcanvasTotalElement = document.getElementById("offcanvas-cart-totals");
  var offcanvasProgressElement = document.getElementById("offcanvas-delivery-progress");
  if (offcanvasTotalElement && offcanvasProgressElement) {
    var offcanvasTotal = parseFloat(offcanvasTotalElement.getAttribute("data-total"));
    var offcanvasThreshold = parseFloat(offcanvasTotalElement.getAttribute("data-threshold"));
    if (!isNaN(offcanvasTotal) && !isNaN(offcanvasThreshold) && offcanvasThreshold > 0) {
      var offcanvasProgress = Math.min((offcanvasTotal / offcanvasThreshold) * 100, 100);
      offcanvasProgressElement.style.width = offcanvasProgress + "%";
      offcanvasProgressElement.setAttribute("aria-valuenow", offcanvasProgress);
    }
  }
}

// Update cart quantity and synchronize it with the server
function updateQuantity(button, action) {
  const input = button.closest(".input-group").querySelector(".qty_input");
  let currentValue = parseInt(input.value);
  const itemId = button.getAttribute("data-item_id");

  if (action === "increment") {
    if (currentValue < parseInt(input.max)) {
      input.value = currentValue + 1;
    }
  } else if (action === "decrement") {
    if (currentValue > parseInt(input.min)) {
      input.value = currentValue - 1;
    } else if (currentValue === 1) {
      removeFromCart(button);
      return;
    }
  }
  updateCart(itemId, input.value);
}

// Send the updated quantity to the server
function updateCart(itemId, newQuantity) {
  fetch(`/update_cart/${itemId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({ quantity: newQuantity }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        console.log("Cart updated successfully");
        updateProgressBar(); // Update the progress bar after updating the cart
      }
    })
    .catch((error) => {
      console.error("Error updating cart:", error);
    });
}

// Remove item from cart
function removeFromCart(button) {
  const itemId = button.getAttribute("data-item_id");
  fetch(`/remove_from_cart/${itemId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        document.getElementById(`item_${itemId}`).remove();
        console.log("Item removed from cart successfully");
        updateProgressBar();
      }
    })
    .catch((error) => {
      console.error("Error removing item from cart:", error);
    });
}

// Retrieve CSRF token for AJAX requests
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
