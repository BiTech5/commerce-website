document.addEventListener('DOMContentLoaded', function() {
    const decrementBtn = document.getElementById('decrement-btn');
    const incrementBtn = document.getElementById('increment-btn');
    const quantityInput = document.getElementById('quantity-input');

    decrementBtn.addEventListener('click', function() {
        let quantity = parseInt(quantityInput.value);
        if (quantity > 0) {
            quantityInput.value = quantity - 1;
        }
    });

    incrementBtn.addEventListener('click', function() {
        let quantity = parseInt(quantityInput.value);
        quantityInput.value = quantity + 1;
    });

    quantityInput.addEventListener('input', function() {
        let quantity = parseInt(this.value);
        if (isNaN(quantity) || quantity < 0) {
            this.value = 0;
        }
    });
});