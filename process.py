class Process(object):
    averageWaitTime = 0
    averageTurnAroundTime = 0

    def __init__(self):
        self.pID = 0
        self.burstTime = 0
        self.waitTime = 0
        self.turnAroundTime = 0
        self.arrivalTime = 0
        self.priority = 0
        self.remainingTime = 0
        self.timesOnReadyQueue = 0
