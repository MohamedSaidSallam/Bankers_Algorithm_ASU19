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
    need = [
        [maxResources[i][j] - allocation[i][j] for j in range(numOfResources)]
        for i in range(numOfProcess)
    ]
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

def terminateProcess(HighestAllocation, allocation, available, maxResources):
    for i in range(len(allocation)):
        available[i] += allocation[HighestAllocation][i]
    del allocation[HighestAllocation]
    del maxResources[HighestAllocation]

def getHighestAllocation(allocation):
    HighestAllocation = 0
    HighestAllocationSum = sum(allocation[0])
    for i, alloc in enumerate(allocation):
        allocSum = sum(alloc)
        if allocSum > HighestAllocationSum:
            HighestAllocationSum = allocSum
            HighestAllocation = i
    return HighestAllocation

def handleDeadlock(numOfProcess, numOfResources, available, allocation, maxResources):
    processesTerminated = []
    inUnsafeState = True
    while inUnsafeState:
        try:
            getSafeSeq(
                numOfProcess, numOfResources, available, allocation, maxResources
            )
        except NoSafeSeqFoundException as ex:
            numOfProcess -= len(ex.processesFinished)
            allocation = [
                process
                for i, process in enumerate(allocation)
                if i not in ex.processesFinished
            ]
            maxResources = [
                process
                for i, process in enumerate(maxResources)
                if i not in ex.processesFinished
            ]
            available = ex.availableResources

            HighestAllocation = getHighestAllocation(allocation)

            processesTerminated.append(HighestAllocation)

            numOfProcess -= 1
            terminateProcess(HighestAllocation, allocation, available, maxResources)
        else:
            inUnsafeState = False
    return processesTerminated
