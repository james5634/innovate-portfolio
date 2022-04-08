
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

    //##########  Hide/show dark mode icons
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


//#########################################################

const floatNavBar = () =>{
    let scrollPosition = window.scrollY
    const nav = document.querySelector("#main-bar-float");

    var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;

    if(scrollPosition < 150 & width > 490){
        nav.classList.remove("float_left")

    }else if (scrollPosition > 151 & width > 490){
        nav.classList.add("float_left")
    };
};

window.addEventListener("scroll",floatNavBar)

//#########################################################
function floatNavBarSmall() {
    const nav = document.querySelector("#main-bar-float");
    const hamburger = document.querySelector("#hamburger_menu");

    nav.classList.toggle("float_left");
    hamburger.classList.toggle("float_left_hamburger");
};

// window.addEventListener("click",floatNavBar)

// Create date from input value
function countdowns(specialDay, specialBear) {
    // var specialDay = "2022/03/16";
    var inputDate = new Date(specialDay);   //panda day
    var todaysDate = new Date();

    if(new Date().setHours(0,0,0,0) === new Date(specialDay).setHours(0,0,0,0)) {
        document.getElementById(specialBear).innerHTML = "It's Today!";
        console.log("its the day");
    } else {

        if (inputDate.getTime() - new Date().getTime() < 0){
            inputDate.setFullYear(todaysDate.getFullYear() +1 )
        };
        
        var x = setInterval(function() {
        
            var distance = inputDate.getTime() - new Date().getTime();
        
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
            document.getElementById(specialBear).innerHTML = days + "d " + hours + "h "
            + minutes + "m " + seconds + "s ";
        
        }, 100);
    };

};
if (window.location.pathname=='/bear-days') {
    countdowns("2022/03/16","panda-day");
    countdowns("2022/02/27","polar-bear-day");
    countdowns("2022/09/09","teddy-bear-day");
}









