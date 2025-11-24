import csv
import os
from datetime import datetime

def record_patient_visit():
    filename = "patient_records.csv"
    
    
    file_exists = os.path.isfile(filename)

    print("--- new patient entry ---")
    
    
    pname = input("patient name: ")
    dname = input("doctor name: ")
    d = input("disease diagnosed: ")
    medi = input("medicines to take: ")
    note = input("other note or 'none': ")

    
    now = datetime.now()
    date = now.strftime("%d %B %Y")

    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
      
        if not file_exists:
            writer.writerow(["date", "patient Name", "doctor Name", "disease", "medicines", "notes"])
            
        
        writer.writerow([date, pname, dname, d, medi, note])



if __name__ == "__main__":
    while True:
        record_patient_visit()
        if input("Add another patient? (y/n): ").lower() != 'y':
            break

        