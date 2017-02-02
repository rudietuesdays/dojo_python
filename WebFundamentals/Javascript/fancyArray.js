// Make sure the console is logging correctly:
console.log('working');

function printNames(names){
    for (var i = 0; i < names.length; i++) {
        console.log(i, "->", names[i]);
    }
}

printNames(["James", "Jill", "Jane", "Jack"])
