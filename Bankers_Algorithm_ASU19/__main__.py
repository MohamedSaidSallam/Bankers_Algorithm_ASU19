from Bankers_Algorithm_ASU19.main import getSafeSeq

numOfProcess = int(input("Number Of Process ? "))
numOfResources = int(input("Number Of Resources ? "))

available = [int(k) for k in input("Available Resources ? ").split()]
print("Allocation:")
allocation = [[int(k) for k in input().split()] for i in range(numOfProcess)]
print("Max:")
maxResources = [[int(k) for k in input().split()] for i in range(numOfProcess)]

print(getSafeSeq(numOfProcess, numOfResources, available, allocation, maxResources))
