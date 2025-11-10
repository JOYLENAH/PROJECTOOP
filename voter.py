from user import User

class Voter(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.__has_voted = False  # Encapsulated attribute

    def cast_vote(self):
        if not self.__has_voted:
            self.__has_voted = True
            print(f"{self._name}, your vote has been recorded!")
        else:
            print("You have already voted!")

    def show_menu(self):
        print("=== Voter Menu ===")
        print("1. Cast Vote")
        print("2. View Candidates")
