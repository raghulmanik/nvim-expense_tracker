from ui.menu import print_menu
from work_functions import add_transaction


def main():

    while True:
        print_menu()
        choice = input("> ")

        if choice == "b":
            break

        elif choice == "1":
            add_transaction()


if __name__ == "__main__":
    main()
