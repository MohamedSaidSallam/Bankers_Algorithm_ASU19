class NoSafeSeqFoundException(Exception):
    def __init__(self, processesFinished, availableResources):
        self.processesFinished = processesFinished
        self.availableResources = availableResources

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

def getSafeSeq(numOfProcess, numOfResources, available, allocation, maxResources):
    need = [[maxResources[i][j]-allocation[i][j] for j in range(numOfResources)] for i in range(numOfProcess)]
    currentAvailable = available.copy()
    finished = [False for i in range(numOfProcess)]
    SafeSeq = []

    availableIncreased = True
    while availableIncreased:
        availableIncreased = False
        for i in range(numOfProcess):
            if not finished[i] and isCurrentHigherThanNeed(currentAvailable, need[i]):
                for j in range(numOfResources):
                    currentAvailable[j] += allocation[i][j]
                finished[i] = True
                SafeSeq.append(i)
                availableIncreased = True
    if len(SafeSeq) == numOfProcess:
        return SafeSeq
    else:
        raise NoSafeSeqFoundException(SafeSeq, currentAvailable)
