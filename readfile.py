employee_file = open("employee.txt", "r") #r = read onlu r+ = read and write a= append
# print(employee_file.readable())
# print(employee_file.readline())
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)
employee_file.close()
