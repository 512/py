

Explanation
===========

```
A.
 ___
√ 5  <--- n


B.
 ____
√ 05 .  <--- base = ['0','5','.']


C.

current = 5
base = ['.']


   2 <--- digit (next char)
 ________
√ 05 . 
-  4   <---- result
----    
   1   <--- working = 5 - 4 = 1

D.

head of base is decimal point 

   2. <---- next char 
 ________
√ 05 . 
-  4  
----    
   1 


E.

base = []
answer = 2

   2. 
 ________
√ 05 . 00        (00 is implied once base is empty) 
-  4    |
----    v
   1   00     <-- current

next_group([], 1) ==>

base is now empty
current = 1 * 100 + 00 = 100

F. 

next_digit(100, 2) ==>

first multiplier = base * 2 * 10 + try_digit = 4?
second multiplier = try_digit = ?

next digit = largest ? such that 4? * ? < 100 (i.e. current)

which is 2

result = 84 (42 * 2)

   2.   2 
 ___________
√ 05 . 00 00      (00 is implied once base is empty) 
-  4    |
----    v
   1   00  
       84
   ------
       16 <--- working
       
answer is now 22

G. 

next_digit(current=1600, base=22) ==>

first multiplier = base * 2 * 10 + try_digit = 44?
second multiplier = try_digit = ?

next digit = largest ? such that 44? * ? < 1600 (i.e. current) 

which is 3

result = 1329 (443 * 3)

   2.   2  3
 ___________
√ 05 . 00 00      
-  4    |
----    v
   1   00  
   -   84
   ------
       16 00
    -  13 29
    --------
        2 71  <--- working
            
answer: 223


H. 

next_digit(current=27100, base=223) ==>

first multiplier = base * 2 * 10 + try_digit = 446?
second multiplier = try_digit = ?

next digit = largest ? such that 446? * ? < 27100 (i.e. current) 

which is 6

result = 26,796 (4466 * 6)

   2.   2  3  6
 ______________
√ 05 . 00 00 00     
-  4    
----    
   1   00  
   -   84
   ------
       16 00
    -  13 29
    --------
        2 71 00
     -  2 67 96
        -------
           3 04 <-- working
            
answer: 2236

And so on ...