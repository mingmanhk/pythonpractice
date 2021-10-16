# employee_file = open("employee.txt", "a")
# r = read onlu
# w = write only
# r+ = read and write
# a= append
employee_file = open("employee.txt", "w")
employee_file.write("\nVictor - CEO")
employee_file.write("\nKelly - Customer Service")
employee_file.close()
