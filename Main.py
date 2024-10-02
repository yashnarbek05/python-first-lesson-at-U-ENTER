def main():
    a = "yes"
    while (a != "no" and a == "yes"):
        print("1-sonni kriting: ")
        n1 = input()
        print("ishorani kriting: ")
        ish = input()
        print("2-sonni kriting: ")
        n2 = input()
        if ish == '+':
            res = (int(n1) + int(n2))
            print("n1 " + ish + " n2 = ", res)
        if ish == '-':
            print("n1 " + ish + " n2 = ", (int(n1) - int(n2)))
        if ish == '*':
            print("n1 " + ish + " n2 = ", (int(n1) * int(n2)))
        if ish == '/':
            print("n1 " + ish + " n2 = ", (int(n1) / int(n2)))

        print("Do you wanna continue?")
        a = input()


if __name__ == "__main__":
    main()