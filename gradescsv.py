# Student Grade Analyzer - Project 2 by Gomolemo
import csv

def analyze_grades(filename="grades.csv"):
    grades = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                grades.append(float(row[1]))
    except FileNotFoundError:
        # sample data if file not found
        grades = [65, 78, 82, 55, 90, 72]

    if not grades:
        return "No grades found"

    avg = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)
    pass_rate = len([g for g in grades if g >= 50]) / len(grades) * 100

    print(f"Total Students: {len(grades)}")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Pass Rate: {pass_rate:.1f}%")

analyze_grades()