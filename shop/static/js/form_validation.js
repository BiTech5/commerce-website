// Get the form element
const form = document.getElementById('contactForm');

// Add an event listener for form submission
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting

  // Get form field values
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const phone = document.getElementById('phone').value.trim();
  const message = document.getElementById('message').value.trim();

  // Validate form fields
  let isValid = true;

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phonePattern = /^\d{10}$/;
  //name validation
  if (name === '') {
    isValid = false;
    alert('Please enter your name.');
  }

  // Email validation
  else if (!emailPattern.test(email)) {
    isValid = false;
    alert('Please enter a valid email address.');
  }

  // Phone validation
  else if (!phonePattern.test(phone)) {
    isValid = false;
    alert('Please enter a valid 10-digit phone number.');
  }

  // Message validation
  else if (message === '') {
    isValid = false;
    alert('Please enter a message.');
  }

  // If form is valid, submit the form
  if (isValid) {
    // Add your form submission logic here
    alert('Form submitted successfully!');
    form.reset(); // Reset the form after submission
  }
});