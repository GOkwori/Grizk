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

  // Progress Bar Calculation
  var totalElement = document.getElementById("delivery-progress");
  if (totalElement) {
    var total = parseFloat(totalElement.getAttribute("data-total"));
    var freeDeliveryDelta = parseFloat(
      totalElement.getAttribute("data-free-delivery-delta")
    );
    if (
      !isNaN(total) &&
      !isNaN(freeDeliveryDelta) &&
      total + freeDeliveryDelta !== 0
    ) {
      var progress = (total / (total + freeDeliveryDelta)) * 100;
      totalElement.style.width = progress + "%";
    }
  }
});

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
