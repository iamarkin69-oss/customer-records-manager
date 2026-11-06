from updater import add_customer, delete_customer, update_customer
from reader import list_customers, search_customer, customer_stats

def main():
    while True:
        task = input("Type in a command (add/list/delete/update/search/stats) or (e) to exit: ")
        if task == "add":
            add_customer()
        elif task == "list":
            list_customers()
        elif task == "delete":
            delete_customer()
        elif task == "update":
            update_customer()
        elif task == "search":
            search_customer()
        elif task == "stats":
            customer_stats()
        elif task == "e":
            print("See you later")
            break
        else:
            print("incorrect input")

if __name__ == "__main__":
    main()