def is_symmetric(string):
    stack = []
    matching_brackets = { ')': '(', ']': '[', '}': '{' }

    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"

def main():
    try:
        while True:
            input_string = input("Введіть рядок для перевірки симетричності дужок: ")
            result = is_symmetric(input_string)
            print(f"{input_string}: {result}")
    except (EOFError, KeyboardInterrupt):
        print()

if __name__ == "__main__":
    main()
