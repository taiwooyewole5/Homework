print("Please enter the following infomation:")
print()

first_name  = input("First name: ")
last_name  = input("Last name: ")
email_address = input("Email  address: ")
phone_number  = input("phone number: ")
Job_title = input("job title: ")
id_number = input("ID number: ")

#print("\") to get a  new line

print("\nThe ID Card is:")
print("--------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize}")
print(f"{Job_title.title()}")
print(f"ID: {id_number}")
print()
print(f"{email_address.lower()}")
print(f"{phone_number}")
print("--------------------------------------")

