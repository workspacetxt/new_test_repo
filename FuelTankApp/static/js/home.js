const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".menu-links"),
      modeSwitch = body.querySelector(".toggle-switch")
      modeText = body.querySelector(".mode-text");


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
    }else{
        modeText.innerText = "Dark mode";
        
    }
});




function submitPopupForm() {
    // Check the selected radio button
    var yesRadio = document.getElementById("yes");
    
    if (yesRadio.checked) {
      // If "Yes" is selected, submit the main form
      document.getElementById("shiftForm1").submit();
    } else {
      // If "No" is selected, do nothing or provide feedback to the user
      closePopupForm() ;
    }
  }


  function openPopupForm() {
    document.getElementById('popupForm').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupForm() {
    document.getElementById('popupForm').style.display = 'none';
  }


  function openPopupFormA() {
    document.getElementById('popupFormA').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormA() {
    document.getElementById('popupFormA').style.display = 'none';
  }

  function submitPopupFormA() {
    // Get the value entered in the "fname" input field
    var fnameValueA = document.getElementById('fnameInputA').value;

    // Set the captured value in the "field11" input field
    document.getElementById('Azone').value = fnameValueA;

    // Close the popup form
    closePopupFormA();
  }


  function openPopupFormB() {
    document.getElementById('popupFormB').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormB() {
    document.getElementById('popupFormB').style.display = 'none';
  }


  function submitPopupFormB() {
    // Get the value entered in the "fname" input field
    var fnameValueB = document.getElementById('fnameInputB').value;

    // Set the captured value in the "field11" input field
    document.getElementById('Bzone').value = fnameValueB;

    // Close the popup form
    closePopupFormB();
  }

  function openPopupFormC() {
    document.getElementById('popupFormC').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormC() {
    document.getElementById('popupFormC').style.display = 'none';
  }
  
  function submitPopupFormC() {
    // Get the value entered in the "fname" input field
    var fnameValueC = document.getElementById('fnameInputC').value;
  
    // Set the captured value in the "field11" input field
    document.getElementById('Czone').value = fnameValueC;
  
    // Close the popup form
    closePopupFormC();
  }

  function submitPopupFormC() {
    // Get the value entered in the "fname" input field
    var fnameValueC = document.getElementById('fnameInputC').value;

    // Set the captured value in the "field11" input field
    document.getElementById('Czone').value = fnameValueC;

    // Close the popup form
    closePopupFormC();
  }

  function openPopupFormD() {
    document.getElementById('popupFormD').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormD() {
    document.getElementById('popupFormD').style.display = 'none';
  }

  function submitPopupFormD() {
    // Get the value entered in the "fname" input field
    var fnameValueD = document.getElementById('fnameInputD').value;
  
    // Set the captured value in the "field11" input field
    document.getElementById('Dzone').value = fnameValueD;
  
    // Close the popup form
    closePopupFormD();
  }

  function openPopupFormE() {
    document.getElementById('popupFormE').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormE() {
    document.getElementById('popupFormE').style.display = 'none';
  }


  function submitPopupFormE() {
    // Get the value entered in the "fname" input field
    var fnameValueE = document.getElementById('fnameInputE').value;
  
    // Set the captured value in the "field11" input field
    document.getElementById('Ezone').value = fnameValueE;
  
    // Close the popup form
    closePopupFormE();
  }

  function openPopupFormF() {
    document.getElementById('popupFormF').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormF() {
    document.getElementById('popupFormF').style.display = 'none';
  }


  function submitPopupFormF() {
    // Get the value entered in the "fname" input field
    var fnameValueF = document.getElementById('fnameInputF').value;
  
    // Set the captured value in the "field11" input field
    document.getElementById('Fzone').value = fnameValueF;
  
    // Close the popup form
    closePopupFormF();
  }

  function openPopupFormG() {
    document.getElementById('popupFormG').style.display = 'block';
  }

  // Function to close the popup form
  function closePopupFormG() {
    document.getElementById('popupFormG').style.display = 'none';
  }

  function submitPopupFormG() {
    // Get the value entered in the "fname" input field
    var fnameValueG = document.getElementById('fnameInputG').value;
  
    // Set the captured value in the "field11" input field
    document.getElementById('Gzone').value = fnameValueG;
  
    // Close the popup form
    closePopupFormG();
  }


  