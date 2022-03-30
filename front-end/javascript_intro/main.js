
//single line comment

/*
multi line comment
*/
//! DATA TYPES

let dataType = "this is a string";       //string data type

dataType = 1234;                  //this is an integer

dataType = 12.34                    // float data type

dataType = true                       // boolean data type

//! VARIABLES

console.log("hello world"); //view in inspect page

var myFirstName = 'James';  //this is legacy code

const mySurname = "Burgess" ;// 'const' canot be updated

let myAge = "24" ;// 'let' can be updated

myAge = "25";

//! IF STATEMENTS

if (myAge === "25"){
    console.log("James is 25");
} else if (myAge === "24"){
    console.log("James is 24");
} else {
    console.log("Nobody knows James' age");
}

if (myFirstName === "James" && mySurname === "Burgess"){  // && is and
    console.log("His name is James Burgess");
} else {
    console.log("Nobody knows his name");
}

if (myAge === "25" || myAge === "24"){                   // || is or
    console.log("I know");
} else {
    console.log("I don't know");
}

//! FUNCTIONS

function myFunction(){
    console.log("This is a function")
}
myFunction()