document.addEventListener("DOMContentLoaded", function () {
  var navbarToggler = document.querySelector(".navbar-toggler");
  var pageContent = document.getElementById("page-content");
  var header = document.getElementById("main-header");
  var isNavCollapsed = true;

  navbarToggler.addEventListener("click", function () {
    setTimeout(function () {
      isNavCollapsed = !isNavCollapsed;
      if (!isNavCollapsed) {
        pageContent.style.marginTop = "30%";
      } else {
        pageContent.style.marginTop = "";
      }
    }, 100); // Delay to ensure the collapse animation completes
  });

  var toastElList = [].slice.call(document.querySelectorAll(".toast"));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
  });
  toastList.forEach((toast) => toast.show());

  updateProgressBar();
});

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

  // For the offcanvas cart
  var offcanvasTotalElement = document.getElementById("offcanvas-cart-totals");
  var offcanvasProgressElement = document.getElementById(
    "offcanvas-delivery-progress"
  );
  if (offcanvasTotalElement && offcanvasProgressElement) {
    var offcanvasTotal = parseFloat(
      offcanvasTotalElement.getAttribute("data-total")
    );
    var offcanvasThreshold = parseFloat(
      offcanvasTotalElement.getAttribute("data-threshold")
    );
    if (
      !isNaN(offcanvasTotal) &&
      !isNaN(offcanvasThreshold) &&
      offcanvasThreshold > 0
    ) {
      var offcanvasProgress = Math.min(
        (offcanvasTotal / offcanvasThreshold) * 100,
        100
      );
      offcanvasProgressElement.style.width = offcanvasProgress + "%";
      offcanvasProgressElement.setAttribute("aria-valuenow", offcanvasProgress);
    }
  }
}

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
        updateProgressBar(); // Update the progress bar after removing the item
      }
    })
    .catch((error) => {
      console.error("Error removing item from cart:", error);
    });
}

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
