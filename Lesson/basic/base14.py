# セット

s = {"a", "b", "c", "d"}
t = {"c", "d", "e", "f"}

u = s | t
print(u)

u = s & t
print(u)

u = s - t
print(u)

u = s ^ t
print(u)

s |= t
print(u)

# issubset, issuperset, isdisjoint
s = {"apple", "banana"}
t = {"apple", "banana", "lemon"}
U = {"cherry"}

print(s.issubset(t))
print(s.issuperset(s))

print(t.isdisjoint(s))
print(t.isdisjoint(u))