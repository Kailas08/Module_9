import random

class NumberTooLowError(Exception):
    """Исключение, когда число слишком маленькое"""
    pass

class NumberTooHighError(Exception):
    """Исключение, когда число слишком большое"""
    pass

class GameWonError(Exception):
    """Исключение, когда игрок угадал число"""
    pass

class AttemptsExhaustedError(Exception):
    """Исключение, когда закончились попытки"""
    pass

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас есть {max_attempts} попыток, чтобы угадать число от 1 до 100.")

    while True:
        try:
            attempts += 1
            if attempts > max_attempts:
                raise AttemptsExhaustedError

            guess = int(input("Введите ваше предположение: "))

            if guess < secret_number:
                raise NumberTooLowError
            elif guess > secret_number:
                raise NumberTooHighError
            else:
                raise GameWonError

        except ValueError:
            print("Пожалуйста, введите целое число.")
        except NumberTooLowError:
            print("Слишком низко! Попробуйте число побольше.")
        except NumberTooHighError:
            print("Слишком высоко! Попробуйте число поменьше.")
        except GameWonError:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток!")
            break
        except AttemptsExhaustedError:
            print(f"Игра окончена. Вы исчерпали все {max_attempts} попыток.")
            print(f"Загаданное число было: {secret_number}")
            break

if __name__ == "__main__":
    guess_number()