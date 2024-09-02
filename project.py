import  csv;
contacts=[]

def save_contacts():
    with open("adress_books.csv", "w" ,newline="") as files:
        name_headers = ["Name", "Family", "Phone" , "Email" ,"City" , "Address"]
        write=csv.DictWriter(files, fieldnames=name_headers)
        write.writerows(contacts)
def Add_contacts():
   print(" Add new contacts  ")
   name=input("Name:")
   family=input("Family:")
   phone=input("Phone:")
   email=input("Email:")
   city=input("City:")
   address=input("Address:")
   if not phone.isdigit():
       raise  ValueError(" phone is numberic")
   contact={"Name":name,"Family":family,"Phone":phone,"Email":email,"City":city,"Address":address}
   contacts.append(contact)
   save_contacts()
   print(f"Added has {name, family} has been successfully added")


def view_contacts():
    print("view contacts")
    for contact in contacts:
        print(f"Name: {contact['Name']}" )
        print(f"Family: {contact['Family']}" )
        print(f"Phone: {contact['Phone']}" )
        print(f"Email: {contact['Email']}" )
        print(f"City: {contact['City']}" )
        print(f"Address: {contact['Address']}" )
        print("----"*30)

def Update_contacts():
    print("update contacts")
    phone=input("pleae enter your phone")
    if not phone.isdigit():
        raise ValueError("phone is numberic")
    for contact in contacts:
        if contact["Phone"]==phone:
            print(f"contact find succesfully is your {contact['Name']}")
            print(f"Name: {contact['Name']}")
            print(f"Family: {contact['Family']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"City: {contact['City']}")
            print(f"Address: {contact['Address']}")
            print("----" * 30)

            new_name=input("new_name(please enter new name)").strip()
            new_family=input("new_family(please enter new family)").strip()
            new_phone=input("new_phone(please enter new phone)").strip()
            new_email=input("new_email(please enter new email)").strip()
            new_city=input("new_city(please enter new city)").strip()
            new_address=input("new_address(please enter new address)").strip()
            if new_name:
                contact["Name"]=new_name
            elif new_family:
                contact["Family"]=new_family
            elif new_phone:
                contact["Phone"]=new_phone
            elif new_email:
                contact["Email"]=new_email
            elif new_city:
                contact["City"]=new_city
            elif new_address:
                contact["Address"]=new_address
    save_contacts()
    print(f"update has been succesfully{contact['Name']}")
    return

def Delet_contant():
    print("plese phone number")
    phone=input("please enter phone number")
    if not phone.isdigit():
        raise  ValueError("phone is numberic")
    for contact in contacts:
        if contact["Phone"]==phone:
            deleted_name=contact["Name"]
            contacts.remove(contact)
            save_contacts()
            print(f"delete {deleted_name} has been deleted")
            return

        print("not found")

def open_files():
    try:
        with open("adress_books.csv" ,"r") as files:
            lines=csv.DictReader(files)
            for line in lines:
               contacts.append(line)

    except FileNotFoundError:
     print("file not found")

open_files()

while True:
     try:

         print("1. Add new contact")
         print("2. View contacts")
         print("3. updates  contacts")
         print("4. Delete contacts")
         print("5. Exite contacts")

         choise=int(input("please enter number ").strip())
         if choise==1:
            Add_contacts()
         elif choise==2:
           view_contacts()
         elif choise==3:
              Update_contacts()
         elif choise==4:
           Delet_contant()
         elif choise==5:
           print("good bye amin"), exit()
     except Exception as e:
         print(f"Eror:{e}")










