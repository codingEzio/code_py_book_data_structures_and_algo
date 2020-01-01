class Dog:
    def __init__(self, name: str, m: int, d: int, y: int, bark: str):
        self.name = name
        self.month = m
        self.day = d
        self.year = y
        self.bark = bark

    def speak(self) -> str:
        return f"{self.bark}"

    def change_bark(self, new_bark: str) -> str:
        self.bark = new_bark
        return self.speak()

    def birth_date(self) -> str:
        return f"Birth date: {self.year}/{self.month}/{self.day}"


boy_dog = Dog(name="Mesa", m=10, d=1, y=2009, bark="woof!")

boy_dog.change_bark("yay!")
print(boy_dog.speak())
print(boy_dog.birth_date())
