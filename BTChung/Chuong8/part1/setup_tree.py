import os

if not os.path.exists('C:\\Chapter1'): 
    os.makedirs('C:\\Chapter1')
if not os.path.exists('C:\\Chapter1\\Part1'): 
    os.makedirs('C:\\Chapter1\\Part1')
if not os.path.exists('C:\\Chapter1\\Part2'): 
    os.makedirs('C:\\Chapter1\\Part2')
if not os.path.exists('C:\\Chapter2'): 
    os.makedirs('C:\\Chapter2')
if not os.path.exists('C:\\Chapter2\\Practice'): 
    os.makedirs('C:\\Chapter2\\Practice')
if not os.path.exists('C:\\Chapter3'): 
    os.makedirs('C:\\Chapter3')

os.chdir('C:\\Chapter2')
with open('.\\Practice\\test1.txt', 'w') as f:
    f.write('Content in file test1.txt')
with open('.\\Practice\\test2.txt', 'w') as f:
    f.write('Content in file test2.txt\n')
    f.write('Content in file test2.txt\n')
    f.write('Content in file test2.txt\n')
    f.write('Content in file test2.txt\n')
    f.write('Content in file test2.txt\n')
    f.write('Content in file test2.txt\n')
with open('.\\Practice\\test3.txt', 'w') as f:
    f.write('Content in file test3.txt')
