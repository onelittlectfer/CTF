encrypted = '805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9'

encrypted_num_list = []
for i in range(0, len(encrypted), 2):
    encrypted_num_list.append(int(encrypted[i:i+2], 16))
print(encrypted_num_list)
flag = 'TWCTF{*******CENSORED********}'
flag_list = []
for i in flag:
    flag_list.append(ord(i))
print(flag_list)
# for i in range(251):
#     for j in range(251):
#         if((128* i + j) % 251 == 84 
#            and (94 * i + j) % 251 == 87
#            and (237 * i + j) % 251 == 67
#            and (203 * i + j) % 251 == 70
#            and (188 * i + j) % 251 == 123):
#             print(i, j)
#             break
i, j = 214, 51
de_flag = ''
for num in encrypted_num_list:
    de_flag = de_flag + chr((i * num + j) % 251)
print(de_flag)