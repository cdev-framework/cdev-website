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


    const codeSnippets = document.querySelectorAll('.code-snippet');
    const copyCodeSnippetButtons = document.querySelectorAll('.copy-code-snippet');
    
    console.log(codeSnippets)

    copyCodeSnippetButtons.forEach((copyCodeButton, index) => {
      const code = codeSnippets[index].innerText;
      const icon = copyCodeSnippetButtons[index].children[0]
      const button = copyCodeSnippetButtons[index]



      copyCodeButton.addEventListener('click', () => {
        window.navigator.clipboard.writeText(code.substring(2));

        console.log(icon.classList)
        if (icon.classList.contains("ti-clipboard")){
            
          icon.classList.remove("ti-clipboard")
          icon.classList.add("ti-check")
          
          button.classList.remove('btn-secondary')
          button.classList.add('btn-success')
          
          //icon.classList.add("ti-check")

          console.log("HERE")
          console.log(icon.classList)

          setTimeout(()=>{
              icon.classList.add("ti-clipboard")
              icon.classList.remove("ti-check")
              
              button.classList.add('btn-secondary')
              button.classList.remove('btn-success')
              
          }, 1000)
        }

      });
    });
});


