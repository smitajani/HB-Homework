
""" Open file 'um-server-01.txt' and print the lines with Sales 
    information for Tuesday."""




log_file = open("um-server-01.txt")     # Open file 'um-server-01.txt'

### Question: What is log_file - file 'handle' for the open file?

def sales_reports(log_file):            # Accept file handle(?) as argument
    for line in log_file:               # Loop through each line on the file 
        line = line.rstrip()            # Strip spaces to the right 
        day = line[0:3]                 # Get the day by extracting the first 
                                        #   three characters of the string
        if day == "Tue":                # If it equals Tue, then print the line 
            print(line)


sales_reports(log_file)
