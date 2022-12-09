def read_file_lines():
    with open("text.txt") as f:
        return [line.strip("\n") for line in f]


def main():
    for i, line in enumerate(read_file_lines(), start=1):
        if not line:
            print(f"{i} -> Пустий рядок")
        else:
            print("{} -> Слів: {} | Символів: {} | Символів (без пробілів): {}"
                  .format(i, len(line.split()), len(line), len(line.replace(" ", ""))))


if __name__ == "__main__":
    main()
