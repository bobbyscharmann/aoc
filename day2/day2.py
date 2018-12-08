#!/bin/python
"""
December 7, 2018

    Day 2  of Advent of Code Challenge (www.adventofcode.com)
Scharmann
"""

# File containing inputs
INPUT_FILE = "input"
print "Welcome to day two of Advent of Code"


# Read in the input frequencies
f = open(INPUT_FILE, 'r')

num_twos = 0
num_threes = 0

# Temporary placeholder for the characters and counts
tmp = {}
lines = []
# For each line in the file
for line in f:
    lines.append(line[:-1])
    # For each character
    for char in line:
        # Add it to our dict - either increment or set it.
        if char in tmp.keys():
            tmp[char] = tmp[char] + 1
        else:
            tmp[char] = 1

    # Look for twos and threes. Would be easy to genericize this
    if 2 in tmp.values():
        num_twos += 1
    if 3 in tmp.values():
        num_threes += 1
    
    # Initialize the data structure for the next line
    tmp = {}    

# Close the file handle
f.close()

# Keep up with the index that is different when we find a match
idx_that_different = 0

# For each line
for line in lines:
    # Loop over the other lines
    for next_line in lines:
        # Don't process the same ine on each loop or it will be a match :)
        if line == next_line:
            continue
        
        # Keep track of the number of differences between the strings
        num_diffs = 0
        
        # Loop over each string comparing characters
        for idx, char in enumerate(line):
            # Keep track of the number of differences
            if char != next_line[idx]:
                num_diffs += 1
                idx_thats_different = idx # Save off index
            
            # If we saw more than one difference, carry on
            if num_diffs > 1:
                continue
        
        # One or fewer differences indicates we found it
        if num_diffs <= 1:
            print "Found it: {} and {} with {}".format(line, next_line, \
                  line[:idx_thats_different] + line[idx_thats_different+1:])


# Print the results
print "Number of twos: {}".format(num_twos)
print "Number of threes: {}".format(num_threes)
print "Checksum is: {}".format(num_twos * num_threes)
print "Exercise Complete"
