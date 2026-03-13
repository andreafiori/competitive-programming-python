"""
Listnode definition
"""
class ListNode(object):
    """ Define and initialize a list node. """

    def __init__(self, x):
        self.val = x
        self.next = None

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None