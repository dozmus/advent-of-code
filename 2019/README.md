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
* If statements (less than, or equals comparisons)

TODO:
* Minus
* While
* For
* Greater than
* Not equals

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
z = -1
print(z)
print(-1)

a = 1

if a < 2 then
    print(1)
endif

if a == a then
    print(1)
endif

if not a < 0 then
    print(1)
endif

if 2 < 1 then
    print(0)
endif
```
