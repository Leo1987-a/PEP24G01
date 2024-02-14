# applicatie verificare password

def check_password():
    requires_chars = ['!','@','%']
    password = input('Introduceti password:')
    print(password)
    condition_not_ok = False
    if len(password) < 7:
        print('Parola cu lungimea gresita!!')
        condition_not_ok = True
        check_password()
    else:

        for character in requires_chars:
            if character in password:

                print('Parola contine un caracter special:! @ %')
            break
        else:
            print('Parola nu contine un caracter special ! @ %:')
            condition_not_ok = True



check_password()



def check_passwd():
    requires_chars = ["!", "@", "%"]
    passwd = input("Introduceti o parola : ")
    print(passwd)
    condition_not_ok = False
    if len(passwd) < 7:
        print("Parola cu lungime gresita")
        condition_not_ok = True

    for character in requires_chars:
        if character in passwd:
            break
    else:
        print("Parola trebuie sa contina : ! @ %")
        condition_not_ok = True

    for character in range(10):
        if str(character) in passwd:
            break
    else:
        print("Parola trebuie sa contina : number")
        condition_not_ok = True

    if condition_not_ok:
        check_passwd()
check_passwd()