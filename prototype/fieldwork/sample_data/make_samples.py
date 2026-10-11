"""Generate SYNTHETIC sample exports for tests and local dry runs only.

These files are not evidence of anything and must never be shown as a customer
result. Demo proof comes from a real organization's own export.

Usage: python sample_data/make_samples.py
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST = ["Ava", "Ben", "Cara", "Dev", "Eli", "Fay", "Gus", "Hana", "Ivan", "Jo", "Kai", "Lena", "Max", "Nia", "Omar",
         "Pia", "Quinn", "Rosa", "Sam", "Tara", "Uma", "Vik", "Wes", "Xia", "Yusuf", "Zoe"]
LAST = ["Smith", "Patel", "Garcia", "Kim", "Nguyen", "Brown", "Lee", "Shah", "Lopez", "Miller"]


def donors(path: Path, seed: int = 7, as_of: datetime = datetime(2026, 9, 30)) -> None:
    rng = random.Random(seed)
    rows = []
    for i in range(160):
        acct = 1000 + i
        name = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
        base = rng.choice([25, 50, 50, 100, 100, 250, 500, 1000])
        start = as_of - timedelta(days=rng.randint(30, 3 * 365))
        lapse_after = rng.random() < 0.55  # most donors stop giving at some point
        d = start
        while d <= as_of:
            rows.append({"Account Number": acct, "Full Name": name, "Primary Email": f"donor{acct}@example.org",
                         "Date": d.strftime("%m/%d/%Y"), "Amount": f"${base * rng.uniform(0.8, 1.6):,.2f}"})
            d += timedelta(days=rng.choice([30, 90, 180, 365, 365, 400]))
            if lapse_after and rng.random() < 0.45:
                break
    rows.sort(key=lambda r: datetime.strptime(r["Date"], "%m/%d/%Y"))
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def square(path: Path, seed: int = 11, as_of: datetime = datetime(2026, 10, 4)) -> None:
    rng = random.Random(seed)
    menu = {"Latte": ("Coffee", 5.25), "Cold Brew": ("Coffee", 4.75), "Drip Coffee": ("Coffee", 2.95),
            "Chai Latte": ("Tea", 5.0), "Matcha": ("Tea", 5.75), "Croissant": ("Bakery", 3.75),
            "Bagel": ("Bakery", 3.25), "Breakfast Sandwich": ("Food", 8.5), "Avocado Toast": ("Food", 9.25),
            "Lavender Scone": ("Bakery", 3.95), "Hot Chocolate": ("Coffee", 4.25), "Seasonal Soup": ("Food", 6.5)}
    weights = [30, 18, 22, 8, 6, 14, 9, 12, 7, 2, 4, 2]
    rows, tid = [], 50000
    day = as_of - timedelta(days=112)
    while day <= as_of:
        n_orders = int({0: 70, 1: 60, 2: 62, 3: 66, 4: 85, 5: 110, 6: 95}[day.weekday()] * rng.uniform(0.85, 1.1))
        for _ in range(n_orders):
            tid += 1
            hour = rng.choices(range(7, 18), weights=[8, 14, 12, 9, 8, 9, 7, 5, 4, 3, 2])[0]
            cust = f"C{rng.randint(1, 900)}" if rng.random() < 0.4 else ""
            for item in set(rng.choices(list(menu), weights=weights, k=rng.choice([1, 1, 2, 2, 3]))):
                cat, price = menu[item]
                qty = 1
                rows.append({"Date": day.strftime("%Y-%m-%d"), "Time": f"{hour:02d}:{rng.randint(0, 59):02d}:00",
                             "Category": cat, "Item": item, "Qty": qty, "Gross Sales": f"${price * qty:.2f}",
                             "Net Sales": f"${price * qty:.2f}", "Transaction ID": f"T{tid}", "Customer ID": cust})
        day += timedelta(days=1)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    donors(HERE / "SYNTHETIC_bloomerang_transactions.csv")
    square(HERE / "SYNTHETIC_square_item_sales.csv")
    print("wrote synthetic samples to", HERE)
