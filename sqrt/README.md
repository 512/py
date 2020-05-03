

Explanation
===========


### A. Find the square root of 5 (input=5)

```
 ___
√ 5  <--- n
```

### B. group the input into pairs of digits

adding decimal point and zeros as needed

```
 ____
√ 05 .  <--- pairs = ['0','5','.']

```

### C. first iteration

current = 5 (i.e. 05)
pairs = ['.']

first digit is the largest x such that x*x < 5

```
   2 <--- digit (answer_so_far)
 ________
√ 05 . 
-  4   <---- result
----    
   1   <--- remainder = 5 - 4 = 1

```

### D. handle the decimal point 

head of pairs is now at decimal point, so the next
character in the answer is the decimal point 

```
   2. <---- answer_so_far
 ________
√ 05 . 
-  4  
----    
   1 
```

### E. pairs is now empty, which implies endless pairs of 00

current_from_next_pair(pairs=[], remainder=1) ==>

```
   2. 
 ________
√ 05 . 00         
-  4    |        (each step, bring down the next two from pairs
----    v        (or 00 once pairs is empty)
   1   00     <-- current

current = 1 * 100 + 00 = 100
partial_root = 2 (ignoring decimal point)
```

### F. next iteration

find_next_digit(100, 2) ==>

```
p = 2
c = 100
let y = (20p + x) * x

find greatest value of x such that y <= c

x = 2

result = 84 (42 * 2)

   2.   2 
 ___________
√ 05 . 00 00      (00 is implied once base is empty) 
-  4    |
----    v
   1   00  
 -     84
   ------
       16 <--- remainder       
```
partial_root is now 22

### G. another iteration

next_digit(current=1600, partial=22) ==>

```
p = 22
c = 1600
let y = (20p + x) * x

find greatest value of x such that y <= c

x = 3

result = 1329 (443 * 3)

   2.   2  3
 ___________
√ 05 . 00 00      
-  4    |
----    v
   1   00  
 -     84
   ------
       16 00
    -  13 29
    --------
        2 71  <--- remainder
```
partial_root: 223

### H. another iteration

next_digit(current=27100, partial=223) ==>

```
p = 223
c = 27100
let y = (20p + x) * x

find greatest value of x such that y <= c

x = 6

result = 26,796 (4466 * 6)


   2.   2  3  6
 ______________
√ 05 . 00 00 00     
-  4    
----    
   1   00  
 -     84
   ------
       16 00
    -  13 29
    --------
        2 71 00
     -  2 67 96
        -------
           3 04 <-- remainder
```
partial: 2236

### I. repeat iterations ad infinitum ...

```
2.236067977499789696409173668731276235440618359611525724270897245410520925637804
89941441440837878227496950817615077378350425326772444707386358636012153345270886
67781731918791658112766453226398565805357613504175337850034233924140644420864325
39097252592627228876299517402440681611775908909498492371390729728898482 ...
```