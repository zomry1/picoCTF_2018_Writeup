
# *script me*

## Information
| Points |Category  | Level|
|--|--|--|
| 500 | General Skills |Hard |

## Challenge

> Can you understand the language and answer the questions to retrieve the flag? Connect to the service with `nc 2018shell.picoctf.com 7866`

### Hint
>  Maybe try writing a python script?
## Solution
So after connecting to the service this massage showed up:

    Rules:
    () + () = ()()                                      => [combine]
    ((())) + () = ((())())                              => [absorb-right]
    () + ((())) = (()(()))                              => [absorb-left]
    (())(()) + () = (())(()())                          => [combined-absorb-right]
    () + (())(()) = (()())(())                          => [combined-absorb-left]
    (())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
    ((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
    () + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]
    
    Example: 
    (()) + () = () + (()) = (()())
    
    Let's start with a warmup.
    (()) + (()()()) = ???

So there is a 8 rules and it's like a math problem, so for understanding the rules.  
I just tried to answer some questions and if I got wrong, the right answer   showed up to show me where I was wrong.  
After some tries I thought I understood the rules and here they are:  
 >1. **Combine** - the max depth of each part are equal => combine them    
 >*example:*  ()()()(()) + (())() = ()()()(())(())()    
 >  
>||part1|part2  |answer |
>|--|:--:|:--:|:--:|
>|value| ()()()(()) | (())() | ()()()(())(())()|
>|max depth| 2| 2| 2|

>2. **Absorb left** (and right) - if the max depth of the left part is more than   >the max left of the right part => put the right part right before closing the left   >part  
 >*example:*  (()) + () = (()())  
 >  
>||part1|part2  |answer |
>|--|:--:|:--:|:--:|
>|value| (()) |  () | (()())|
>|max depth| 2| 1| 2|  
>* the absorb right it's symmetric  

>3. **Left associative** - start from the 2 left parts, do the + between them and take >the result + the third part  
>*example:* () + (()) + ((())) = ((()())(()))  
 >
>||part1|part2  |part3 |part1+part2 |result+part3 |
>|--|:--:|:--:|:--:|:--:|:--:|
>|value| () | (())|  ((())) | (()())|((()())(())) |  
>|max depth| 1| 2| 3| 2| 3|  

So I wrote this python script:  
```python
import re

#Count the max depth of a str.
#Each '(' add one, each ')' sub one.
def depth (str):
	max = 0
	curr = 0
	for c in str:
		if c == '(':
			curr+= 1
			if curr > max:
				max = curr
		if c == ')':
			curr-= 1
	return max

#AbsorbLeft (when the left part depth is more than the right part.
#Set all the left part without the closing ')' at the end, insert right part and close by ')'
def absorbLeft(left,right):
	return left[:-1]+right+left[-1]

#Symmertic to the absorbLeft
def absorbRight(left,right):
	return right[0] + left + right[1:]


def splitProblem(question):
	#Split by "?" and "=" and "+"
	question = re.split('[= + ?]', question)
	#Remove empty strings from the list
	return filter(None, question)	


def solveProblem(question):
	#Split the question to parts.
	parts = splitProblem(question)
	print "answer:"
	result = parts[0]
	for i in range(1,len(parts)):
		#The depth is equal for both, just add after the first part
		if(depth(result) == depth(parts[i])):
			result += parts[i]
			continue
		#Left part depth is less than the right part depth - 
		#Absorb right
		if(depth(result) < depth(parts[i])):
			result = absorbRight(result,parts[i])
			continue
		#else, left part depth is more than the right part depth - 
		#Absorb left
		result = absorbLeft(result,parts[i])
	return result

if __name__ == "__main__":
	text = raw_input("Enter question: ")
	while(text != "exit"):
		print solveProblem(text)
		text = raw_input("Enter question: ")
```
*Comments speaks for themselves  
  
So I print each question I got from the shell to the script, got the answer and   print it back in the shell,and after 5 questions I got the key.
## Flag
> `picoCTF{5cr1pt1nG_l1k3_4_pRo_45ca3f85}`


