import string, random


class CharType:
    LOWERCASE = "lowercase"
    UPPERCASE = "uppercase"
    NUMBERS = "numbers"
    SPECIAL = "special"


class Password:
    __VALUES = {
        CharType.LOWERCASE: string.ascii_lowercase,
        CharType.UPPERCASE: string.ascii_uppercase,
        CharType.NUMBERS: string.digits,
        CharType.SPECIAL: " " + string.punctuation,
    }

    def __init__(self, size: int, characters: list[CharType], more: int = 1) -> None:
        self.size = size
        self._types = characters
        self.characters = "".join([self.__VALUES.get(i) for i in characters])
        self.more = more

    def values(self):
        return self.__VALUES

    def generate(self) -> str:
        password = ""
        for i in range(self.size):
            r = random.randint(0, len(self.characters) - 1)
            password += self.characters[r]
        return password

    def generate_more(self):
        p = [self.generate() for i in range(self.more)]
        return "\n".join(p)

    def write_in_file(self):
        filename = f"passwords_{self.more}x{self.size}_{'+'.join(self._types)}.txt"
        with open(filename, "w") as f:
            f.writelines(self.generate_more())
        print(f"Password save in {filename}")
