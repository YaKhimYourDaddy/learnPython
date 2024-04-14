import os

os.chdir('C:')

# 1
print(os.getcwd())

# 2
os.chdir('C:\\Chapter1\\Part2')
print(os.getcwd())

# 3
os.chdir('C:\\Chapter3')
print(os.getcwd())

# 4
with open('..\\Chapter2\\Practice\\test1.txt', 'r') as f:
    print(f.readlines())

# 5
with open('C:\\Chapter2\\Practice\\test1.txt', 'r') as f:
    print(f.readlines())