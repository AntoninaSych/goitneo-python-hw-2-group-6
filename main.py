from ContactsClass import Contacts

# while True:
#     user_input = input("Enter")

con = Contacts()
con.add_contact("Antonina",'12321312','sdfsdf@sdf.dsf',True)
con.add_contact("Anton",'3333333','anton@sdf.dsf',False)
print(con.get_contact(1))
print(con.remove_contact(1))
print(con.remove_contact(1))
