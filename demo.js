// scripts.js

document.getElementById("deliveryForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const itemName = document.getElementById("itemName").value;
    const deliveryLocation = document.getElementById("deliveryLocation").value;
    const statusMessage = document.getElementById("statusMessage");
    statusMessage.textContent = `Request received for ${itemName}. Delivery location: ${deliveryLocation}.`;
  });
  