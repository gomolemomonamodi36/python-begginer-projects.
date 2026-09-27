# gauteng_traffic_tracker.py
# By Gomolemo Monamodi - Johannesburg / Pretoria Route
# Concept: My own version of God's Eye but for MY daily commute - no tracking other people
# Data Science Essentials - May 2026

import csv
from datetime import datetime
import os

# I log this manually everyday after my trip - real life data
# Format: date, from, to, departure_time, arrival_time, taxi_fare, traffic_level, notes

trip_log_file = "my_trips.csv"

def init_file():
    if not os.path.exists(trip_log_file):
        with open(trip_log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date","from","to","depart","arrive","fare","traffic","notes"])
        print("Created new log file")

def add_trip():
    print("\n--- LOG TODAY'S TRIP ---")
    date = input("Date (today) [press enter for today]: ") or datetime.now().strftime("%Y-%m-%d")
    from_place = input("From (e.g. Pretoria Bosman): ")
    to_place = input("To (e.g. JHB MTN): ")
    depart = input("Depart time (e.g. 06:30): ")
    arrive = input("Arrive time (e.g. 07:45): ")
    fare = input("Taxi fare R: ")
    traffic = input("Traffic 1-10 (1=no traffic, 10=standstill): ")
    notes = input("Notes (roadblock/police/accident): ")

    with open(trip_log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, from_place, to_place, depart, arrive, fare, traffic, notes])
    print("Trip saved!")

def analyze():
    print("\n--- MY TRAFFIC ANALYSIS (GOD'S EYE FOR MY ROUTE) ---")
    try:
        with open(trip_log_file, "r") as f:
            reader = list(csv.DictReader(f))
            if not reader:
                print("No trips yet - log some first")
                return

            total_fare = sum(float(r["fare"]) for r in reader)
            avg_traffic = sum(int(r["traffic"]) for r in reader) / len(reader)

            print(f"Total trips logged: {len(reader)}")
            print(f"Total spent on taxi: R{total_fare}")
            print(f"Average traffic level: {avg_traffic:.1f}/10")

            # find best time
            print("\nBest times to travel (lowest traffic):")
            sorted_trips = sorted(reader, key=lambda x: int(x["traffic"]))
            for t in sorted_trips[:3]:
                print(f" {t['date']} - Depart {t['depart']} - Traffic {t['traffic']}/10 - {t['notes']}")

            # roadblocks
            blocks = [r for r in reader if "roadblock" in r["notes"].lower() or "police" in r["notes"].lower()]
            if blocks:
                print(f"\nPolice/Roadblocks encountered: {len(blocks)} times")
                for b in blocks:
                    print(f"  {b['date']} at {b['from']} -> {b['to']}")

    except FileNotFoundError:
        print("No data yet - add trips first")

def menu():
    init_file()
    while True:
        print("\n1. Add trip  2. Analyze traffic  3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_trip()
        elif choice == "2":
            analyze()
        elif choice == "3":
            print("Sharp Gomolemo - stay safe on the road!")
            break
        else:
            print("1, 2 or 3 only")

if __name__ == "__main__":
    menu()