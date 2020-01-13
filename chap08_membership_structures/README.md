
### The idea of *bloom filter*
- Making *test membership in a set* **quicker**. That means two things:
    - Less queries to the *server*, let most of the stuff happen in the *client*
    - Less interaction <small>(cuz the less operations made by the algorithm)</small> to the *disk*
- A *hash table* would do, but it doesn't always meet the two needs we mentioned.
    > This also means other data structures like *Linked List* won't work good enough either, since searching in hash table is already quick enough.<br>

- Simply put <small>(in different tones)</small>,
    1. It's all about *trade-off*, whether it's *space* <small>(disk, memory)</small> or simply *speed*.
    2. Used when the data is **really large** and you need search it, whereas small error rate is *accepted*.
    3. Is it *in it* or *not*?

### How does *bloom filter* work <small>(my own notes/thoughts)</small>
- Stage zero
    - Instead of using mostly-used-for-arrays algorithms, we use *fast hash stuff* and *low-cost operations* <small>(like switching `0` and `1` in a *bit array*)</small>.
    - But of course, we made some trade-offs, such as, the bits cannot be *removed* and the algorithm won't be *100% correct*.
    - Finally, do note that it's all about ***membership test***, there's no *fancy stuff* going on.
- Stage one
    - An arrry of bits all set to `0`, like `0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣` <small>(I need the *boxes*)</small>.
- Stage two
    - Using different hash functiones to `hash` the input, and then marking them on the *bit array*.
        ```python
        # INITIAL: 0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣

        # AFTER:   0️⃣1️⃣0️⃣0️⃣4️⃣0️⃣0️⃣7️⃣0️⃣0️⃣
        hash_function_x("Krista") % N = 1
        hash_function_y("Krista") % N = 4
        hash_function_z("Krista") % N = 7

        # AFTER:   0️⃣1️⃣0️⃣0️⃣4️⃣5️⃣0️⃣7️⃣0️⃣9️⃣
        hash_function_x("Alison") % N = 4   # the core of 'probabilistic', since Krista also "has" this
        hash_function_y("Alison") % N = 5
        hash_function_z("Alison") % N = 9
        ```

    - What do we know from this bit array?
        1. First of all, all the data should be hashed and then stored in this bit array
        2. After that, we compared our *hashed input* <small>(e.g. search keyword)</small> with the *bit array*.
        3. Basically we could draw *two* conclusions from the result
            - It's *definitely* **NOT** present <small>(not marked)</small>
            - It's *probably* present <small>(marked, but it was probably marked by *other* items)</small>
- Stage three
    - What can we do to make this algorithm *better*?
        1. *More* and *faster* hash functions: *reducing false positives*, *speed up this whole thing*
        2. *Larger* <u>bit arrays</u>: *storing the hashed results* in the <small>(simple)</small> *bit array*
- Final word
    > [*Luis Casillas*](https://crypto.stackexchange.com/a/52735): Bloom filters are normally used to short-circuit more expensive checks—if the filter returns "no" you avoid an expensive operation, but then if it returns "maybe" you have to do the expensive operation to actually confirm whether it's a "yes."


### References
- *Bloom filter*
    1. [Bloom Filters – Introduction and Python Implementation](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)
    2. [Probabilistic Data structures: Bloom filter](https://hackernoon.com/probabilistic-data-structures-bloom-filter-5374112a7832)
    3. More on this
        - [What are Bloom filters?](https://blog.medium.com/what-are-bloom-filters-1ec2a50c68ff)
        - [ Simple Bloom filter implementation in Python 3 (for use with the HIBP password list)](https://gist.github.com/marcan/23e1ec416bf884dcd7f0e635ce5f2724)
- *Trie*
    1. [Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014) <small>([*Vaidehi Joshi*](https://medium.com/@vaidehijoshi))</small>
    2. [An implementation on Github](https://github.com/ZoranPandovski/al-go-rithms/tree/master/data_structures/trie)
    3. [Trie on Wikipedia](https://en.wikipedia.org/wiki/Trie)
