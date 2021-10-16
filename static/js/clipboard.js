$( document ).ready(function() {
    console.log( "ready!" );

    const codeBlocks = document.querySelectorAll('.code-block');
    const copyCodeButtons = document.querySelectorAll('.copy-code');
    
    copyCodeButtons.forEach((copyCodeButton, index) => {
      const code = codeBlocks[index].innerText;
      const icon = copyCodeButtons[index].children[0]
      const button = copyCodeButtons[index]



      copyCodeButton.addEventListener('click', () => {
        window.navigator.clipboard.writeText(code);
        
        console.log(code)

        if (icon.classList.contains("ti-clipboard")){
            icon.classList.remove("ti-clipboard")
            icon.classList.add("ti-check")

            button.style.backgroundColor = "green";

            setTimeout(()=>{
                icon.classList.add("ti-clipboard")
                icon.classList.remove("ti-check")
                button.style.backgroundColor = null
            }, 1000)
        }

      });
    });
});


