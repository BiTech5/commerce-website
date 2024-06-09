const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(event) {
  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();
  let isValid = true;

  const usernameError = document.getElementById('usernameError');
  const passwordError = document.getElementById('passwordError');
  if (usernameError) usernameError.remove();
  if (passwordError) passwordError.remove();

  if (username === '') {
    isValid = false;
    const error = document.createElement('div');
    error.id = 'usernameError';
    error.style.color = 'red';
    error.textContent = 'Please enter your username.';
    document.getElementById('username').after(error);
  }

  if (password === '') {
    isValid = false;
    const error = document.createElement('div');
    error.id = 'passwordError';
    error.style.color = 'red';
    error.textContent = 'Please enter your password.';
    document.getElementById('password').after(error);
  }

  if (!isValid) {
    event.preventDefault();
  }
});
