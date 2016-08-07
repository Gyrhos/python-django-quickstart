#!/usr/bin/env python3


def tuple_samples():
    '''
        they are inmutable (they cannot be changed).
        Strings are like tuples of chars.

    '''
    ttuple = (0, 1, 2, 3, 4, 5,)

    print ("tuple examples")
    # the line below would fail bacause cannot convert tuples to strings
    # implicitly
    # print("print the entire tuple: " + ttuple)
    # This instead works ok
    # print("print the entire tuple: ", ttuple)

    # You see, arguments are in a tuple theirselfs
    print("print the entire tuple: %s" % (ttuple,))
    # This tells to print from 0 to index 1
    print("first 2 elements: %s " % (ttuple[:2], ))
    # this tells to print from index 1 to the end
    print("prints from 1 element in advance: %s " % (ttuple[1:],))
    # this tells to print from index 1 to the end
    print("print indexes 1, 2 elements: ", (ttuple[1:3],))
    print("print last element  with -1: ", (ttuple[-1],))


def list_samples():
    '''
        The treatment is like tuples but you can also
        add, remove, insert etc...
        functions on lists:

        cmp(list1, list2)
        Compares elements of both lists.

        len(list)
        Gives the total length of the list.

        max(list)
        Returns item from the list with max value.

        min(list)
        Returns item from the list with min value.

        list(seq)
        Converts a tuple into list.

        list.append(obj)
        Appends object obj to list

        list.count(obj)
        Returns count of how many times obj occurs in list

        list.extend(seq)
        Appends the contents of seq to list

        list.index(obj)
        Returns the lowest index in list that obj appears

        list.insert(index, obj)
        Inserts object obj into list at offset index

        list.pop(obj=list[-1])
        Removes and returns last object or obj from list

        list.remove(obj)
        Removes object obj from list

        list.reverse()
        Reverses objects of list in place

        list.sort([func])
        Sorts objects of list, use compare func if given
    '''
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]

    print ("list examples")
    # the line below would fail bacause cannot convert tuples to strings
    # the line below would fail bacause cannot convert tuples to strings
    # implicitly
    # print("print the entire tuple: " + ttuple)

    # You see, arguments are in a tuple theirselfs
    print("print the list1: ", list1)
    print("print the list2: ", list2)
    print("print the list3: ", list3)
    list3[1] = "not b"
    print("print the list3: ", list3)
    del list3[2]
    print("print the list3: ", list3)

    hi = ["HI!"]
    print ("hi * 4: ", hi*4)
    print ("is 'a' in list3?: ", "a" in list3)
    print ("iterate the list, tuple, dictionary:")
    for i in list3:
        print("\t", i)


def dictionary_samples():
    '''
        Dictionaries are more or less like lists by the can be access through
        a different index, that index can be a string, an integer or an object.

        No duplicate keys
        Key must be an inmutable object (no lists, no other dicts...)

        cmp(dict1, dict2)
        Compares elements of both dict.

        len(dict)
        Gives the total length of the dictionary. This would be equal to the
        number of items in the dictionary.

        str(dict)
        Produces a printable string representation of a dictionary

        type(variable)
        Returns the type of the passed variable. If passed variable is
        dictionary, then it would return a dictionary type.

        dict.clear()
        Removes all elements of dictionary dict

        dict.copy()
        Returns a shallow copy of dictionary dict

        dict.fromkeys()
        Create a new dictionary with keys from seq and values set to value.

        dict.get(key, default=None)
        For key key, returns value or default if key not in dictionary

        dict.has_key(key)
        Returns true if key in dictionary dict, false otherwise

        dict.items()
        Returns a list of dict's (key, value) tuple pairs

        dict.keys()
        Returns list of dictionary dict's keys

        dict.setdefault(key, default=None)
        Similar to get(), but will set dict[key]=default if key is not already
        in dict

        dict.update(dict2)
        Adds dictionary dict2's key-values pairs to dict

        dict.values()
        Returns list of dictionary dict's values
    '''
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print ("dictionary examples")
    print ("dict['Name']: ", dict['Name'])
    print ("dict['Age']: ", dict['Age'])

    del dict['Class']
    print ("delete an element: ", dict)

    dict['Class'] = 'Added after being removed'
    print ("add an element: ", dict)


if __name__ == "__main__":
    tuple_samples()
    print ("\n")
    list_samples()
    print ("\n")
    dictionary_samples()
