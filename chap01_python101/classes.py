class Dog:
    def __init__(self, name: str, m: int, d: int, y: int, bark: str):
        self.name = name
        self.month = m
        self.day = d
        self.year = y
        self.bark = bark

    def __add__(self, other_dog):
        return Dog(
            name=f"Puppy of {self.name} and {other_dog.name}",
            m=self.month,
            d=self.day,
            y=self.year + 1,
            bark=f"{self.bark} {other_dog.bark}",
        )

    def speak(self) -> str:
        return f"{self.bark}"

    def change_bark(self, new_bark: str) -> str:
        self.bark = new_bark
        return self.speak()

    def birth_date(self) -> str:
        return f"Birth date: {self.year}/{self.month}/{self.day}"


boy_dog = Dog(name="Mesa", m=10, d=1, y=2009, bark="woof!")
girl_dog = Dog(name="Sequoia", m=2, d=20, y=2010, bark="meow~")

boy_dog.change_bark("yay!")
assert boy_dog.speak() == "yay!"
assert boy_dog.birth_date() == "Birth date: 2009/10/1"

puppy = boy_dog + girl_dog
puppy.change_bark("yeeee")
assert puppy.speak() == "yeeee"
assert puppy.birth_date() == "Birth date: 2010/10/1"
