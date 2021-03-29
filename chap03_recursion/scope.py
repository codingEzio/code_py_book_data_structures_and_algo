# LEGB: Local -> Enclosing -> Global -> Built-in

# Scope
#   a part of a program where a [collection of identifiers] are [visible]

# x is NOT 6
# x is A REFERENCE that points to an object ☞ with a 6 in it
x = 6

# Identifier
#   i_var: a reference (i_var) to an object ("alex") in the local scope
#   i_param: a ref to an obj that was passed to the current func as an arg
i_var = "alex"


class i_class:
    def i_func(self, i_param):
        i_arg = i_param
        print(i_arg)


# LEGB rule
#   local: the scope of the function that the computer is executing
#   enclosed: the scope of the outer/enclosing function (nested | not global)
#   global: the top-most scope (e.g. x, i_var, i_class, say_my_name)
#   built-in: a scope that's created/loaded whenever u run a script or else
# ref:
#   https://realpython.com/python-scope-legb-rule/
say_my_name = i_class()
say_my_name.i_func(i_var)
