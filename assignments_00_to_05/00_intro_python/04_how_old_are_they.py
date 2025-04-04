""""Write a program to solve this age-related riddle!
Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
1. Anton is 21 years old.
2. Beth is 6 years older than Anton.
3. Chen is 20 years older than Beth.
4. Drew is as old as Chen's age plus Anton's age.
5. Ethan is the same age as Chen."""

def main():
    ageOfAnton:int = 21
    ageOfBeth:int=ageOfAnton+6
    ageOfChen:int = ageOfAnton+20
    ageOfDrew:int=ageOfChen+ageOfAnton
    ageOfEthan:int=ageOfChen
    
    print(f"""Anton is {ageOfAnton} old
Beth is {ageOfBeth} old
Chen is {ageOfChen} old
Drew is {ageOfDrew} old
Ethan is {ageOfEthan} old""")



if __name__ == '__main__':
    main()    