# Python

[back to readme](../README.md)

great wiki which covers the basics: [Simple programs](https://wiki.python.org/moin/SimplePrograms)

Nice tutorial [learn Python](http://www.tutorialspoint.com/python/index.htm)

## Basics

* Comments
```
    # one line comment
    print ('hi') # end expression comment
```
* Python takes into account indentation and it has to be always the same:
```
if x == 3:
    print(x) # this is inside if block
print(x-1) # this is outside if block
```
* wrong
```
if x == 3:
    print(x)
   print(x-1) # this is wrong because wrong indentation
```

* Print line
In python3 `print ('Hello, workd')` 

* Strings
Can use both ' and "
`'This is a string'`
`"Also this is a String"`
```
'''
    This is multi line string,
    where text can be split into lines
'''
```

* Dynamic typing
No need to declare variables, the get the type from the value we assign to them.
The scope is where you first use the variable, if it is inside a function then inside
the function it is, if it is inside a code block then it won't be accessible out of it.
```python
    if True :
        my_variable = "you won't see this out of if block"

    println (my_variable)
```

## Flow control

* if, if elif else
```python
    number = 3
    if number == 3 :
        print ("number is ", number)
    elif number == 2 :
        print ("number is %d" & number)
    else:
        print ("what the heck is number? " + number)
```

* while
```python
    count = 10
    while (count > 0):
        print ("Is the final count down: " + count)
        count = count -1
    else:
        print ("The count is over") # When the condition is not true anymore
```

* for
```python
    for i in 0..10 # 0..10 creates a range from 0 to 10... NICE!
        print ("Is the final count up: " + i)
```

