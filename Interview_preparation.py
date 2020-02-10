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
##############################################################

# Task 2
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

##############################################################

# Task 3

'''
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output: 1

'''


def solve(A, B, C):
        min_diff = abs(max(A[0], B[0], C[0]) - min(A[0], B[0], C[0]))
        for a in A:
            for b in B:
                for c in C:
                    if abs(max(a, b, c) - min(a, b, c)) < min_diff:
                        min_diff = abs(max(a, b, c) - min(a, b, c))
                    if min_diff == 0: return 0
        return min_diff
