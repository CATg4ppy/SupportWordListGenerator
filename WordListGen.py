import random
import os


number_of_users = int(input('Enter number of users: '))




users = []
for i in range(number_of_users):
    login_input = input('Enter login: ')
    users.append(login_input)



passwrds = []
pass_list = []
pass_buffer = []
pass_input = ''
while True:
    pass_input = input('For stop printing enter STOP\nInput word for passwords:\n')
    if pass_input != 'STOP':
        pass_list.append(pass_input)
    else:
        break
pass_lenght = int(input('Enter number of words in password: '))
for i in range(number_of_users):
    random.shuffle(pass_list)
    pass_buffer = ''.join(map(str, pass_list[0:pass_lenght]))
    passwrds.append(pass_buffer)
    pass_buffer = list()



output = dict(zip(users,passwrds))
output_directory = input('Set directory for output file: \n ')
with open(output_directory+"WordListGen.txt", "w") as output_file:
    for key, value in output.items():
        output_file.write('%s\n%s\n\n' % (key, value))
