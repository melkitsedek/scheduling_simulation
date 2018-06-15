from process import Process
import process_management

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

if automaticFlag == 'M':
    print("\nSetup of processes...")    # Manual process creation... 
    processes = process_management.manualProcessCreator(numberOfProcesses)

else:
    print("\nSetting up processes...")  # Automatic and modern process creation!
    processes = process_management.automaticProcessCreator(numberOfProcesses)

print("Processes created! Calculating!")

process_management.calculate(processes, scheduling)

input("Press enter to continue...")
print("End of program.")
