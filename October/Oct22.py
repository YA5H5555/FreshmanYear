import csv

# Step 1
def file_addition(filename):
    total = 0
    with open(filename, "r") as file:
        for line in file:
            total += int(line.strip())
    return total

# Step 2
def line_counter(filename):
    with open(filename, "r") as file:
        return sum(1 for _ in file)

# Step 3
def csv_data(filename):
    count = 0
    max_row_length = 0
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            count += 1
            max_row_length = max(max_row_length, len(row))
    return count, max_row_length  # returns a tuple of the two values

# Step 4
def get_filtered_CSV(filename, filter_by):
    lst = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if filter_by in row:
                lst.append(row)
    return lst

# Step 5
def find_flight(filename, airlines, city, earliest, latest):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            flight_airline, flight_city, flight_time = row[0], row[1], row[2]
            if flight_airline == airlines and flight_city == city and earliest <= flight_time <= latest:
                return row
    

# Add your own tests to this method
def run():
    print(file_addition("num.txt"))
    print(line_counter("harryPotter.txt"))
    print(csv_data("myfile.csv"))
    print(get_filtered_CSV("Airport.csv", "United"))
    print(find_flight("Airport.csv", "United", "Portland", "0000", "2400"))

if __name__ == '__main__':
    print()
    run()