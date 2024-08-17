# local search using Genetic & Simulated Annealing<br/>
&emsp; This was Ai assignment to perform local search on the problem with **Genetic** and **Simulated Annealing** (**SE** in code).<br/>
<br/>
## Question:<br/>
&emsp; In this question we have to open(crack) a door's lock, or break lock code in other word. This lock behaves like this. Imagine every key is a number that contains 100 bits. This lock contains many OR gates in which every OR gate 
gets three of inputs bit as its input. These inputs are one of the numbers bit itself or the bit after it passes a not gate. For example one of these OR gates can have this (X20, X31, ~X45) which means we have an OR gate that takes 20th 
bit, 31st bit and the reverse of 45th bit as an input and then returns the result.<br/>
As we mentioned we have many of these OR gates that bahave as mentioned. Then after each OR gate returns the answer, we perform an AND gate on these OR gates result. Then this AND gate returns True or False(zero or one). If the and gates
result is True (or one), it means that we have opened (cracked) the lock, otherwise we have failed on openning (cracking) the lock.<br/>
<br/>
## input structure:<br>
&emsp; WE have a database.cnf file that each line on this file contains three numbers (positive or negative) which beside their sign, absolute value that number a number, shows a bit index that we had in the key(key is a number with 100 bit). 
Indexes start from one to 100. Each line represent an OR gate and three given numbers in each line, represent the a bit index in the key. If they are positive, it means we have that bit as one gate's input, and if it is negative, 
it means we have to reverse that bit first (pass it through NOT gate) and then pass it to our OR gate. and after these three numbers, we have a zero to specify the end of a line.<br/>
<br/>
## solution:<br/>
&emsp; We solved this by using two different algorithm for local search, **Genetic** and **Simulated Annealing (SE)**. The current main.py code, solve it using Genetic algorithm and if we want to solve it with SE algorithm, we just need to 
uncomment these code these lines:<br/> 
`#se = SE(get_input())`<br/>
`#se.run()`<br/>
and commenting These lines:<br/>
`genetic = Genetic(get_input())`<br/>
`genetic.run()`
