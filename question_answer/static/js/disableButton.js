checkBoxes = document.querySelectorAll('.checkbox');
btn = document.getElementById('btn');
/* Added a javascript handler that removes the "disalbed" class
from the button if the question answer checkbox is selected */
checkBoxes.forEach((checkBox) => {
    checkBox.addEventListener('change', event => {
        if (checkBox.checked) {
            btn.classList.remove('hide');
            btn.textContent = 'Next'
        } else {
            btn.classList.add('hide');
            btn.textContent = 'Submit answer'
        }
    })
})

