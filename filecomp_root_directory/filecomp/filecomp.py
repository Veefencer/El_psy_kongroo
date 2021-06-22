import os
import re


def fcomp(yourpath):

    """
    Docs:
     Function receives the path and analyzes the directory it represents
     in order to find the files/directories of maximum and minimum sizes that the initial folder contains.
     Then returns a dictionary with tuples containing path to those objects as values.
     Keys used are: 'maxs' for maximum sized objects, 'mins' for minimal sized ones and 'eq' if all have equal sizes.
     Usage of backslash in paths should be avoided due to it causing the function to fail (SyntaxError).
     Either double backslash or slash should be used instead. Alternatively, the path can be
     initially inputted as raw
     """

    contents = os.listdir(yourpath)
    quantity = len(contents)
    if quantity != 0:
        sizelist = []                                  # Creating a list with sizes of path contents in bytes
        for k in range(quantity):
            currentpath = os.path.join(yourpath, contents[k])
            if os.path.isfile(currentpath):
                sizelist += (os.path.getsize(currentpath),)
            else:
                sizesum = 0
                for path, dirs, files in os.walk(currentpath):
                    for file in files:
                        sizesum += os.path.getsize(os.path.join(path, file))
                sizelist.append(sizesum)
        maxs = max(sizelist)
        mins = min(sizelist)
        sizelist = list(enumerate(sizelist))           # Finding all indexes(keys) of minimal and maximal sized contents
        maxlist = [i for i, j in sizelist if j == maxs]
        minlist = [i for i, j in sizelist if j == mins]
        slash = re.compile('\\\\')                     # Preparing the returned values
        largest = [slash.sub('/', str(os.path.join(yourpath, contents[i]))) for i in maxlist]
        if maxlist == minlist:
            returned = {'eq': largest}
        else:
            smallest = [slash.sub('/', str(os.path.join(yourpath, contents[i]))) for i in minlist]
            returned = {'maxs': largest, 'mins': smallest}
        return returned
    elif quantity == 0:
        return
