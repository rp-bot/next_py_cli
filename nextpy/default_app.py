import argparse


def main():
    parser = argparse.ArgumentParser(description='A simple CLI program.')
    parser.add_argument('name', help='Your name')
    parser.add_argument('age', type=int, help='Your age')
    parser.add_argument(
        '-g', '--gender', choices=['male', 'female'], help='Your gender')
    args = parser.parse_args()
    print(f'Hello, {args.name}!')
    if args.age:
        print(f'You are {args.age} years old.')
    if args.gender:
        print(f'You are {args.gender}.')


if __name__ == '__main__':
    main()
