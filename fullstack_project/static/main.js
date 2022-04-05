
function hideText(y) {
    var x = document.getElementById(y);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }


//#########  Dark mode with saved settings ############

let darkMode = localStorage.getItem('darkMode');

const enableDarkMode = () => {
    document.body.classList.add("dark-mode");
    localStorage.setItem("darkMode", true);

    //##########  Hide/show dark moe icons
    document.getElementById("dark-mode-toggle").style.display ="none"; 
    document.getElementById("light-mode-toggle").style.display ="block";
}
const disableDarkMode = () => {
    document.body.classList.remove("dark-mode");
    localStorage.setItem("darkMode", false);

    document.getElementById("dark-mode-toggle").style.display ="block";
    document.getElementById("light-mode-toggle").style.display ="none";
}

if (darkMode === "true"){
    enableDarkMode();
} else{
    disableDarkMode();
};


const darkModeToggle = document.querySelector("#dark-mode-toggle");
darkModeToggle.addEventListener("click" , () => {
    darkMode = localStorage.getItem("darkMode");
    if (darkMode !== "true") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});

const lightModeToggle = document.querySelector("#light-mode-toggle");
lightModeToggle.addEventListener("click" , () => {
    darkMode = localStorage.getItem("darkMode");
    if (darkMode !== "true") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});


//##################################################