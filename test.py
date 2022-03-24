#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

def searchSuggestions(repository, customerQuery):
    # Write your code here
    output = []
    search = ""
    for word in customerQuery:
        search = search + word
        matching = []
        if len(search)>1:
            print(len(search))
            for words in repository: 
                    print(
                        "checking " + words
                    )
                #if words not in matching:
                    if search == words[0: len(search)]:
                        matching.append(words)
            matching.sort()
            print(matching)
            output.append(matching)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
