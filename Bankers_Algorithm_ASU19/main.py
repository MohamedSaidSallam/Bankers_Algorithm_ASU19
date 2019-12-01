def main(numOfProcess, numOfResources, available, allocation, maxResources):
    need = [[maxResources[i][j]-allocation[i][j] for j in range(numOfResources)] for i in range(numOfProcess)]
    currentAvailable = available.copy()
    finished = [False for i in range(numOfProcess)]

    canDoWork = True
    while canDoWork:
        canDoWork = False
        for i in range(numOfProcess):

            isNeedLowerThanCurrent = True
            for j in range(numOfResources):
                isNeedLowerThanCurrent = (need[i][j] < currentAvailable[j]) and isNeedLowerThanCurrent

            if not finished[i] and isNeedLowerThanCurrent:
                for j in range(numOfResources):
                    currentAvailable[j] += allocation[i][j]
                    finished[i] = True
                canDoWork = True

    safeState = True
    for isFinished in finished:
        safeState = isFinished and safeState

    print(safeState)