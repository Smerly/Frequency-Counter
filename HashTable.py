from LinkedList import LinkedList


class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):
        arr = []

        for i in range(size):
            arr.append(LinkedList())
        return arr

    # 2️⃣ TODO: Create your own hash function.

    # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored.

    def hash_func(self, key):

        # This orders the items from lowest amount of vowels to most amount of vowels
        a_count = key.count('a')
        e_count = key.count('e')
        i_count = key.count('i')
        o_count = key.count('o')
        u_count = key.count('u')

        vowel_count = a_count + e_count + i_count + \
            o_count + u_count

        index = vowel_count % self.size
        return index

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):

        new_data = (key, value)

        arr_index = self.hash_func(key)

        ll = self.arr[arr_index]

        # If not found, append
        if ll.find(key) == -1:
            print(f"{key} was not found")
            ll.append(new_data)

        else:
            # ll.put(key, value)
            self.arr[arr_index].put(key)


# See LinkedList.py, print_nodes()

    def print_key_values(self):
        for ll in self.arr:
            ll.print_nodes()
        #
        # else:

            # 4️⃣ TODO: Complete the print_key_values method.

            # Traverse through the every Linked List in the table and print the key value pairs.

            # For example:
            # a: 1
            # again: 1
            # and: 1
            # blooms: 1
            # erase: 2

            # Go to LinkedList at print_nodes function and fix

    # TODO:

    # fix stuff on linkedlist.py in print_nodes
    # change hash_func to something different
    # fix update method in linkedlist.py
