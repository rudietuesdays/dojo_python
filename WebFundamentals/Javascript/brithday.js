// Make sure the console is logging correctly:
// console.log('working');

for (var daysLeft=60; daysLeft>=0; daysLeft-- ){
    if (daysLeft==0){
        console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
        console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
        console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
    }
    else if (daysLeft == 1) {
        console.log(daysLeft, "DAY UNTIL MY BIRTHDAY!!");
    }
    else if (daysLeft<=5) {
        console.log(daysLeft, "DAYS UNTIL MY BIRTHDAY!!");
    }

    else if (daysLeft<=30) {
        console.log("Only", daysLeft, "days until my birthday!");
    }
    else if (daysLeft>30) {
        console.log(daysLeft, "days until my birthday. Will it ever arrive?? :(");
    }
}
