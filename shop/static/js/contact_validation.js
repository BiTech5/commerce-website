const contactForm = document.getElementById('contactForm');

contactForm.addEventListener('submit', function(event) {
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const phone = document.getElementById('phone').value.trim();
  const message = document.getElementById('message').value.trim();
  let isValid = true;

  // Clear previous error messages
  const errors = document.querySelectorAll('.error');
  errors.forEach(error => error.remove());

  if (name === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your name.';
    document.getElementById('name').after(error);
  }

  if (email === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your email.';
    document.getElementById('email').after(error);
  } else {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      isValid = false;
      const error = document.createElement('div');
      error.className = 'error';
      error.style.color = 'red';
      error.textContent = 'Please enter a valid email address.';
      document.getElementById('email').after(error);
    }
  }

  if (phone === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your phone number.';
    document.getElementById('phone').after(error);
  }

  if (message === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your message.';
    document.getElementById('message').after(error);
  }

  if (!isValid) {
    event.preventDefault();
  }
});
