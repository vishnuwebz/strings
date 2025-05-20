# 1 word counter

text = "Python is easy and python is powerful"

word_list = text.lower().split()

count= word_list.count("python")

print(f"Word 'python' appeared {count} times")

"Word 'python' appeared 2 times"