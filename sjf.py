from process import Process
from operator import attrgetter

def order(processes): #by burst time
    processes.sort(key = attrgetter("burstTime"))
    return processes
