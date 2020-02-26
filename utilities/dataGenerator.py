import random, string


class DataGenerator:

    @staticmethod
    def generate_random_number_with_n_digits(n) -> int:
        lower = 10 ** (n - 1)
        upper = 10 ** n - 1
        return random.randint(lower, upper)

    @staticmethod
    def generate_random_string(length=10, chars=string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(length))