# 0x13. JavaScript - Objects, Scopes and Closures

When it comes to JS there are several ways of implementing Object oriented programming and just like Python, JS has such ablity from creating and inheriting of classes as well as objects.

when it comes to Object, almost everything in JS can be treated as an Object or as a value to an object ranging from functions and several datatypes as well as an object itself.

This makes JavaScript very powerful when it comes to OOP.

There are things to also noted about scopes when it comes to JS. Both the const and let which allows you to create a variable can be accessed if a function is declared and defined immediately after the let and const variable has been initialized

Closures are just functions defined within a function in which the inner functions with in the outer function is made private and only accessible with in the scope of that function, values can't be changes unless the outer function returns all inner function in an object e.g `return {innerFunction1, innerFunction2 ... innerFunctionX};`

```Function gameHost() {
        let score = 0;
        function addScore(points) {
                score += points;
                console.log(`+${points}pts`);
        }
        function removeScore(points) {
                score -= points;
                console.log(\`-${points}pts');
        }
        function getScore() {
                return score;
        }
        return {addScore, removeScore, getScore};
}
```
