const signupForm = document.getElementById('signupForm');

signupForm.addEventListener('submit', function(event) {
  const firstName = document.getElementById('firstname').value.trim();
  const lastName = document.getElementById('lastname').value.trim();
  const username = document.getElementById('username').value.trim();
  const email = document.getElementById('email').value.trim();
  const password1 = document.getElementById('password1').value.trim();
  const password2 = document.getElementById('password2').value.trim();
  let isValid = true;

  const errors = document.querySelectorAll('.error');
  errors.forEach(error => error.remove());

  if (firstName === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your first name.';
    document.getElementById('firstname').after(error);
  }

  if (lastName === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your last name.';
    document.getElementById('lastname').after(error);
  }

  if (username === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your username.';
    document.getElementById('username').after(error);
  }

  if (email === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your email.';
    document.getElementById('email').after(error);
  }

  if (password1 === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please enter your password.';
    document.getElementById('password1').after(error);
  }

  if (password2 === '') {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Please confirm your password.';
    document.getElementById('password2').after(error);
  } else if (password1 !== password2) {
    isValid = false;
    const error = document.createElement('div');
    error.className = 'error';
    error.style.color = 'red';
    error.textContent = 'Passwords do not match.';
    document.getElementById('password2').after(error);
  }

  if (!isValid) {
    event.preventDefault();
  }
});
