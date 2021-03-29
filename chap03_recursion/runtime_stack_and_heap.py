# Run-Time Stack and the Heap
#   Stack
#       IS like a bunch of plates, last in -> first out (aka. LIFO)
#       IS a data structure (so we're talking about USEFUL concepts not DS)
#   Heap
#       STORE everything
#       IS where ALL OBJECTS are stored (x in `x = 6` is merely a reference!)
#   Run-Time Stack
#       IS a stack (literal) of <activation records> or <call frames>
#       IS a stack (DS-type) that stores info about the active subroutines
#       IS the reason why the innermost var (multi ref, diff location) rules
#       IS also called as 'the stack', 'control stack', 'call stack' etc.
#       IS hidden and automatic in high-level prog langs (use `inspect` etc.)
#       STORE call frames
#       STORE local variables (references to the objects [stored in the heap])
#       PUSH an activation record ONTO the RT-stack when the func is CALLED
#       POP the activation record OFF when the func RETURNED (eof or `return`)

# references
#   concept
#       https://en.wikipedia.org/wiki/Call_stack
#       https://stackoverflow.com/a/33800853/6273859
#   concept with practical examples
#       https://sites.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/
#   see more
#       print call frame info
#           https://stackoverflow.com/a/16200714/6273859
