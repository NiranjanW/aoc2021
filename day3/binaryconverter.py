import argparse, readline


def binaryconverter(inp: str) -> int:
    num = 0
    for i in inp:
        num = 2 * num + int(i)
    return num


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", action="store_true", default=False)
    (args, rest) = parser.parse_args()
    if args.interactive:
        try:
            readline(args.interactive)
        except:
            pass
        rest += input("Arguments: ").split(" ")  # Get input args
        try:
            readline.write_history_file()
        except:
            pass
    # Your other script arguments go here
    parser.add_argument("-output-dir", default="/out")
    # ...
    args = parser.parse_args(rest)

    print(args)


if __name__ == "__main__":
    main()
