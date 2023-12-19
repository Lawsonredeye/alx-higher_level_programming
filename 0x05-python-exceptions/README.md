# 0x05. Python - Exceptions
## > What is exception

Exceptions is the process of handling errors from a given program.
Errors detected during execution are called exceptions and are not unconditionally fatal.

The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message.

Standard exception names are built-in identifiers (not reserved keywords).

Try and except is used for handling errors which changes the normal flow of the program and the except handles errors whenever an error occured in the try block.

> Syntax
`try:
    # Some Code
except:
    # Executed if error in the
    # try block`

To know what kind of exception to use or you'll encounter, you can use the following statement with the except statement:

` except Exception as e:
	print("The error is: ",e)`

This would actually return the type of exception error that was raised based on the inputs being passed.

***Else*** statements can also be used along side of an except but it should be placed after all except statement has been written or passed.

> ***Syntax:***

```
{
try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
}
```

> Tasks:
