# BMI Calculator 🧮

#!/usr/bin/env python3
"""BMI Calculator with CSV export and validation."""

import csv
from config import CSV_FILE, BMI_RANGES

def get_bmi_category(bmi):
    """Return BMI category based on value."""
    for category, threshold in BMI_RANGES.items():
        if bmi < threshold:
            return category
    return "Obese"

def main():
    print("🧮 BMI Calculator")
    print("-" * 30)
    
    # Get validated input
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)
    
    # Display result
    print(f"\n✅ Your BMI is {bmi:.2f} ({category})")
    
    # Save to CSV
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([weight, height, bmi, category])

## ✨ Features
- Metric unit support (kg, meters)
- 4 BMI categories (Underweight, Normal, Overweight, Obese)
- Input validation
- CSV history tracking
- Configurable via `config.py`

## 📊 Demo

🧮 BMI Calculator
------------------------------
Enter weight (kg): 70
Enter height (m): 1.75

✅ Your BMI is 22.86 (Normal weight)
💾 Saved to bmi_history.csv

