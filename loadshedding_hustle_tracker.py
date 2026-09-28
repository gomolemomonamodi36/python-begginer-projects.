# loadshedding_hustle_tracker.py
# By Gomolemo Monamodi - Pretoria
# Problem: Loadshedding kills my Cisco Python study time
# Solution: Track blackouts, costs, and find best hustle hours
# Data Science Essentials Project - May 2026

import csv
import os
from datetime import datetime

FILE = "hustle_log.csv"

def setup():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date","stage","hours_no_power","data_used_mb","battery_powerbank_used","what_i_was_doing","money_lost"])
        print(">> New hustle log created")

def log_day():
    print("\n--- LOG TODAY'S HUSTLE ---")
    date = input("Date [enter for today]: ") or datetime.now().strftime("%Y-%m-%d")
    stage = input("Loadshedding Stage (1-6): ")
    hours = float(input("Hours without power: "))
    data = float(input("Data used because WiFi dead (MB): "))
    battery = input("Powerbank % used (e.g. 40): ")
    doing = input("What were you trying to do? (study/coding/assignment): ")
    # Data in SA is expensive - R15 per 100MB is real
    money = (data / 100) * 15
    print(f"That blackout cost you ~ R{money:.2f} in data")

    with open(FILE, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([date, stage, hours, data, battery, doing, f"{money:.2f}"])
    print("Saved!")

def analyze_hustle():
    print("\n--- MY HUSTLE REPORT - GOD'S EYE FOR MY GRIND ---")
    try:
        with open(FILE, "r") as f:
            rows = list(csv.DictReader(f))
            if not rows:
                print("No logs yet")
                return

            total_hours = sum(float(r["hours_no_power"]) for r in rows)
            total_data = sum(float(r["data_used_mb"]) for r in rows)
            total_money = sum(float(r["money_lost"]) for r in rows)
            avg_stage = sum(int(r["stage"]) for r in rows) / len(rows)

            print(f"Days tracked: {len(rows)}")
            print(f"Total hours lost to loadshedding: {total_hours} hours")
            print(f"Total data wasted: {total_data} MB")
            print(f"Total money lost: R{total_money:.2f}")
            print(f"Average Stage: {avg_stage:.1f}")

            print("\n--- WHEN DO I LOSE MOST STUDY TIME? ---")
            study_losses = [r for r in rows if "study" in r["what_i_was_doing"] or "coding" in r["what_i_was_doing"]]
            if study_losses:
                worst = sorted(study_losses, key=lambda x: float(x["hours_no_power"]), reverse=True)[0]
                print(f"Worst day: {worst['date']} - Stage {worst['stage']} - Lost {worst['hours_no_power']}h while {worst['what_i_was_doing']}")

            print("\n--- MY HUSTLE PLAN ---")
            if avg_stage >= 4:
                print("Plan: Study 05:00-07:00 morning (before loadshedding), charge powerbank at campus")
            else:
                print("Plan: Study 18:00-20:00 evening - power more stable")

    except FileNotFoundError:
        print("Log file not found")

if __name__ == "__main__":
    setup()
    while True:
        print("\n1. Log blackout 2. See my hustle report 3. Exit")
        c = input("> ")
        if c == "1": log_day()
        elif c == "2": analyze_hustle()
        elif c == "3":
            print("Keep hustling Gomolemo - Eskom won't stop you")
            break
