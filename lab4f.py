def outer(l):
    def inner(n):
        return l * n
    return inner
    
l = [1, 2, 3]
f = outer(l)
print(f(3))  # => ??

l.append(4)
print(f(3))  # => ??
