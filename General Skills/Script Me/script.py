#!/usr/bin/python
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
		
