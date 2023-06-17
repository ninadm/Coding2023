

# IP Routing Table
#  
# Purpose = directing incoming traffic to the appropriate port / application
#  
# IP = 6 digit string (ex: 101010)
#  
# DATA STRUCTURE:
# IP Prefix => Port
# 10        => 3
# 010       => 4
# 1111      => 5
# 100       => 6
#  
# USAGE:
# IP Lookup => Port
# 101010    => 3
# 111111    => 5
# 100111    => 6
#  
# TO IMPLEMENT:
# 1. void insert(ipPrefix, port);
# 2. int lookup(ip); // returns port
# 3. unit tests

class Node:
    #value is a tuple
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:

    head = Node((-1, None))
    def insert(self, ipPrefix, port):
        dummy = self.head
        for i in range(ipPrefix):
            if ipPrefix[i] == '0':
                if not dummy.left:
                    if i == len(ipPrefix) - 1:
                        node = Node((0, port))
                        dummy.left = node
                    else:
                        node = Node((0, None))
                        dummy.left = node
                if dummy.left and i == len(ipPrefix) - 1:
                    dummy.left.val = (0, port)
                elif i < len(ipPrefix) - 1:
                    dummy = dummy.left
            else:
                if not dummy.right:
                    if i == len(ipPrefix) - 1:
                        node = Node((0, port))
                        dummy.right = node
                    else:
                        node = Node((0, None))
                        dummy.right = node
                if dummy.right and i == len(ipPrefix) - 1:
                    dummy.right.val = (0, port)
                elif i < len(ipPrefix) - 1:
                    dummy = dummy.right
