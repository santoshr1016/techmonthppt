with open("Counter_prac/sample.txt") as f:
    for line in f:
        print(line)

file = open("Counter_prac/sample2.txt", 'w')
try:
    file.write('Hola!')
finally:
    file.close()