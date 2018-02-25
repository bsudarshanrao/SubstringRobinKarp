def createHash(str, length):

    # calculate the string value
    stringLen = len(str)

    # initialize hash value
    hashvalue = 0

    # initialize hash table
    hashTable = {}

    # calculate p**len-1 = 256*len-1
    maxPower = 256 ** (length-1)

    # loop to calculate the hash
    for index in range(stringLen):
        if index < length:
            hashvalue = hashvalue * 256 + ord(str[length-index-1])
        else:
            hashTable[hashvalue] = index - length
            hashvalue = hashvalue - ord(str[index - length])
            hashvalue = hashvalue // 256
            hashvalue = hashvalue + ord(str[index])*maxPower

    hashTable[hashvalue] = index - length + 1
    return hashTable

def compareString(hashTable, string, length):

    # initialize found to false
    found = False

    # calculate the string value
    stringLen = len(string)

    # initialize hash value
    hashvalue = 0

    # calculate p**len-1 = 256*len-1
    maxPower = 256 ** (length - 1)

    # loop to calculate the hash
    for index in range(stringLen):
        if index < length:
            hashvalue = hashvalue * 256 + ord(string[length-index-1])
        else:
            if hashvalue in hashTable:
                found = True
                break
            else:
                hashvalue = hashvalue - ord(string[index - length])
                hashvalue = hashvalue // 256
                hashvalue = hashvalue + ord(string[index])*maxPower

    if index+1 is stringLen and hashvalue in hashTable:
            found = True

    if found:
        return found, hashTable[hashvalue], index-length+1
    else:
        return found, 0, 0

def main():

    # open input files and read the strings
    firstStrFd = open("firstString.txt", 'r')
    secondStrFd = open("secondString.txt", 'r')

    firstString = firstStrFd.read()
    secondString = secondStrFd.read()

    # close file descriptors
    firstStrFd.close()
    secondStrFd.close()

    # find the largest of the strings
    if len(firstString) > len(secondString):
        largeStr = firstString
        smallStr = secondString
        largeStrLen = len(firstString)
        smallStrLen = len(secondString)
    else:
        largeStr = secondString
        smallStr = firstString
        largeStrLen = len(secondString)
        smallStrLen = len(firstString)

    # binary search for length in the second substring
    max = smallStrLen
    min = 0
    found = False
    # do until you find the max substring length
    while max >= min:

        # initialize hashmap
        hashMap = {}

        # calculate mid
        mid = int((max + min) / 2)

        # quit if mid becomes zero
        if mid is 0:
            break

        # create a hash for all strings of length mid for large string
        hashMap = createHash(largeStr, mid)

        # Now check if a string of this length is found in the hash map
        value = compareString(hashMap, smallStr, mid)

        if value[0] is True:
            min = mid + 1
            largeStrIndex = value[1]
            smallStrndex = value[2]
            strlength = mid
            #print(largeStrIndex, smallStrndex, mid)
            found = True
        else:
            max = mid - 1

    if found is True:
        print("Length of the largest substring is = ", strlength)
        #print(largeStr[largeStrIndex:largeStrIndex+strlength])
    else:
        print("Not found")
main()
