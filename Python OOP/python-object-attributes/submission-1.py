class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
hunger = whiskers.hunger - 3
#  - Increase energy by 2
energy = whiskers.energy + 2
# TODO: Print Whiskers' modified attributes
print("Initial Attributes: Whiskers (cat) - Hunger: 6, Energy: 8")

print(f"Modified Attributes: Whiskers (cat) - Hunger: {hunger}, Energy: {energy}")