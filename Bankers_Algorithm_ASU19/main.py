def allEqualTrue(inputList):
    for item in inputList:
        if not item:
            return False
    return True

def isCurrentHigherThanNeed(current, need):
    for j in range(len(need)):
        if need[j] > current[j]:
            return False
    return True

def isInSafeState(numOfProcess, numOfResources, available, allocation, maxResources):
    need = [[maxResources[i][j]-allocation[i][j] for j in range(numOfResources)] for i in range(numOfProcess)]
    currentAvailable = available.copy()
    finished = [False for i in range(numOfProcess)]

    availableIncreased = True
    while availableIncreased:
        availableIncreased = False
        for i in range(numOfProcess):
            if not finished[i] and isCurrentHigherThanNeed(currentAvailable, need[i]):
                for j in range(numOfResources):
                    currentAvailable[j] += allocation[i][j]
                finished[i] = True
                availableIncreased = True

    return allEqualTrue(finished)

def main(numOfProcess, numOfResources, available, allocation, maxResources):
    print(isInSafeState(numOfProcess, numOfResources, available, allocation, maxResources))