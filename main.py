import csv

#print csv file
with open(r"C:\Users\dhars\analize-csv\std_data.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    print("\nstd_data")
    for row in csv_reader:
        print(row)
  


# print first and last three rows        
with open(r"C:\Users\dhars\analize-csv\std_data.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    
    rows = list(csv_reader)

    print("First three rows:")
    for row in rows[:3]:
        print(row)
    
    print("\nLast three rows:")
    for row in rows[-3:]:
        print(row)
        

#print total and average
#print who are between 60 to 80
# who are below 60
with open(
    r"C:\Users\dhars\analize-csv\std_data.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print(f"{'Name':<15}{'Total':<10}{'Average':<10}{'Status'}")
    print("-" * 45)
    
    topper_count = 0
    medium_count = 0
    failer_count = 0

    for row in csv_reader:
            name = row[0]
            marks = [int(mark) for mark in row[1:]]
            if not marks:
                print(f"invalied data.")

            total_marks = sum(marks)
            average_marks = total_marks / len(marks)

            if average_marks >= 80:
                status = "Topper"
                topper_count += 1
            elif average_marks >= 60:
                status = "Medium"
                medium_count += 1
            else:
                status = "Failer"
                failer_count += 1

            print(f"{name:<15}{total_marks:<10}{average_marks:<10.2f}{status}")
    print("\nstudent category count(toper,medium,failer)")
    print(f"Topper Count: {topper_count}")
    print(f"Medium Count: {medium_count}")
    print(f"Failer Count: {failer_count}")
