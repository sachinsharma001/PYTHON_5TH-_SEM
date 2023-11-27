# file= open("textfile.txt")
# count = 0
# for line in file:
#     if line !='\n':
#         count+=1
# file.close()
# print(count)


# Create a text file 'Myfile.txt' in python and ask the user to write separate 3 lines with three input statements
# from the user.
with open('Myfile.txt','w') as file:
    for i in range(3):
        line = input(f'Enter line {i + 1}: ')
        file.write(line+'\n')
print("Three lines have been written to Myfile.txt.")