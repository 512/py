

Explanation
===========

```
A. Find the square root of 5 (input=5)
 ___
√ 5  <--- n


B. "zeroize" the input
 ____
√ 05 .  <--- base = ['0','5','.']


C.

current = 5 (i.e. 05)
base = ['.']

first digit is the largest x such that x*x < 5

   2 <--- digit (next char)
 ________
√ 05 . 
-  4   <---- result
----    
   1   <--- working = 5 - 4 = 1

D.

head of base is now at decimal point, so the next
character in the answer is the decimal point 

   2. <---- next char 
 ________
√ 05 . 
-  4  
----    
   1 


E. base is now empty, which implies endless pairs of 00

next_group(base=[], working=1) ==>

current = 1 * 100 + 00 = 100

base = []
answer = 2

   2. 
 ________
√ 05 . 00         
-  4    |        (each step, bring down the next two from base
----    v        (or 00 once base is empty)
   1   00     <-- current


F. 

next_digit(100, 2) ==>

first multiplier = ans_sofar * 2 * 10 + try_digit = 4?
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

next_digit(current=1600, ans_sofar=22) ==>

first multiplier = ans_sofar * 2 * 10 + try_digit = 44?
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

next_digit(current=27100, ans_sofar=223) ==>

first multiplier = ans_sofar * 2 * 10 + try_digit = 446?
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