"""
Модуль описывающий структуру данных - стек

>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""

_stack = []

def push(x):
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear

def is_empty():
    return len(_stack) == 0

open = ('(', '[')
close = (')', ']')

def corect_brackets(s: str):
    """
    Проверяет корректность собочной последовательности
    из круглых и квадратных скобок () []

    >>> corect_brackets("(([(a)]))[]")
    True
    >>> corect_brackets("([)]")
    False
    >>> corect_brackets("(")
    False
    >>> corect_brackets("]")
    False
    """
    for brace in s:
        if brace not in open + close:
            continue
        if brace in open:
            push(brace)
        else:
            #assert brace in close, "Ожидалась закрывающая скобка: " + str(brace)
            if is_empty():
                return False
            prev = pop()
            #assert prev in open, "Ожидалась открывающая скобка: " + str(brace)
            for i in range(len(open)):
                if prev == open[i] and brace != close[i]:
                    return False
    return is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod()