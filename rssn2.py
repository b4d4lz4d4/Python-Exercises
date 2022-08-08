# Sual:1
# usint = input("İstifadəçinin girdiyi ədəd: ")

# if not usint.isnumeric():
#     print("Yalniz rəqəm daxil edin!")
# elif int(usint)%7==0 and int(usint)%3==0 and int(usint)%8==0 :
#     print("eded 7, 8 ve 3`e qaliqsiz bölünür")   
# else:
#     print("eded 7, 8 ve 3`e qaliqsiz bölünmür")
# ==============================
# # Sual:2
# id = input("Şexsiyyet vesiqesinin kodunu daxil edin: ")
# if len(id) == 10:
#     if id[0:3].isascii() and id[0:3].isupper() and id[3:].isnumeric():
#         print("kod duzgundur")
# else:
#     print("kod dogru deyil!")
# ==============================
# Sual:4

pswrd = input('şifreni daxil edin: ')

if not 8 < len(pswrd) < 40:
    if len(pswrd) < 8:
        print('Şifre 8-dən kiçik ola bilmez kişi!')
    else:
        print('Şifre 40-dan böyük ola bilmez kişi!')
elif not pswrd.isascii():
    print('Yalnız ingilis şriftinden istifade et kişi!')
elif not pswrd.isalnum():
    print('Yalnız herf ve reqem daxil et kişi!')
elif not (pswrd[0].isupper() and pswrd[0].islower()):
    print('Ən az bir böyük və kiçik hərf olmalıdır!')
elif not (pswrd[0].isalnum() and pswrd[0].isalpha()):
    print('en az 1 hərf ve en az 1 reqem olmalıdır!')
else:
    print('Şifre dogrudur kişi!')