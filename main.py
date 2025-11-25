def reversearrayinplace(arr):
    startindex = 0
    endindex = len(arr) - 1

    while startindex < endindex:
        arr[startindex], arr[endindex] = arr[endindex], arr[startindex]
        startindex += 1
        endindex -= 1
originalarray = [6, 5, 4, 3, 2, 1]
print("Originalarray:",originalarray)

reversearrayinplace(originalarray)
print("Reversedarray: ",originalarray)
