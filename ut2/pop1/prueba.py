daughter_age = 35
mother_age = 15
target_mother_age = 0
target_daughter_age = 0


for i in range(daughter_age, mother_age):
        mother_age += 1
        daughter_age += 1
        if mother_age == daughter_age * 2:
            target_mother_age = mother_age
            target_daughter_age = daughter_age
        print(target_mother_age, target_daughter_age)