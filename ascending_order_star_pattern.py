#!usr/bin/python

#Asking the user to enter the number of rows for star pattern print
no_of_rows  =   int(raw_input("\nEnter the number of rows for the star pattern\n"))
row_count = 1
print "The pattern is:\n"

#While the total number of rows are met for printing the respective star pattern
while (row_count <= no_of_rows):
    '''Number of stars based on the row number, for example, for row 5 there will be 5 stars
    Reset the number of stars to be printed to 1 for the new row after finishing the current row''' 
    no_of_stars = 1
    while (no_of_stars <= row_count):
        print "*",
        no_of_stars = no_of_stars + 1
    print "\n"
    row_count = row_count + 1