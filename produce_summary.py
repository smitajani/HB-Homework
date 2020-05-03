
""" Open raw data files the and print to the sales report 
"""

# Iteration-1: Fix the report to print correct values - melon, count & amount, 
# on each line

# Iteration:2: Code cleanup and optimization

# Open the file object passed as the argument, loop through each row and do the
# following:
# - Strip spaces on the right
# - Split the values separated by '|' into a list
# - Print the values in a readable format on the report

def print_report(the_file, day_num):
    print(f"Day {day_num}: {the_file.name}")

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    print(f"---- (EOF) End of file #{day_num}----\n\n")
    the_file.close()


# Assign file names to a list and loop through. This replaces the code block 
# below that called the function for each individual file 
# ----------------------------------------------------------

list_of_files = []
list_of_files = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]

for index, current_file in enumerate(list_of_files):
    current_file = open(current_file)
    print_report(current_file, index)


# current_file = open("um-deliveries-20140519.txt")
# print_report(current_file, 1)


# current_file = open("um-deliveries-20140520.txt")
# print_report(current_file, 2)


# current_file = open("um-deliveries-20140521.txt")
# print_report(current_file, 3)
