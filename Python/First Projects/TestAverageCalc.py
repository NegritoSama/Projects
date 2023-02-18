#Empty list to archive users scores/potential scores
earnedPoints = []
potentialScore = []
num = 1

#Gets how many test the user took
totalTest = int(input("How many test did you take?: "))

#Collects the score earned and potential score from user
for i in range(totalTest):
    pointsEarned = int(input(f"\nPlease enter points earned in test #{num}: "))
    potentialPoints = int(input(f"Please enter total potential points of test #{num}: "))
    potentialScore.append(potentialPoints)
    earnedPoints.append(pointsEarned)
    num += 1

#Calulates what the average score is from the user tests
totalEarned = sum(earnedPoints)
totalPotential = sum(potentialScore)
grade = totalEarned / totalPotential * 100

#Prints out the average of the user's test scores
print(f"\nYour average grade for {totalTest} test is {round(grade)}")