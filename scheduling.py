from process import Process
from random import randint
from operator import attrgetter

averageWaitTime = 0
averageTurnAroundTime = 0

def manualProcessCreator(n, bt, at):
    p = Process()
    p.arrivalTime = at
    p.pID = n
    p.burstTime = bt
    processes.append(p)
    return

def automaticProcessCreator(n):
    p = Process()
    p.pID = n
    p.arrivalTime = n
    p.burstTime = randint(1, 50)
    processes.append(p)
    return

def orderByArrivalTime():
    processes.sort(key = attrgetter("arrivalTime"))
    return

def orderByBurstTime():
    processes.sort(key = attrgetter("burstTime"))

def calculateWaitTime():
    processes[0].waitTime = 0
    global averageWaitTime
    for i in range(1, numberOfProcesses):
        processes[i].waitTime = processes[i - 1].waitTime + processes[i - 1].burstTime
        
        averageWaitTime += processes[i].waitTime
    return

def calculateTurnAroundTime():
    global averageTurnAroundTime
    for p in processes:
        p.turnAroundTime = p.waitTime + p.burstTime
        averageTurnAroundTime += p.turnAroundTime
    return

def printProcesses():
    print("PROCESS ID\tBURST TIME\tTIME OF ARRIVAL\tWAIT TIME\tTURNAROUND TIME")
    for p in processes:
          print(p.pID, "\t\t", p.burstTime, "\t\t", p.arrivalTime, "\t\t", p.waitTime, "\t\t", p.turnAroundTime)
    return

def calculateProcessesFCFS():
    orderByArrivalTime()
    calculateWaitTime()
    calculateTurnAroundTime()
    printProcesses()

def calculateProcessesSJF():
    orderByBurstTime()
    calculateWaitTime()
    calculateTurnAroundTime()
    printProcesses()

print("""Welcome to the scheduling simulation.

Available scheduling options:
    - (1)First Come First Serve;
    - (2)Shortest Job First;
    """)
scheduling = int(input("Please, select one by the number: "))


while True:
    if scheduling == 1:
        print("First Come First Serve selected!\n")
        break
    elif scheduling == 2:
        print("Shortest Job First selected!\n")
        break
    else:
        print("Invalid option.")
        print("""
        Available scheduling options:
            - (1)First Come First Serve;
            - (2)Shortest Job First;
            """)
        scheduling = int(input("Please, select one by the number: "))

numberOfProcesses = int(input("Insert the number of processes: "))

automaticFlag = input(
"""\nThis program supports automatic set of processes.
If you want to insert them manually, insert (M).
Otherwise, leave it blank.
Input: """)

processes = []
averageWaitTime = 0
averageTurnAroundTime = 0

if automaticFlag == 'M':
    print("\nSetup of processes...")
    for n in range(numberOfProcesses):
        print("Insert the attributes of process ", n, ": ")
        at = int(input("Time of arrival: "))
        bt = int(input("Burst time: "))
        manualProcessCreator(n, bt, at)

else:
    print("\nSetting up processes...")
    for n in range(numberOfProcesses):
        automaticProcessCreator(n)

print("Processes created! Calculating!")
if scheduling == 1:
    calculateProcessesFCFS()
elif scheduling == 2:
    calculateProcessesSJF()

print("""
Average Wait Time: """, averageWaitTime/numberOfProcesses, """
Average Turnaround Time: """, averageTurnAroundTime/numberOfProcesses)

input("Press enter to continue...")
print("End of program.")
