# Preparing for Hacker Test from https://coderbyte.com/

# Task 1
'''
Letter Changes
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
Examples
Input: "hello*3"
Output: Ifmmp*3
Input: "fun times!"
Output: gvO Ujnft!
'''
# Solution of task 1

def LetterChanges(txt):
  new_str = ""
  for i in range(0, len(txt)):
    if(txt[i] == 'z' or txt[i] == 'Z' or not txt[i].isalpha()):
      new_str += txt[i]
    else:
      new_str += chr( ord(txt[i]) + 1 )
  return new_str

# keep this function call here 
print(LetterChanges(input()))

# Test 1
'''
"Argument goes here z"
Bshvnfou hpft ifsf z
'''

'''
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

A : [1 3 5] 
k : 4

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''

def diffPossible(self, A, B):
	    for i in reversed(range(len(A) )):
	        for j in range (0, i):
	            if (A[i] - A[j] == B):
	                return 1
        return 0
