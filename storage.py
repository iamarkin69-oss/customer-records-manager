import json

def load_customers():
    try:
        with open("customers.json", "r", encoding="utf-8") as json_file:
            try:
                start = 0
                data = json.load(json_file)
                if type(data) is list and len(data) > 0:
                    for line in data:
                        if type(line) is dict:
                            start += 1
                            customer_id = (
                                 type(line.get("id")) is int
                                and line.get("id") > 0
                            )
                            name = (
                                type(line.get("name")) is str
                                and line.get("name").strip() != ""
                            )
                            email = (
                                type(line.get("email")) is str
                                and line.get("email").strip() != ""
                            )
                            city = (
                                type(line.get("city")) is str
                                and line.get("city").strip() != ""
                            )
                            
                            if len(line) == 4 and customer_id and name and email and city:
                                continue
                            else:
                                print(f"line {start} structure is damaged, first delete the line and rewrite it.")
                                print(f"Line data: {line}")
                                return
                        else:
                            print("Can not open a file")
                            return
                    print("JSON loaded")
                    return data
                elif type(data) is list and len(data) == 0:
                    return "empty"
                else:
                    print("Can not open a file")
                    return
            except json.JSONDecodeError:
                print("File is damaged.")
                return 
    except FileNotFoundError:
        return "no file"
            
            

def save_customers(customers):
    with open("customers.json", "w", encoding="utf-8") as json_file:
        json.dump(customers, json_file, ensure_ascii=False, indent=4)
    return "JSON data changed succesfully"


