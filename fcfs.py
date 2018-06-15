from process import Process
from operator import attrgetter

def order(processes): #by arrival time
    processes.sort(key = attrgetter("arrivalTime"))
    return processes
