
### Chapter Goals
> By the end of this chapter, you should be able to answer these questions.
- How does Python determine the meaning of an identifier in a program?
- What happens to the run-time stack when a function is called?
- What happens to the run-time stack when a function returns from a call?
- What are the two important parts to a recursive function and which part comes
first?
- Exactly what happens when a return statement is executed?
- Why should we write recursive functions?
- What are the computational complexities of various recursive functions?

### Run-time stack and heap
- The params and body of each func define a scope must be stored somewhere
within the RAM of a computer.
- Python splits the RAM up into two parts,
called "Run-time Stack" (it IS "stack") and the "Heap".

### Keyword
- Stack
    > first in, last out (stores references to objects (points to the heap))
- Heap
    > the area of RAM where all objects are stored, literally.
