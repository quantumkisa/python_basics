count_words = []
with open('5_2_file.txt') as f:
    lines = f.readlines()
    for index, value in enumerate(lines):
        number_of_words = len(value.split(" "))
        count_words.append(number_of_words)
print(f"Кол-во строк = {len(lines)}")
print(f"Кол-во лов в строках - {count_words}")


