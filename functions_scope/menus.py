def display_menu():
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")
    
    # Pedimos al usuario que elija una opción
    choice = input("Choose an option (1-3): ")
    
    # Convertimos a entero antes de retornar
    return int(choice)