password1 = document.getElementById('password1');
password2 = document.getElementById('password2');
registerBtn = document.getElementById('register-btn');

password1.addEventListener('change', function() {
    checkInputs()
})

password2.addEventListener('change', function() {
    checkInputs()
})

function checkInputs() {
  if (password1.value !== '' && password2.value !== '') {
    registerBtn.classList.remove('btn__disabled');
    registerBtn.classList.add('btn');
  } else {
    registerBtn.classList.remove('btn');
    registerBtn.classList.add('btn__disabled');
  }
}

console.log(checkInputs())