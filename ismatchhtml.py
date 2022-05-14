from stack import ArrayStack


def is_match_html(expr):
    s = ArrayStack()
    j = expr.find('<')
    while j != -1:
        k = expr.find('>',j+1)
        if k == -1:
            return False
        tag = expr[j+1:k]
        if not tag.startwith('/'):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] != s.pop():
                return False
        j = expr.find('<',k+1)
    return s.is_empty()