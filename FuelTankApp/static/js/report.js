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

function disableFields(disable) {
    var select = document.getElementById("myList");
    var start = document.getElementsByName("start")[0];
    var end = document.getElementsByName("end")[0];
   
  
    select.disabled = disable;
    start.disabled = !disable;
    end.disabled = !disable;
  }

  function validateForm(event) {
   
    var station = document.getElementById("myList2").value;
    const radio1 = document.getElementById("radio1");
    const radio2 = document.getElementById("radio2");

 
  
    if (!radio1.checked && !radio2.checked) {
      showPopup3();
      event.preventDefault(); // Prevent the form from submitting
    }
   
    console.log(station);
    if (station === "") {
        showPopup();
        return false; // Prevent form submission
    }
   
  };
function showPopup() {
    document.getElementById("popupDiv").style.display = "block";
}

function closePopup() {
    document.getElementById("popupDiv").style.display = "none";
}

function closePopup3() {
    document.getElementById("popupDiv3").style.display = "none";
  }
  
  function showPopup3() {
    document.getElementById("popupDiv3").style.display = "block";
  }