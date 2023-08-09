#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countNumbers function below.
def countNumbers(arr):
    dynamic = []

    for x in arr:
        # print(arr)
        start = int(x[0])
        end = int(x[1])
        if len(dynamic) * 10 <= end:

            for fill in range(len(dynamic) * 10, end + 1, 10):
                valid = 0
                invalid = 0
                list = []
                for i in range(10):
                    if len(str(fill + i)) == len(set(str(fill + i))):
                        list.append(fill + i)
                        valid += 1
                    else:
                        list.append("X")
                        invalid += 1
                list.append(valid)
                list.append(invalid)
                dynamic.append(list)
        valid = 0
        if start % 10 == 0 and end % 10 == 9:
            valid += get_valid_count(start, end, dynamic)
        else:
            if end - start < 10:
                for i in range(end - start + 1):
                    if len(str(start + i)) == len(set(str(start + i))):
                        valid += 1
            else:
                startfrom = 0
                endat = end - (end % 10) - 1
                for i in range(start, start + 10):
                    if len(str(i)) == len(set(str(i))):
                        valid += 1
                    if i == end:
                        break
                    if i % 10 == 9:
                        startfrom = i + 1
                        break  # end it as it is the last number of the row
                for i in range(end - (end % 10), end + 1):
                    if i <= start:
                        break
                    if len(str(i)) == len(set(str(i))):
                        valid += 1

                valid += get_valid_count(startfrom, endat, dynamic)
        print(valid)


def get_valid_count(start, end, dynamic):
    valid = 0
    startindex = int(start / 10)
    endindex = int(end / 10)

    for i in range(startindex, endindex + 1):
        valid += dynamic[i][10]
    return valid


if __name__ == "__main__":

    dict = {"123":5,"456":6,}
    NumOfList = int(input("Enter the number of lists: "))
    ListOfInput =[]
    for i in range(NumOfList):
        start = input("Enter the start number: ")
        end = input("Enter the end number: ")
        list = [start,end]
        ListOfInput.append(list)

    countNumbers(ListOfInput)

