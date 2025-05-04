//Functions are used to model algorithims and values
//Break into smaller problems, and by combining, you will get closer to the result.
//treating functions as values
//no for or while loops, we will look at recursion functions
//just read them linearly and more bugs found in compile time, also more reusable

//where functions are transformations, pretend a pipe, where each input is mapped to 1 ouput, only 1 input for 1 output
//can never do sideeffects, wont W/R to files, db's. Do all side effects later. 
//Never mutate, only create new variables from old ones, 

//Referential transpaery means you can replace a function with its defination

//Functional programming is all about composing values
//functions are values too

//if you have 2 functions, 1 is increment and another is to_string, you can just call their definations and 

const increment = (x: number): number => x + 1;

console.log(increment(2))