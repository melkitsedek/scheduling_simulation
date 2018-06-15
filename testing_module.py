import process_management
from process import Process

Process.averageWaitTime = 8
Process.averageTurnAroundTime = 5
processes = process_management.automaticProcessCreator(10)

process_management.calculate(processes, 1)