class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    def login(self):
        print(f"{self._name} logged in successfully.")

    def show_menu(self):
        pass  # To be overridden by subclasses (Polymorphism)
