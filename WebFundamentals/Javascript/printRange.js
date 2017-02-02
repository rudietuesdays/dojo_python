// Make sure the console is logging correctly:
console.log('working');

// Create a function to take start, end and skip amount
// function printRange(a,b,c){
//         for (var i = a; i <b; i+=c) {
//             console.log(i);
//         }
// }

// play with the input data to test the function
// printRange (4,21,3)

// BONUS QUESTIONS
function printRange(a,b,c){
    //if the skip amount is 0 or negative, set the skip amount to 1
    if (c==0 || c<0) {
        c=1;
    }
    //if the end point is a smaller value than the start point, set the start point to 0 and the end point to the start point
    if (b<a) {
        b=a;
        a=0;
    }

    for (var i = a; i <b; i+=c) {
        console.log(i);
    }

    //if the user doesn't pass a skip amount, set the skip amount to 1
    // function printRange(a,b){
    //     for (var i = a; i <b; i++) {
    //         console.log(i);
    //     }
    // }

    //if the user doesn't pass an end point, set the start point to 0 and the end point to the start point
    // function printRange(a,c){
    //     for (var i = 0; i < a; i+=c) {
    //         console.log(i);
    //     }
    // }

}

// play with the input data to test the function
printRange(6,10,0)
