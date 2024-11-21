from patterns.creational import *
from patterns.structural import *

def main():
    #----------------------  CREATIONAL PATTERNS  ----------------------

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

    #----------------------  STRUCTURAL PATTERNS  ----------------------

    print("\n----------------- Testing Adapter Pattern ----------------- \n")
    process_payment(100)

    print("\n----------------- Testing Bridge Method Pattern ----------------- \n")
    bridge_toggle()

    print("\n----------------- Testing Composite Pattern ----------------- \n")
    composite_folder()

    print("\n----------------- Testing Decorator Pattern ----------------- \n")
    decorator_crypting()

    print("\n----------------- Testing Facade Pattern ----------------- \n")
    facade_smart_home()

    print("\n----------------- Testing Flyweight Pattern ----------------- \n")
    flyweight_forest_draw()

    print("\n----------------- Testing Proxy Pattern ----------------- \n")
    proxy_image()

if __name__ == "__main__":
    main()
