# base13.py

# ファイル入力

file_path = "resources/input.csv"
f = open(file_path, mode="r", encoding="utf-8")

# line = f.read()
# print(line)

# lines = f.readlines() # 改行区切りで表示
# print(lines)
# for x in lines:
#     print(x.rstrip("\n"))

# line = f.readline() # 中身全体
# while line:
#     print(line.rstrip("\n"))
#     line = f.readline()

# line = f.readline()
while (line := f.readline()):
    print(line.rstrip("\n"))
#     line = f.readline()

f.close() # ファイルを閉じることができる
# -> メモリをくう。他の処理でファイルを開けない
with open(file_path, mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

print(f.read())