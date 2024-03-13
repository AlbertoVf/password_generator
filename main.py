import argparse, subprocess
from src.Password import Password, CharType


def main():
    characters = []
    parser = argparse.ArgumentParser(description="Generate password")
    parser.add_argument( "-l", "--length", dest="l", required=True, type=int, help="Password's length" )
    parser.add_argument( "-a",'--alpha', action="store_true", help="Include lowercase character")
    parser.add_argument( "-A",'--ALPHA', action="store_true", help="Include Uppercase character")
    parser.add_argument( "-n",'--numbers', action="store_true", help="Include Numbers")
    parser.add_argument( "-s",'--special', action="store_true", help="Include Special characters")
    parser.add_argument( "-m",'--more', dest="m", required=False, type=int, help="Generate more passwords")

    args = parser.parse_args()
    if args.alpha: characters.append(CharType.LOWERCASE)
    if args.ALPHA: characters.append(CharType.UPPERCASE)
    if args.numbers: characters.append(CharType.NUMBERS)
    if args.special: characters.append(CharType.SPECIAL)

    p = Password(size=args.l, characters=characters)
    if args.m:
        p.more = args.m
        print(p.generate_more())
    else:
        print(p.generate())


main()
