You will find here a compiler for the IntCode VM that we build throughout this event.  
Beware, it is space-sensitive!

Use:
```
python intcode_compiler.py code.txt
python intcode_vm.py code.ic
```

Features:
* Plus, Multiply
* Input
* Print
* Assign

Example code:
```
x = 2 + 4
print(x)
x = 2 * 4
print(x)
z = input()
print(z)
z = z * x
print(z)
z = 1
print(z)
z = x
print(z)
```

