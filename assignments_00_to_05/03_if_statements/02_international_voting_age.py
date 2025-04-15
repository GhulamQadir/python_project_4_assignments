Age_In_Peturksbouipo: int = 16
Age_In_Stanlau: int = 25
Age_In_Mayengua: int = 48


def main():
    userAge: int = int(input("Enter your age:\t"))
    if userAge < 16:
        print("You can't vote in any country")
    elif userAge >= 16 and userAge < 25:
        print(
            "You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48."
        )
    elif userAge >= 25 and userAge < 48:
        print(
            "You can vote in Peturksbouipo and Stanlau where the voting age is 16 and 25. You cannot vote in Mayengua where the voting age is 48."
        )
    else:
        print("You can vote in Peturksbouipo, Stanlau and Mayengua.")


if __name__ == "__main__":
    main()
