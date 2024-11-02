from collections import deque

def is_palindrome(input_string):
    clean_string = ''.join(input_string.split()).lower()
    char_deque = deque(clean_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    try:
        while True:
            input_string = input("Введіть рядок для перевірки на паліндром: ")
            if is_palindrome(input_string):
                print("Рядок є паліндромом.")
            else:
                print("Рядок не є паліндромом.")
    except (EOFError, KeyboardInterrupt):
        print()

if __name__ == "__main__":
    main()
