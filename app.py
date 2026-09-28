# Pitori Traffic Eye - by Gomolemo Monamodi
# Built because Google Maps doesn't know about loadshedding & taxi madness
# May 2026 - Pretoria to JHB
# Simple version, no fancy stuff yet

from flask import Flask, render_template_string, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)

DB_FILE = "traffic_reports.csv"

# create file if not there
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "location", "issue", "traffic_level", "reported_by"])
        writer.writerow(["2026-05-18 07:30", "N1 Allandale", "Robots off - Stage 4", "9", "Gomolemo"])
        writer.writerow(["2026-05-18 07:45", "Old Pretoria Road", "Clear, taxis moving", "3", "Thabo"])

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pitori Traffic Eye</title>
    <style>
        body
