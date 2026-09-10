def berkeley_algorithm(clocks):
    print("\n========== BEFORE SYNCHRONIZATION ==========")

    for i in range(len(clocks)):
        print("Process", i + 1, "Clock:", clocks[i])

    # Process 1 acts as the master
    master_clock = clocks[0]

    print("\nMaster Clock:", master_clock)

    # Calculate clock offsets
    offsets = []

    for clock in clocks:
        offset = clock - master_clock
        offsets.append(offset)

    print("\n========== CLOCK OFFSETS ==========")

    for i in range(len(offsets)):
        print("Process", i + 1, "Offset:", offsets[i])

    # Calculate average offset
    average_offset = sum(offsets) / len(offsets)

    print("\nAverage Offset:", round(average_offset, 2))

    # Synchronize all clocks
    synchronized_clocks = []

    for clock in clocks:
        correction = average_offset - (clock - master_clock)
        new_clock = clock + correction
        synchronized_clocks.append(new_clock)

    print("\n========== CLOCK CORRECTIONS ==========")

    for i in range(len(clocks)):
        correction = synchronized_clocks[i] - clocks[i]

        print(
            "Process", i + 1,
            "Correction:", round(correction, 2)
        )

    print("\n========== AFTER SYNCHRONIZATION ==========")

    for i in range(len(synchronized_clocks)):
        print(
            "Process", i + 1,
            "Clock:",
            round(synchronized_clocks[i], 2)
        )

    return synchronized_clocks


# ==========================================
# MAIN PROGRAM
# ==========================================

print("============================================")
print("   BERKELEY CLOCK SYNCHRONIZATION SIMULATOR")
print("============================================")

# Get number of processes
n = int(input("\nEnter number of processes: "))

clocks = []

# Get clock values
print("\nEnter clock values for each process:")

for i in range(n):
    clock = float(
        input("Process " + str(i + 1) + " clock: ")
    )

    clocks.append(clock)

# Run Berkeley Algorithm
berkeley_algorithm(clocks)

print("\n============================================")
print("Synchronization Completed Successfully!")
print("============================================")

