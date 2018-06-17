from process import Process
from operator import attrgetter

def calculateByRemainingTimePreemption(processes):
    toCalculate = processes
    aux = []
    processes = []

        

    return processes

def order(processes):
    processes.sort(key = attrgetter("arrivalTime"))
    
    processes = calculateByRemainingTimePreemption(processes)

    return processes
