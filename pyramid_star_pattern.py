#!usr/bin/python

#Asking the user to enter the number of rows for star pattern print
no_of_rows  =   int(raw_input("\nEnter the number of rows for the star pattern\n"))
row_count = 1
max_star_count = 1

#To calculate the maximum number of stars that will appear in the last row
i = row_count
while(i <= no_of_rows):
    max_star_count = max_star_count + 2
    i = i + 1

#To calculate the spaces needed for each row starting from maximum.
space_count = (max_star_count*2-2)/2
print "\nThe pattern is:\n"

#While the total number of rows are met for printing the respective star pattern
while (row_count <= no_of_rows):
    current_space_count = space_count
    #Reset Star count to 1 after finishing every row
    star_count = 1
    while (current_space_count > 0):
        #Print spaces per row
        print "",
        current_space_count = current_space_count - 1
    #Decrement spaces, as we proceed to next row
    space_count = space_count - 2
    #Print the number of stars based on row count in the patterns of 1, 3, 5, 7,..
    while (star_count <= 2*(row_count-1)+1):
        #Print the stars per row
        print "*",
        star_count = star_count + 1
    print "\n"
    row_count = row_count + 1