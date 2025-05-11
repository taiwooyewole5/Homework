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
print(f"{last_name}, {first_name}")
print(f"{Job_title}")
print(f"ID: {id_number}")
print()
print(f"{email_address}")
print(f"{phone_number}")
print("--------------------------------------")

