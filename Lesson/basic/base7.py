# 文字列型

fruit = "apple"
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + " banana"
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = "banana"
print(fruit[1])

# encode, decode => bytes[]
byte_fruit = fruit.encode("utf-8")
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode("utf-8")
print(str_fruit)
print(type(str_fruit))

# count

msg = "ABCDEABC"
print(msg.count("ABCDEF"))

# startswith, endswith

print(msg.startswith("ABCD"))
print(msg.endswith("DC"))

# strip(両橋), rstrip(右端), lstrip(左端)

msg = " ABC "
print(msg)
print(msg.strip())
msg = "ABCDEFABC"
print(msg.strip("CBA"))
print(msg.lstrip("CBA"))
print(msg.rstrip("CBA"))


# upper , lower, swapcase, replace, capitalize

msg = "abcABC"
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC", "FFF", -1)
print(msg_r)

msg = "hello world"
print(msg.capitalize())

# 文字列の一部取り出し、 format, islower, isupper

msg = "hello, my name is taro"
print(msg[1:10:3])
print("hello {}".format("Taro"))
name = "Jiro"
print(f"hello {name}")
print(f"{name=}")

msg = "apple , BANANA"
print(msg.islower())
print(msg.isupper())

# find, index, rfind, rindex

msg = "ABCDEABC"
print(msg.find("ABC"))
print(msg.rfind("ABC"))
print(msg.index("ABC"))
print(msg.rindex("ABC"))

print(msg.find("ABCE"))
print(msg.index("ABCE"))