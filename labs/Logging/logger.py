# import your libraries here.
from datetime import datetime


# the name of the log file to write to.
log_file = str("log-file-"+ datetime.today().strftime('%Y-%m-%d') + ".log")




def log(text, log_file=log_file):
    # open up the log file in the correct mode.
    f = open(log_file,"w")
    # create a string that has the current date and time in the beginning of the text.
    f.write(datetime.today().strftime('%Y-%m-%d') + text)
    # Ensure the string ends with a new line character.
    # append the text to the end of the file.
    f.close # close the file.
    return None


def dump(log_file=log_file):
    '''
    This function prints out each line in the log file to the console
    '''
    f = open(log_file, "r")
    # open up the log file in the correct mode.
    file_list = []
    # read the file into a list.
    data = log_file.read(file_list=log_file)
    # iterate through each item in the list and print out the results.
    print(data)
    return None