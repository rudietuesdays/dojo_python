
// How much was the reward after 30 days?
// var reward = 0.01;
// for (var days = 1; days <= 30; days++) {
//     reward += reward;
// }
// console.log("The servant will get $", reward, "after 30 days.");


// How many days would it take the servant to make $10,000?
// var reward = 0.01;
// for (var days = 1; days <= 30; days++) {
//     reward += reward;
//     if (reward >= 10000) {
//         console.log("The servant will get at least $10,000 after", days, "days.");
//         break;
//     }
// }


// How many days until $1 billion?
var reward = 0.01;
var days = 1;
while (reward<=1000000000) {
    reward += reward;
    days +=1;
    if (reward>1000000000) {
        console.log("The servant will receive at least $1 billion after", days, "days.");
        break;
    }
}
