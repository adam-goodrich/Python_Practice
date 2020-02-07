# notes

foo = 8

def print_bar():
    global foo
    print(foo)

print(foo)
print_bar()