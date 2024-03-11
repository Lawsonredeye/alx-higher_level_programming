# Javascript Learning

Javascript is a powerful programming language which is used to add interactivity to a website and also build frontend web Application Program Interface (API).

Its versatile and beginner-friendly and with much exeprience users can build games, animate graphics in both 2D and 3D as well as comprehensive database-driven apps.

## VARIABLES

Variables are containers that stores datas and Javascript has three ways of creating variables and these are:

1. **const**: which creates a constant thats local to that directory and also the value assisgned to it remains the same across the source code.
   `const myVariable = 'John';`
2. **let**: creates a variable that its values can change but cant be redeclared after being created. It provides more security than the **var**.
   `let newVariable = 16;`
3. **var**: this creates variables which can store values but can be redeclared at any time within a source code.
   `var myVariable = 10;`

## DATATYPES

Javascript like other languages has datatypes and these datatypes are very easy to understand.

1. Strings: used for creating sequence of text strings and they are enclosed in either single or double quotes but for those using a checker such as semi-standard the single quotes is best used for creating strings.
   `let myVariable = 'Lawson Redeye';` // string datatype

2. Number: this is just a number and they dont use quotes around them when being assigned as a value to a variable.

It recognises both floating-point numbers and intergers as well. for larger values use the big-int.

`let myNumber = 58.6;`
`let myAge = 75;` // PS i am not 75
`let x = BigInt(999999999999999);`

3. Boolean: This just create a true/false value to a variable and dont require quotation marks around them.
   `let myvariable = true;`

4. Array: This allows you to store multiple values as well as datatypes in a single variable. it is denoted by square brackets [].
   `let myArray = [];` // empty array
   `let myArray = ['Lawson', 46, true, 0];`

The members of an array can be accessed using the name of the variable together with the square bracket and the index number e.g
`myArray[0];` //would return the string 'Lawson'

4. Objects: everything in javascript is an object and can be stored in a variable. Most object are denoted by the curly brackets {}.
   `let person = {};` // empty object
   let anotherPerson = {
   name : 'Lawson',
   age : 56,
   id : 25864,
   };

## COMMENTS

This can be written just like it is written in C language where we can write multi-line comments and single line comments.
Multiline comments:
\\_
Everything in between is a comment.
\\_

single line comment:
// this is a comment
