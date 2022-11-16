// for (var i = 0; i < 10; i++){
//     console.log(i);
// }

// console.table(["orange", "strawberry", "banana"])

// //Runner If/Then/Else

// const runner = "Kendyll";
// const position = 2;
// let medal;

// if(position === 1) {
//   medal = "gold";
// } else if(position === 2) {
//   medal = "silver";
// } else if(position === 3) {
//   medal = "bronze";
// } else {
//   medal = "pat on the back";
// }

// console.log(runner + " received a " + medal + " medal.");

// //Musicians If/Then/Else
// const musicians = 76;

// if (musicians <= 0)
//     console.log("Not a group");
// else if (musicians === 1)
//     console.log("Solo");
// else if (musicians === 2)
//     console.log("Duet");
// else if (musicians === 3)
//     console.log("Trio")
// else if (musicians === 4)
//     console.log("Quartet")
// else
//     console.log("This is a large group!")


// Programming Quiz: Murder Mystery
// const room = "ballroom";
// const suspect = "Mr. Kalehoff"; 

// let weapon = "";
// let solved = false;

// if (suspect === "Mr. Parkes") 
// {
//     if(room === "billiards room")
//         weapon = "pool stick";
//     else if(room === "gallery")
//         weapon = "trophy";
//     else if (room === "ballroom")
//         weapon = "poison";
//     else
//     {
//         weapon = "knife";
//         solved = true;
//     }

// } else if (suspect === "Ms. Van Cleve") {
//     if(room === "billiards room")
//         weapon = "pool stick";
//     else if(room === "gallery")
//         {
//             weapon = "trophy";
//             solved = true;
//         }
//     else if (room === "ballroom")
//         weapon = "poison";
//     else
//         weapon = "knife";
    
// } else if (suspect === "Mrs. Sparr") {
//     if(room === "billiards room")
//     {
//         weapon = "pool stick";
//         solved = true;
//     }
//     else if(room === "gallery")
//         weapon = "trophy";
//     else if (room === "ballroom")
//         weapon = "poison";
//     else
//         weapon = "knife";

// } else {
//     if(room === "billiards room")
//         weapon = "pool stick";
//     else if(room === "gallery")
//         weapon = "trophy";
//     else if (room === "ballroom")
//     {
//         weapon = "poison";
//         solved = true;
//     }
//     else
//         weapon = "knife";
// }

// if (solved) {
//     console.log(suspect + " did it in the " + room + " with the " + weapon + "!");
// } else {
//   console.log("The case is not solved!")
// }


//ATM Quiz
// const balance = 0
// const checkBalance = true;
// const isActive = false;

// if(checkBalance === false)
//     console.log("Thank you. Have a nice day!")
// else if(checkBalance === true && isActive === true && balance > 0)
//     console.log("Your balance is $" + balance + ".")
// else if(checkBalance === true && isActive === false)
//     console.log("Your account is no longer active.")
// else if(checkBalance === true && isActive === true && balance === 0)
//     console.log("Your account is empty.")
// else
//     console.log("Your balance is negative. Please contact the bank.")

//Ice Cream Quiz
// const flavor = "strawberry";
// const topping = "bananas";
// const vessel = "sugar cone";

// if((flavor === "vanilla" || flavor === "chocolate") && (topping === "sprinkles" || topping === "peanuts") && (vessel === "wafer cone" || vessel === "sugar cone"))
//     console.log("Great choice! Your ice cream is at the next window!")
// else
//     console.log("Please check our menu and try again.")

// Shirt Size Quiz
// const shirtWidth = 21;
// const shirtLength = 99;
// const shirtSleeve = 8.40;

// // your code here
// let size = "NA";

// if ((shirtWidth>=18 && shirtWidth<20) && (shirtLength>=28 && shirtLength<29) && (shirtSleeve>=8.13 && shirtSleeve<8.38) ) {
//     size = "S";
// }
// else if ((shirtWidth>=20 && shirtWidth<22) && (shirtLength>=29 && shirtLength<30) && (shirtSleeve>=8.38 && shirtSleeve<8.63) ) {
//     size = "M";
// }
// else if ((shirtWidth>=22 && shirtWidth<24) && (shirtLength>=30 && shirtLength<31) && (shirtSleeve>=8.63 && shirtSleeve<8.88) ) {
//     size = "L";
// }
// else if ((shirtWidth>=24 && shirtWidth<26) && (shirtLength>=31 && shirtLength<33) && (shirtSleeve>=8.88 && shirtSleeve<9.63) ) {
//     size = "XL";
// }
// else if ((shirtWidth>=26 && shirtWidth<28) && (shirtLength>=33 && shirtLength<34) && (shirtSleeve>=9.63 && shirtSleeve<10.13) ) {
//     size = "2XL";
// }
// else if ((shirtWidth>=28) && (shirtLength>=34) && (shirtSleeve>=10.13) ) {
//     size = "3XL";
// }
// else {
//     size = "NA";
// }
// console.log(size);

// change the values of `eatsPlants` and `eatsAnimals` to test your code
// const eatsPlants = false;
// const eatsAnimals = false;
// let category;

// // your code goes here
// eatsPlants ? (eatsAnimals ? category = "Omnivore" : category = "Herbivore") : (eatsAnimals ? category ="Carnivore" : category = "undefined")

// console.log(category);

//FizzBuzz
// let x = 1

// while(x < 100)
// {

// 	if ((x % 5 === 0) && (x % 3 === 0))
// 		console.log("FizzBuzz")
// 	else if (x % 3 === 0)
// 		console.log("Fizz")
// 	else if (x % 5 === 0)
// 		console.log("Buzz")
// 	else
// 		console.log(x)
// 	x = x + 1
// }

//99 Bottles
// let num = 99;

// while (num > 0) {
// 	if(num === 2)
// 		console.log(num + " bottles of juice on the wall! " + num + " bottles of juice! Take one down, pass it around... " + (num - 1) + " bottle of juice on the wall!")
//     else if(num === 1)
//     	console.log(num + " bottle of juice on the wall! " + num + " bottle of juice! Take one down, pass it around... " + (num - 1) + " bottles of juice on the wall!")
//     else
//     	console.log(num + " bottles of juice on the wall! " + num + " bottles of juice! Take one down, pass it around... " + (num - 1) + " bottles of juice on the wall!")
//     num = num - 1;
// }

//Nasa Countdown
// let countdown = 60;

// while(countdown >= 0)
// {
// 	if(countdown === 50)
// 		console.log("Orbiter transfers from ground to internal power.")
// 	else if(countdown === 31)
// 		console.log("Ground launch sequencer is go for auto sequence start.")
// 	else if(countdown === 16)
// 		console.log("Activate launch pad sound suppression system.")
// 	else if(countdown === 6)
// 		console.log("Main engine start.")
// 	else if(countdown === 0)
// 		console.log("Solid rocket booster ignition and liftoff!")
// 	else
// 		console.log("T-" + countdown + " seconds.")
// 	countdown = countdown - 1;
// }

//For loop
for(let k = 0; k < 26; k++){
	for(let j = 0; j < 100; j++){
		console.log(k + "-" + j)
	}
}