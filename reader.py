
from storage import load_customers

def list_customers():
    data = load_customers()
    if type(data) is not list and data == "empty":
        print("No data in file")
        return
    elif type(data) is not list and data == "no file":
        print("No file")
        return
    elif type(data) is not list:
        return
    
    if len(data) > 0:
        for customer in data:
            print(f"{customer["id"]:<4} | {customer["name"]:<18} | {customer["email"]:<30} | {customer["city"]:<14}")
        return 
    else:
        print("file is empty")
        return 

def search_customer():
    data = load_customers()
    
    if type(data) is not list and data == "empty":
        print("No data in file")
        return
    elif type(data) is not list and data == "no file":
        print("No file")
        return
    elif type(data) is not list:
        return
    
    try:
        customer_id = int(input("Type in customers id: "))
    except ValueError:
        print("Incorrect input, try again later")
        return
    
    if len(data) > 0:
        found = False
        for customer in data:
            if customer_id == customer["id"]:
                found = True
                for key, value in customer.items():
                    print(f"{key}: {value}")
        if found:
            return
        else:
            print("No such id found") 
    else:
        print("file is empty")
        return 

def customer_stats():
    data = load_customers()
    if type(data) is not list and data == "empty":
        print("No data in file")
        return
    elif type(data) is not list and data == "no file":
        print("No file")
        return
    elif type(data) is not list:
        return
    
    stats = {}
    if len(data) > 0:
        for customer in data:
            if customer["city"] in stats:
                stats[customer["city"]].append(customer["name"])
            else:
                stats[customer["city"]] = []
                stats[customer["city"]].append(customer["name"])
        for key, value in stats.items():
            print(f"{key}: {value}")
    else:
        print("file is empty")
        return 