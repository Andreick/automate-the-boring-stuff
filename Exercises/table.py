#! python 3
#table.py - Module with printTable function.

import sys

def printTable(list_of_lists):
    """Takes a list of lists of strings and displays it in a well-organized
    table with each column right-justified."""

    numRows = len(list_of_lists) #Matrix rows.
    numColumns = len(list_of_lists[0]) #Matrix columns.

    for i in range(numRows):
        if len(list_of_lists[i]) != numColumns:
            sys.exit('The inner lists must contain the same number of strings.')

    colWidths = [0] * numRows #Table columns widhts.

    for i in range(numRows):
        for string in list_of_lists[i]:
            #Loop through all strings in the row.

            if len(string) > colWidths[i]:
                colWidths[i] = len(string)
            #Stores the maximum width of each column.

    for j in range(numColumns):
        for i in range(numRows):
            print(list_of_lists[i][j].rjust(colWidths[i]), end = ' ')
        print()
