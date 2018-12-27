import io
def compress(text):
    """
    compress() takes a string and compresses it using the LZW algorithm.
    Returns the compressed string in the form of a list of integers.
    @params: string to be compressed.
    @return: compressed string (list of ints).
    """
    if text == '':
        return []
    elif type(text) != str:
        # printError(2)
        pass

    # Creates a list that will hold the integers after compression of the
    # string.
    compressed_lst = []

    # Makes the dictionary to hold our values we map to.
    table = {}
    for i in range(256):
        table[chr(i)] = i
    value = ''
    index = 0
    # Loop over each individual character in the text and keep track of where
    # in the string you are (using the value index). Value keeps track of the
    # longest substring you have seen that is in your table.
    for char in text:
        # Add the latest character to our substring.
        total = value + char
        index += 1
        # If we have seen total before we want to make it our value (aka we
        # want to remember it) and move on to the next character. However,
        # we also need to check if we have reached the end of the string. If
        # we have reached the end, we add the total to our compressed list.
        if total in table:
            value = total

        # However, if we have not seen total before, we add value (the
        # substring we had remembered) to the ditionary and we add total
        # to the dictionary (because we have not seen it before). We then
        # move on to remembering the most recent character.
        else:
            compressed_lst.append(table[value])
            table[total] = len(table)
            value = char

        if index == len(text):
            compressed_lst.append(table[value])
        # print(total) # For testing purposes.

    compressed_str = ''
    for num in compressed_lst:
        # print num
        # print str(num)
        compressed_str += ' ' + str(num)
        # print compressed_str

    return compressed_str.strip()

def decompress(compressed_lst):
    """
....decompress() takes a list of integers and decompresses it using the LZW
....algorithm. Returns the decompressed string.
....@params: compressed string (list of ints).
....@return: decompressed string.
...."""
    #convert str to list
    # compressed_lst = list(map(int,compressed_lst.split()))

    if compressed_lst == []:
        return ''
    elif type(compressed_lst) != list:
        printError(1)

    # We start by reconstructing the dictionary we used to compress the
    # string. However, now the keys are the integers and the values are the
    # strings.

    table = {}
    for i in range(256):
        table[i] = chr(i)

    prev = str(chr(compressed_lst[0]))
    compressed_lst = compressed_lst[1:]
    decompressed_str = prev

    # Loops over element in the compressed list so that we can decompress it.
    # If an element does not exist in our table it must be premature and
    # hence, the list we were given is invalid --> error.
    # If an element is in the list we retrieve it and add it to our solution.
    # And then make sure to add a new value to our table, which is the
    # previous element plus the first letter of the current string.

    for element in compressed_lst:
        if element == len(table):

            # print prev # For testing purposes.

            string = prev + prev
        elif element not in table:
            printError(1)
        else:
            string = table[element]

        decompressed_str += string

        # Constructs new values to add to our table by taking the previous
        # string and adding the first letter of the current string to it.

        table[len(table)] = prev + string[0]

        prev = string

    return decompressed_str

def compress1(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size

            dict_size += 1
            w = c

    #Output the new Dictionary.
    # newDictionary = list(dictionary.items())
    # print("****New Dictionary****")
    # print(" ITEM  INDEX ")
    # for d in newDictionary[256:]:
    #     print(d,"\n")

    #Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def decompress1(compressed):
    """Decompress a list of output ks to a string."""


    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop

    result = io.StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

if __name__ == '__main__':
    a = compress('Nguyen Minh Dung')
    b = compress1('Nguyen Minh Dung')
    print(b)
    print(decompress1(b))
