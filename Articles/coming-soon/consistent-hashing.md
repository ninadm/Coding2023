# Consistent hashing

In this article we will try to understand the following
1. What is hashing/hashmaps?
2. Why do I need to care about consistent hashing?
3. How can I do it in practice?
4. What are the drawbacks of consistent hashing?
5. How can we fix them?
6. Real case study where it is being used.

## What is hashing/hashmaps?

Hashing refers to basically mapping an input to an output (typically an integer) with the hopes of the output being of a fixed size and much smaller than the input. 

### Example
Let us consider the example of a very simple hashing function and see how effective it is.

hash(number) = sum of all digits till we are left with 1 digit

For example,
hash(10) => 1
hash(99) => 9 (9+9 = 18, 1 + 8 = 9)
hash(345676) = > 4 (3 + 4 + 5 + 6 + 7 + 6 = 31, 3 + 1 = 4)
and so on...

What have we acheived above?
1. We obscured the original input.
2. We obtained an output value much smaller than the given input.

Let's assume we want to now lookup what 4 mapped to, we can look up and arrive at the input 345676 if we store the above mapping.

However a problem quickly becomes evident...

What would hash(11) and hash(56) map to?

They would both generate the same output of 2. This will create what we call as a *collision*. 

Since the number of range of which inputs that can be mapped is effectively infinite (from 0 to &#8734;) however the output range is still extremely small (0 to 9), there is always a huge possibility of collisions that can take place.

This characteristic is really undesirable for an effective hash function and hence we need to come up with a better one. 
There are other problems that a good hashing function should tackle as well. 

### Characteristics of a good hash function

1. A good hash function should distribute the input fairly evenly across the output range. 
2. A good hash function should have collision resistance.
3. A good hash function should make it extremely difficult to decipher the original input from the output.
4. A good hash function should always calculate the same output given the same input.
5. A good hash function should always compute the result as efficiently as possible and have a constant time complexity
6. A good hash function should generate a substantially different output even if the input was changed only by a small amount

### HashMaps or HashTables

Simply put, a hashmap or a hashtable is a data structure that expands on the example given above and creates a mapping of each input to each output and stores it for future reference. If the hashmap uses a hashing function with all characteristics as described above adding new data to a hashmap will take constant time, looking up data will take a constant time and hence removal of data will also take constant time. The time compleixities are summarized below.

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Insertion (average)    | O(1)            |
| Insertion (worst case) | O(n)            |
| Deletion (average)     | O(1)            |
| Deletion (worst case)  | O(n)            |
| Search (average)       | O(1)            |
| Search (worst case)    | O(n)            |
| Access (average)       | O(1)            |
| Access (worst case)    | O(n)            |

> Fun fact
> In CPython, the reference implementation of Python, the hash() function uses a variant of the hash function called "MurmurHash3" for numeric and string objects. This algorithm is designed to provide good distribution and performance.


## Why do I need to care about consistent hashing?






