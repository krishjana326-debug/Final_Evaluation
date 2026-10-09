def calculate_result(marks):
    """Return the total and average of the given marks."""
    total = sum(marks)
    average = total / len(marks)
    return total, average


def main():
    name = input("Enter student's name: ")

    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks of subject {i}: "))
        marks.append(mark)

    total, average = calculate_result(marks)

    print("\n--- Student Result ---")
    print("Name    :", name)
    print("Marks   :", marks)
    print("Total   :", total)
    print("Average :", round(average, 2))

    if average >= 40:
        print("Result  : Pass")
    else:
        print("Result  : Fail")


main()