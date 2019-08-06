#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # Example weights = [4, 4], limit = 8
    # How to handle collisions like this with the code available to us...
    ht = HashTable(16)

    for i in range(len(weights)):
        # Insert the weight values into the hash table as keys and indexes as values
        # hash_table_insert(ht, weights[0] == 4, i = 0)
        # hash_table_insert(ht, weights[1] == 4, i = 1)
        hash_table_insert(ht, weights[i], i)
        # I believe the duplicate key is causing the issue with the [4,4] values

    print(ht.storage)

    for i in range(0, len(weights)):
        # We set value1 with the weight limit (Example value of 8) and subtract weights[i] 
        value1 = limit - weights[i] # 8 - 4 = 4
        print(f'Line 17 - value1: {value1}')
        value2 = weights[i] # 4
        print(f'Line 18 - value2: {value2}')
        key1 = hash_table_retrieve(ht, value1) # We're retrieving key 4
        key2 = hash_table_retrieve(ht, value2) # Again here with the [4, 4]. 

        if key1 == key2:  
            # Here key 1 and key 2 are the same weight index
            print(f'key1 and key2 are equal.')
        
        if key1 is not None:
            print(f'key1: {key1} key2: {key2} limit: {limit}')

            if value1 + value2 == limit:
                if key1 > key2:
                    return [key1, key2]
                else:
                    return [key2, key1]
            elif value1 == limit:
                return [key1]

    return None


print(get_indices_of_item_weights([4, 4], 2, 8))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
