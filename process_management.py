from process import Process
from random import randint
import fcfs
import sjf

def manualProcessCreator(numberOfProcesses):
    processes = []
    for n in range(numberOfProcesses): 
        print("Insert the attributes of process ", n, ": ")
        at = int(input("Time of arrival: "))
        bt = int(input("Burst time: "))
        p = Process()
        p.arrivalTime = at
        p.pID = n
        p.burstTime = bt
        processes.append(p)
    return processes

def automaticProcessCreator(numberOfProcesses):
    processes = []
    for n in range(numberOfProcesses):
        p = Process()
        p.pID = n
        p.arrivalTime = n
        p.burstTime = randint(1, 50)
        processes.append(p)
    return processes

def calculateWaitTime(processes):
    processes[0].waitTime = 0
    Process.averageWaitTime = 0 #warning
    for i in range(1, len(processes)):
        processes[i].waitTime = processes[i - 1].waitTime + processes[i - 1].burstTime
        
        Process.averageWaitTime += processes[i].waitTime
    Process.averageWaitTime /= len(processes)
    return processes

def calculateTurnAroundTime(processes):
    Process.averageTurnAroundTime = 0
    for p in processes:
        p.turnAroundTime = p.waitTime + p.burstTime
        Process.averageTurnAroundTime += p.turnAroundTime
    Process.averageTurnAroundTime /= len(processes)
    return processes

def printProcesses(processes):
    print("PROCESS ID\tBURST TIME\tTIME OF ARRIVAL\tWAIT TIME\tTURNAROUND TIME")
    for p in processes:
          print(p.pID, "\t\t", p.burstTime, "\t\t", p.arrivalTime, "\t\t", p.waitTime, "\t\t", p.turnAroundTime)

    print("Average Waiting Time: ", Process.averageWaitTime, "\tAverage Turnaround Time: ", Process.averageTurnAroundTime)
    return

def calculate(processes, scheduling):
    if scheduling == 1:
        processes = fcfs.order(processes)
    elif scheduling == 2:
        processes = sjf.order(processes)
    processes = calculateWaitTime(processes)
    processes = calculateTurnAroundTime(processes)

    printProcesses(processes)
    return 
    
    