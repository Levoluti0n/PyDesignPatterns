from patterns.creational import *

def main():
    print("\n----------------- Testing Singleton Pattern ----------------- \n")
    threads_test()

    print("\n----------------- Testing Factory Method Pattern ----------------- \n")
    get_vehicle_to_drive("car")
    get_vehicle_to_drive("truck")

    print("\n----------------- Testing Abstract Factory Pattern ----------------- \n")
    afactory_create_ui()

    print("\n----------------- Testing Prototype Pattern ----------------- \n")
    create_document_clone()

    print("\n----------------- Testing Builder Pattern ----------------- \n")
    builder_test()


if __name__ == "__main__":
    main()