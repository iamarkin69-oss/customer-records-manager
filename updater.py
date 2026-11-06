import json
from storage import load_customers, save_customers
def add_customer():
    loaded = load_customers()
    if loaded == None:
        return
    
    whole_data = []
    one_customer = {}
    ids = []
    name  = input("Name: ").strip()
    if name == "" or type(name) is not str:
        print("invalid data, try again later")
        return 
    email = input("Email: ").strip()
    if email == "" or type(email) is not str:
        print("invalid data, try again later")
        return 
    city = input("City: ").strip()
    if city == "" or type(city) is not str:
        print("invalid data, try again later")
        return 

    if loaded == "no file" or loaded == "empty":
        one_customer = {
            "id": 1,
            "name": name,
            "email": email,
            "city": city
        }
        whole_data.append(one_customer)
        print(save_customers(whole_data))
        return " "
    elif type(loaded) is list:
        for line in loaded:
            ids.append(line.get("id"))
        if ids:
            customer_id = max(ids) + 1
        else:
            customer_id = 1
        one_customer = {
            "id": customer_id,
            "name": name,
            "email": email,
            "city": city
        }
        for string in loaded:
            whole_data.append(string)
        whole_data.append(one_customer)
        print(save_customers(whole_data))
        return 

def delete_customer():
    found = False
    try:
        customer_id = int(input("Type in customers id: "))
    except ValueError:
        print("Incorrect input, try again later")
        return

    whole_data = []
    
    data = load_customers()
    if data == None:
            return
    
    if data == "no file" or data == "empty":
        print("Can not operate this command until the file 'customers.json' will have customers")
        return
    elif type(data) is list:
        for line in data:
            if customer_id == line.get("id"):
                found = True
                print("Deleted succefully")
                continue
            whole_data.append(line)

        if found == False:
            print(f"No customer with ID {customer_id} found")
        else:
            save_customers(whole_data)
    return


def update_customer():
    found = False
    try:
        customer_id = int(input("Type in customers id: "))
    except ValueError:
        print("Incorrect input, try again later")
        return

    whole_data = []
    
    data = load_customers()
    if data == None:
            return
    
    if data == "no file" or data == "empty":
        print("Can not operate this command until the file will have customers")
        return
    elif type(data) is list:
        for line in data:
            if customer_id == line.get("id"):
                
                update = input("Type in (email/city/name) to choose data to change: ")
                text = input("Changed data: ").strip()
                if type(text) is str and text != "":
                    if update == "email":
                        line["email"] = text
                        print("Email changed")
                    elif update == "city":
                        line["city"] = text
                        print("City changed")
                    elif update == "name":
                        line["name"] = text
                        print("Name changed")
                    else:
                        print("First input must be 'name', 'email' or 'city'")
                        return
                else:
                    print("Incorrect input, try again later")
                    return
                found = True
            whole_data.append(line)

        if found == False:
            print(f"No customer with ID {customer_id} found")
        else:
            save_customers(whole_data)
    return