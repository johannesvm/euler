
def less_than(original, n):
    a = [i for i in original if i < n]
    return a

a = [3, 4, 6, 1]
b = [1, 2, 3, 4, 5, 6]
c = [9, 5, 2, 7, 3]
n = 4

new_a = less_than(a, n)
new_b = less_than(b, n)
new_c = less_than(c, n)

print(new_a, new_b, new_c)
