from klasy import *

private_users = [PrivateAccount("Jan Kowalski","7788990011"),
                PrivateAccount("Alicja Nowak", "8899001122"),
                PrivateAccount("Grzegorz Król", "9900112233")]

business_users = [BusinessAccount("Krzak", "0011223344","3129","2578"),
                BusinessAccount("Magnolia", "1122334455", "2539", "7878"),
                BusinessAccount("Przebiśnieg", "2233445566","5629","9648")]

for private_user in private_users:
    private_user.show_info()

for business_user in business_users:
    business_user.show_info_business()

with open('C:\\Users\\pawel\\Desktop\\Iga\\PycharmProjects\\pythonProject\\OOP Lab2\\Zad2\\business_users.txt', 'w') as file:
    for business_user in business_users:
        file.write(str(business_user) + '\n')

business_users = []
with open('C:\\Users\\pawel\\Desktop\\Iga\\PycharmProjects\\pythonProject\\OOP Lab2\\Zad2\\business_users.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        user_data = line.strip().split(',')
        if len(user_data) == 3:
            business_user = BusinessAccount(user_data[0], user_data[1], user_data[2])
            business_users.append(business_user)