// Initialize these three variables
var a = 5;
var b = 10;
var c = "I am a string";

// Do not change code below this line

a += 1;
b += 5;
c = c +" String!";

// Math

var sum = 10 + 10;
console.log(sum);

var difference = 45 - 33;
console.log(difference);

// regular operators apply + - * /

// Increment 

var myVar = 1;
myVar++;
myVar--;

var myDecimal = 0.008;

var remainder;
remainder = 11 % 3;

myVar *= 10;
console.log(myVar);

myVar /= 10;
console.log(myVar);

// Escape characters \

var myStr = "\"Mathieu\"";
console.log(myStr);

var myStr2 = '"Mathieu"';
console.log(myStr2);

var myStr3 = `'"Woah single and double quotes, how did he do that?"'`;
console.log(myStr3);

// Concatenate strings

var ourStr = "I come first. " + "I come second.";

var ourStr2 = "I come third. ";
ourStr2 += "I come fourth.";

// Length of a string

console.log(ourStr.length)

// Indexing

console.log(ourStr[0])
console.log(ourStr[ourStr.length - ourStr.length + 1])

// The characters of strings are immutable

// Arrays

var ourArray = ["John", 23, [1, 2, 3]]

console.log(ourArray[2])

// Array indexes are mutable

ourArray[0] = `Mathieu`

console.log(ourArray[0])

// Append data to the end of an array with push ourArray.push()

ourArray.push('Jackson', 'Charles', 'Fargo')

console.log(ourArray)

// Remove last variable using ourArray.pop()

ourArray.pop()

ourArray.shift()
console.log(ourArray) // shift to the left
ourArray.unshift("Lucas") // adds Lucas to the start of the array 