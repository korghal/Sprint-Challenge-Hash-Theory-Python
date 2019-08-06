#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    print(ht.storage)
    for i in range(0, len(weights)):
        value1 = limit - weights[i]
        value2 = weights[i]
        key1 = hash_table_retrieve(ht, value1)
        key2 = hash_table_retrieve(ht, value2)
        if key1 is not None:
            print(f'key1: {key1} key2: {value2} limit: {limit}')
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
