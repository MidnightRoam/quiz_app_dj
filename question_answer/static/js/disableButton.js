checkBoxes = document.querySelectorAll('.checkbox');
btn = document.getElementById('btn');

checkBoxes.forEach((checkBox) => {
    checkBox.addEventListener('change', event => {
        if (checkBox.checked) {
            btn.classList.remove('disabled');
            btn.textContent = 'Next'
        } else {
            btn.classList.add('disabled');
            btn.textContent = 'Submit answer'
        }
    })
})

