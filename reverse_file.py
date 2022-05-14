from stack import ArrayStack


def reverse_file(filename):
    arrar_stack = ArrayStack()
    # orginal = open(filename)
    with open(filename) as orginal:
        for line in orginal:
            arrar_stack.push(line.rstrip('\n'))
    # orginal.close()

    # output = open(filename,'w')
    with open(filename,'w') as output:
        while not arrar_stack.is_empty():
            output.write(arrar_stack.pop() + '\n')


if __name__ == '__main__':
    reverse_file('test.txt')