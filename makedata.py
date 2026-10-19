text = input("文字列を入力してください: ")

result = ",".join(f'"{c}"' for c in text)

print(result)