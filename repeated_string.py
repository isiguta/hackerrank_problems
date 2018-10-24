# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.
# For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.
# Function Description
# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider
# Input Format
# The first line contains a single string, s.
# The second line contains an integer, n.
# Output Format
# Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating infinitely many times.
# Sample Input 0
# aba
# 10
# Sample Output 0
# 7
# Explanation 0
# The first n=10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we print 7 on a new line.


def repeated_string(s, n):

    # calculate how many 'whole' repeating cycles we have
    # and how many characters we would need to append at the end of the resulting string
    cycles = divmod(n, len(s))

    return s.count('a') * cycles[0] + s[:cycles[1]].count('a')
