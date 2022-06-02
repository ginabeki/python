# pure function
# rules of pure function
# 1. given the same input it will return the same output
# 2. should not produce side effects

def multpily_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
print(multpily_by2([1, 2, 3])) # [2, 4, 6]

# pure function is more than a guideline
# it is impossible to have pure functions everywhere
# pure functions cause less bugs
