from stack import ArrayStack


def is_match(expr):
    left = '({['
    right = ']})'
    array_stack = ArrayStack()
    for c in expr:
        if c in left:
            array_stack.push(c)
        elif c in right:
            if array_stack.is_empty():
                return False
            if right.index(c) != left.index(array_stack.pop()):
                return False
    return array_stack.is_empty()


print(is_match('[(5+x)-(y+z)]'))