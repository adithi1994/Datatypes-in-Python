def DISPLAY_MENU():
    print("\nSHOPPING CART MENU: ")
    print("1:ADD ITEM")
    print("2:DISPLAY TOTAL")
    print("3:REMOVE ITEM")
    print("4:DISPLAY ALL ITEMS")
    print("5:EXIT")

def ADD_ITEM(CART):
    ITEM_NAME=input("Enter name of item: ").strip()
    try:
        ITEM_PRICE=float(input("Enter the price: "))
        if ITEM_NAME in CART:
              CART[ITEM_NAME] += ITEM_PRICE
        else:
            CART[ITEM_NAME] = ITEM_PRICE
    except ValueError:
        print("Invalid price.Please enter a number.")

def REMOVE_ITEM(CART):
    ITEM_NAME = input("Enter name of item: ").strip()
    if ITEM_NAME in CART:
        del CART[ITEM_NAME]
        print(f"Item {ITEM_NAME} removed from cart")
    else:
        print(f"{ITEM_NAME} not found in cart")

def DISPLAY_TOTAL(CART):
    TOTAL_PRICE=sum(CART.values())
    print(f"\nTotal price of items in cart : {TOTAL_PRICE}")

def VIEW_CART(CART):
    if CART:
        print("\n Items in your cart: ")
        for items,price in CART.items():
            print(f"{items} : ${price:.2f}")
    else:
        print("Your cart is empty")

def main():
        CART={}
        while True:
            DISPLAY_MENU()
            choice=int(input("Enter your choice: "))


            if choice == 1:
                ADD_ITEM(CART)

            elif choice == 2:
                DISPLAY_TOTAL(CART)

            elif choice == 3:
                REMOVE_ITEM(CART)

            elif choice == 4:
                VIEW_CART(CART)

            elif choice == 5:
                print("EXITING SHOPPING CART")

            else:
                print("Invalid choice,please try again")

if __name__=="__main__":
    main()


