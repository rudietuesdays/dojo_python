// var HOUR;
// var MINUTE;
// var PERIOD;
// var TIME = [HOUR, MINUTE, PERIOD];

console.log("working");

function haveTime(TIME) {

    var BEFOREAFTER;
    var MORNNITE;

    if ((TIME[0] < 1) || (TIME[0] > 12) || (TIME[1] < 1) || (TIME[1] > 59)) {
        console.log("That is not a valid time!");

    } else {

        if (TIME[1] == 30) {
            BEFOREAFTER = "half past"
        } else if (TIME[1] == 15) {
            BEFOREAFTER = "a quarter after"
        } else if (TIME[1] == 5) {
            BEFOREAFTER = "5 after"
        } else if (TIME[1] < 30) {
            BEFOREAFTER = "just after";
        } else if (TIME[1] > 30) {
            BEFOREAFTER = "almost";
            TIME[0] += 1;
        }

        if (TIME[2] == "AM") {
            MORNNITE = "morning";

        } else if (TIME[2] == 'PM') {
            if (TIME[0] <= 4)
                MORNNITE = "afternoon";
            }
            else if (TIME[0]>4) {
                MORNNITE="evening";
            }
        }

        console.log("It's", BEFOREAFTER, TIME[0], "in the", MORNNITE, ".");

    }

haveTime([1, 15, "PM"]);
