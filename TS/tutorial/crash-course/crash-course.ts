let id: number = 5;
let company: string = "Me";
let isTrue: boolean = true;

//Specific types

let ids: number[] = [1,2,3,4,5]
let x: any = "pepdro"
let xArr: any[] = ["oer", 5, true] 

//use any type in extreme scenerios

// let a = "hello"
// let b = "world"

//adding return type for a function
const concat = (a: any, b: any): string =>{
    return a+b;
}

console.log(concat("hello", "world"))
console.log(concat(5, 20))


//for opjects, we need to have a blueprint, which is an object interface

interface UserInterface {
    id: number, 
    name: string,
    age?: number,
    greet(message: string): void;
    nine(a: number, b: number): number;
}

//when you want to make a parameter optional, you can put a question mark
const User: UserInterface = {
    id: 2,
    name: "Pedro", 
    // age: 22,
    greet(message){
        console.log(message)
    },
    nine(a, b){
        return a+b
    }
}

// if (!User.age){
//     console.log("No user is defined")
// }else{
//     console.log(User.age)
// }

//sending functions

User.greet("Good day sir");
console.log("Nine plus ten is", User.nine(9,10))



////////////////////////////////////////////////////////////////////////////////////////
//Can also deal with bad data, data that eithe isnt formatted or expected output

//can use union which can be either that or other with " | " or you can do a custom type. Interface is mostly done for objects but type is used for single fields

//also known as type alias

type IDFieldType = string | number

const printID = (id: IDFieldType) =>{
    console.log("ID:", id)
}

printID(342304923)

interface BusinessPartner {
    name: string,
    creditScore: number,
}

interface UserIdentity {
    id: number,
    email: string,
}

type Employee = BusinessPartner & UserIdentity

//with this function, which is of tupe union, we can get a parameter from BusinessPartner and a parameter from UserIdentity

//In this case, you have the intersection of both types instead of union, employ IS of objects of both types, where as if we were to use union, it could be of ONE of the tupes
const signContract = (employee: Employee) => {
    console.log("Contract signed by " + employee.name + " with email " + employee.email)
}

signContract({name: "Pedro", creditScore: 800, id: 124, email: "email.gon"})

//ENUMS

//defining a set of named constants

//can have unauthorized, doesn't exist, wrong credentials, internal error

enum LoginError {
    Unauthorized = "unauthorized",
    NoUser = "nouser",
    wrongCredentials = "wrongcredentials"
}

const printErrorMsg = (error: LoginError) => {
    
    if (error == LoginError.NoUser)
    
    console.log(error)
}


//Generic Iterms, storage container class

//should be taking in various different datatypes so should be using a T
class StorageContainer<T> {
    //array of different types of things
    private contents: T[]

    constructor(){
        this.contents = [];
    }

    addItem(item: T): void{
        this.contents.push(item)
    }

    getItem(indx: number): T | undefined{
        return this.contents[indx];
    }
}

const usernames = new StorageContainer<string>();
usernames.addItem("me")
usernames.addItem("myself")
usernames.addItem("I")
console.log(usernames.getItem(1))

const idNum = new StorageContainer<number>();

//Read only variables
interface Employee2{
    readonly employee: number
}