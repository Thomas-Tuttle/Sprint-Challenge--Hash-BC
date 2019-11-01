#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
#############################################################################################################
    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    for r in range(length):
        if route[r-1] is not None:
            route[r] = hash_table_retrieve(hashtable, route[r-1])
#############################################################################################################
    return route
