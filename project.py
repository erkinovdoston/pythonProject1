import json

def unique_id1():
    lt = []
    a = readfile('id.json')
    nnn = '2'
    for i in a:
        if i['type'] == 1:
            a = readfile('id.json')
            for i in a:
                lt.append(i['id'])
    af = max(lt) + 1

    dic = {
        'type': 1,
        'id': af
    }
    writefile(dic, 'id.json')


def unique_id2():
    lt = []
    a = readfile('id.json')
    nnn = '2'
    for i in a:
        if i['type'] == 2:
            a = readfile('id.json')
            for i in a:
                lt.append(i['id'])
    af = max(lt) + 1

    dic = {
        'type': 2,
        'id': af
    }
    writefile(dic, 'id.json')


def unique_id3():
    lt = []
    a = readfile('id.json')
    nnn = '2'
    for i in a:
        if i['type'] == 3:
            a = readfile('id.json')
            for i in a:
                lt.append(i['id'])
    af = max(lt) + 1

    dic = {
        'type': 3,
        'id': af
    }
    writefile(dic, 'id.json')



def unique_id4():
    lt = []
    a = readfile('id.json')
    nnn = '2'
    for i in a:
        if i['type'] == 4:
            a = readfile('id.json')
            for i in a:
                lt.append(i['id'])
    af = max(lt) + 1

    dic = {
        'type': 4,
        'id': af
    }
    writefile(dic, 'id.json')




def readfile(a):
    with open(a, 'r') as file:
        f = json.load(file)
        return f


def writefile(d, a):
    f = readfile(a)
    lst = []
    for i in f:
        lst.append(i)
    lst.append(d)

    with open(a, 'w') as file:
        json.dump(lst, file, indent=3)


while True:
    menu = input("1.sign in  |  2.sign up : ")
    if menu == "1":
        username = input("username : ")
        password = input("password : ")
        a = readfile('users.json')
        for i in a:
            if i['username'] == username and i['password'] == password:
                menu2 = input("1.identification  |  2.card  |  3.log out : ")
                if menu2 == '1':
                    bb = int(input('1.Create  |  2.Have : '))
                    if bb == 1:
                        name = input("name : ")
                        last_name = input("lastname : ")
                        thridname = input("thridname : ")
                        print("Your Birtday")
                        birthd = int(input('Day : '))
                        birthm = int(input('Month : '))
                        birthy = int(input('Year : '))
                        p_seria = input('Passport seria : ')
                        pa_number = input('Passport number : ')
                        p_jshr = input('Passport jshr : ')


                        g = readfile('iden.json')

                        p = {
                            "id": len(g) + 1,
                            "name": name,
                            "lastname": last_name,
                            "thridname": thridname,
                            "birthd": birthd,
                            "birthm": birthm,
                            'birthy': birthy,
                            'passpord_seria': p_seria,
                            'passpord_number': pa_number,
                            'passpord_jshr': p_jshr
                        }
                        writefile(p, 'iden.json')



                    elif bb == 2:
                        name = input("Name : ")
                        p_jshr = input("Passpord JSHR : ")

                        a = readfile('iden.json')
                        for i in a:
                            if i['name'] == name and i['passpord_jshr'] == p_jshr:
                                e = readfile('iden.json')
                                hh = 'name'
                                print('id :', i["id"],'\nname :', i["name"],'\nlasname :', i["lastname"],'\nbirthday :', i["birthd"],'\nbirthmonth :', i["birthm"],'\nbirthyear :',i['birthy'],'\npasspord seria :', i["passpord_seria"],'\npasspord number :', i["passpord_number"],'\npospord jshr :', i["passpord_jshr"])




                elif menu2 == '2':
                    menu3 = input("1.my cards  |  2.create card  : ")
                    if menu3 == '1':
                        c = readfile('cards.json')
                        for i in c:
                            print(i)
                    elif menu3 == '2':
                        c = readfile('card_type.json')
                        for i in c:
                            print(i['name'], ' : ', i['id'])

                        a = readfile('id.json')
                        e = {
                            'type':'3'


                        }




                        card_type = int(input("card type id : "))
                        card_number = int(input("card number : "))
                        card_date = input("card date : ")
                        is_virtual = int(input("is virtual  1.yes  |  2.no : "))

                        c1 = readfile('card_type.json')

                        cc = {
                            "id" : len(c1)+1,
                            "card_type": card_type,
                            "card_number": card_number,
                            "card_date": card_date,
                            "is_virtual": is_virtual,
                            "owner_id": i['id']
                        }

                        writefile(cc, 'cards.json')

                elif menu2 == '3':
                    break

    elif menu == '2':
        username = input("enter username : ")
        email = input("enter email : ")
        password = input("enter password : ")
        p_number = int(input("enter phone number : +998"))
        passpord_number = int(input('enter passport number : '))

        u = readfile('users.json')
        d = {
            "id": len(u) + 1,
            "username": username,
            "email": email,
            "password": password,
            'phone number': p_number,
            "passpord number": passpord_number
        }

        writefile(d, 'users.json')
        unique_id1()

