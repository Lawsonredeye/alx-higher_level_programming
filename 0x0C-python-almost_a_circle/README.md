# 0x0C. Python - Almost a circle

**Unittest is a framework** used to run and test a given code before being pushed to production.

It helps to spot errors while running/creating your code/application from scratch.

*Unittest* is done using a subclass with the unittest being passed as a parent class to the subclass.

**Syntax**
`class ExampleUnittest(unittest.TestCase):`

## Methods used with unittest.TestCase

There are several methods in the unittest library/module but the most common and repetitive methods being used is the `.assertEqual(), assertRaises(), assertTrue() and assertFalse()`.

`assertEqual()`: checks if the output is equal to the expected input

`assertRaises()`: notifies the test runner about a specific error that would occur when being run. e.g
`with self.assertRaises(ZeroDivisionError):`
    `result = 10 / 0`

`assertTrue() and assertFalse()`: this just checks for a condition and in most cases True is always True and False is always False

`setUp(self) and tearDown(self)`: allows you to define instructions that would be used before and after each test method

### Methods for skipping and Expection Errors

You can also skip test as well as inform the test runner about errors to expect using special decorators.

`@unittest.skip(add reason here)`: this makes the test runner to skip this specific test and gives a report that a test is skipped

`@unittest.expectFailure`: tells the test runner that it should expect and error but when it doesnt see any error an error or failed would be raised by the test runner that no error was found

`.subTest()` can also be used when working with loops and it helps to complete the entire loop incase an error is found. it also reports all places where errors are found without stopping the loop.
