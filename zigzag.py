

# class Solution(object):
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # if there is only one row no change is needed
    if numRows <= 1:
        print(s)
        return s

    # create an array of strings with a string in each row
    outputRows = []
    rows = range(numRows)
    for r in rows:
        outputRows.append("")
    
    # loop through word and insert letters into the new array
    # count = 0 NOT SURE THIS IS NEEDED
    currRow = 0
    ascending = True
    spacing = ""
    count = 1
    for letter in s:
        rowContent = outputRows[currRow]
        outputRows[currRow] = rowContent + spacing + letter
        # update the current row
        if ascending and currRow < numRows - 1:
            currRow += 1
            if count > numRows:
                spacing = spacing + "  "
        elif ascending and currRow == numRows - 1:
            ascending = False
            currRow -= 1
            spacing = " "
        elif not ascending and currRow > 0:
            currRow -= 1
            spacing = spacing + "  "
        else:
            ascending = True
            currRow += 1
            spacing = " "
        count += 1
    #print output and create the returned value of the reordered string
    zigString = ""
    for line in outputRows:
        print(line)    
        zigString = zigString + line.replace(" ", "")
    return zigString


test = 'BMTRNDEWS'
rows = 4
converted = convert(test, rows)
print(converted)

# this is not a very good solution. It is not good with memory distributon or time :(