class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 8 #hunger level
        self.energy = 4  #energy level
        self.happiness = 5 #happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Prevent hunger from going below 0
        self.happiness = min(10, self.happiness + 1)  # Prevent happiness from exceeding 10
        print(f"{self.name} eats happily! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Prevent energy from exceeding 10
        print(f"{self.name} takes a nap! Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:  # Ensure pet has enough energy to play
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)  # Prevent happiness from exceeding 10
            self.hunger = min(10, self.hunger + 1)  # Hunger slightly increases
            print(f"{self.name} is having fun! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play! Try sleeping first.")

    def get_status(self):
        print(f"🔹 {self.name}'s Status:\nHunger: {self.hunger}/10\nEnergy: {self.energy}/10\nHappiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)  # Training boosts happiness
        print(f"{self.name} learned a new trick: {trick}! Happiness: {self.happiness}")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet!")

# Example usage
my_pet = Pet("Miles")
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("Runs in Circles")
my_pet.train("Fetch")
my_pet.show_tricks("hide and seek")
my_pet.get_status()