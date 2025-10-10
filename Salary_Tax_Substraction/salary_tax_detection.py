# 💰 Salary Tax Calculator - Pakistan
# This program calculates net salary after tax deduction for filers and non-filers.


salary = float(input('Enter Your Salary:' ))#Take input from user for their salary and convert it to float
filer_nonfiler = input('Are You a Filer or Nonfiler?: ').strip().lower().replace('-','').replace(' ','') #Take input from user for filer or nonfiler and format it

if filer_nonfiler  == 'filer' :  #Check if user is a filer
    after_tax_salary = salary - (salary * 0.15)  #Calculate salary after 15% tax deduction
    tax_deducted = salary * 0.15  #Calculate tax deducted
    print(f'Your Salary after 15% tax deduction is:{after_tax_salary} and tax deducted is: {tax_deducted}')
elif filer_nonfiler == 'nonfiler':  #Check if user is a nonfiler
    after_tax_salary = salary - (salary * 0.20)  #Calculate salary after 20% tax deduction
    tax_deducted = salary * 0.20  #Calculate tax deducted
    print(f'Your Salary after 20% tax deduction is: {after_tax_salary} and tax deducted is: {tax_deducted}')
else:  #If user input is neither filer nor nonfiler
    print('Invalid Input')  #Print invalid input message