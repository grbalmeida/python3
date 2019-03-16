def salary_with_discounted_tax(salary, tax = 27):
    return salary - salary * tax * 0.01

print(salary_with_discounted_tax(5000)) # 3650.00