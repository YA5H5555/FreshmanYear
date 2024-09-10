def calculate_income(rate, period):
    return rate * period


def format_name(firstname, lastname):
    return lastname+', '+ firstname

def employee_info(firstname, lastname, department, email, rate, period):
    income = rate*period
    return f"{lastname}, {firstname}\n${income}\n{department}\n{email}"

def main():

    print(calculate_income(5000,12))
    print(format_name('Ruhil','Yash'))
    print(employee_info('Ruhil', 'Yash','Computer Science Lab', 'YRlab.edu',5000,12))

if __name__ == "__main__":
    main()
