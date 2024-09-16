contacts={}
def create_contact():
    name = input("enter the name :")
    phone = input("enter the phone number :")
    email = input("enter your email :")
    contacts[name] = {"phone" : phone ,
                      "email" : email}

def update_contacts(name):
    new_phone = input("enter the new phone : ")
    new_email = input("enter the email : ")
    contacts[name] = {"phone" : new_phone ,
                      "email" : new_email}
def delete_contacts(name):
    if name in contacts:
        del contacts[name]
    else:
        print("this contact doesnot exist !!! ")



def view_contacts():
    for name, details in contacts.items():
        print("name : " , name)
        print("phone" , details["phone"])
        print("email" , details["email"])


while(True):
    print("Contact Management System\n"
          "----------------------------\n"
          "1. Add Contact\n"
          "2. Update Contact\n"
          "3. Delete Contact\n"
          "4. View Contacts\n"
          "5. Exit\n"
          "----------------------------")
    user_response = int(input("enter your choice depend upon the list : "))
    if user_response ==1:
        create_contact()
    elif user_response ==2 :
        update_contacts()
    elif user_response == 3:
        delete_contacts()
    elif user_response == 4:
        view_contacts()
    elif user_response == 5:
        exit()
    else:
        print("there is error with your response ! ")