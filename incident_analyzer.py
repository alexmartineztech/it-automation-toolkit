import csv
from collections import Counter

def analyze_tickets(file):
    issues = []

    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            issues.append(row['issue'])

    counter = Counter(issues)
    print("Most common issues:")
    for issue, count in counter.items():
        print(f"{issue}: {count}")

if __name__ == "__main__":
    analyze_tickets("tickets.csv")
