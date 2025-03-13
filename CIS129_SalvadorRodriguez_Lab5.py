# Part 2 - Repetition Structures Pseudocode

# Test

# Step 1 Define Variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0.0
keepGoing = "y"

# Step 3 Loop to run program again
while keepGoing.lower() == "y":

    # Step 4

    # getBottles code
    NBR_OF_DAYS = 7
    # Declare and initialize totalBottles, todayBottles, counter to 0
    totalBottles = 0
    todayBottles = 0
    counter = 0

    while counter < NBR_OF_DAYS:
        print("Enter number of bottles returned for day #", counter + 1, ":")
        todayBottles = int(input())
        totalBottles = totalBottles + todayBottles
        counter = counter + 1

    # Step 5

    # calcPayout code
    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

    # Step 6

    # printInfo code
    print("Total number of bottles collected: " + str(totalBottles))
    print("Total payout: $" + str(totalPayout))

    # Ask if the user wants to run the program again
    keepGoing = input("Do you want to run the program again? (Enter y for yes): ")
