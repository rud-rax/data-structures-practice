
function reverseString(str) {
    // alert("In function !");

    let ns = "";
    for (let i = str.length -1 ; i >= 0 ; i-- ){
        ns += str[i] ;


    }

    return ns ;
}


// let s = prompt('Enter a string : ');
let s = "hello world" ; 

let ns = reverseString(s);
console.log(ns);