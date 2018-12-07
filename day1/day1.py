#!/bin/python
"""
December 7, 2018

    Day 1 of Advent of Code Challenge (www.adventofcode.com)
Scharmann
"""

# File containing inputs
INPUT_FILE = "input"
print "Welcome to day one of Advent of Code"

my_sum = 0
freq = []

# Read in the input frequencies
f = open(INPUT_FILE, 'r')
nums = [int(val) for val in f]   
f.close()

# Compute the simple sum for Challenge 1
my_sum = sum(nums)
        
# May need to roll over so keep up with the current index
idx = 0

# A temporary sum to use to see if we compute the same one twice
tmp_sum = 0
while True:
    # Get the current rolling frequency sum
    tmp_sum += nums[idx % len(nums)]
    
    # Have we seen it?
    if tmp_sum in freq:
        # Yes! Yah!
        print "Found frequency twice: {}".format(tmp_sum)
        break
    else:
        # Nope, log it and carry on
        freq.append(tmp_sum)
    idx += 1

# Print the results
print "Sum was: {}".format(my_sum)
print "Exercise Complete"
