# Philip Brady
# This is the Weekly Task 7.
# The program takes in the name of a file and returns
# the total number of e's contained within the file text.

filename = input("Enter the file name: ")
# Initialised the e counter.
ecount = 0

# Opened the inputed file in the read format.
with open (filename, 'r') as f:
    # This loop goes through each line in the file.
    for line in f:
        # The split function is used to create a list
        # of words for each line.
        words = line.split()
        # This nested loop goes through each word of the
        # words list.
        for word in words:
            # This nested loop goes through each letter
            # of the word.
            for letter in word:
                # If the letter is an 'e' then the e
                # counter is increased by 1.
                if letter == "e":
                    ecount += 1

print("The total number of e's in the file '{}' is {}."
.format(filename, ecount))

# I got the idea for this code from
# https://www.sanfoundry.com/python-program-read-file-counts-number/
# I also studied the split function further in
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str