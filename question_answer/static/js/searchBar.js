function search() {
    window.onload = () => {
        let input = document.querySelector('#search-field');
        input.oninput = function() {
            let value = this.value.trim(); // Catch the entered letters in the input
            let list = document.querySelectorAll('.group');

            if(value) {
                list.forEach(elem => {
                   if (elem.innerText.search(value) === -1) {
                       elem.classList.add('hide');
                   }
                });
            } else {
                list.forEach(elem => {
                    elem.classList.remove('hide')
                });
            }
        };
    };
}

search();

const audio = new Audio("https://www.fesliyanstudios.com/play-mp3/387");
const buttons = document.querySelectorAll(".link");

buttons.forEach(button => {
      button.addEventListener("click", () => {
      audio.play();
  });
});