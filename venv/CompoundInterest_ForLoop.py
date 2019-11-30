yearly_installment = float(input("Enter the yearly installment you wish to invest: $"))
term = int(input("Enter the term period in years: "))

# The interest rate will vary depending on the  term lenght.
if term<10:
    interest_rate= 0.08
elif term>=10 and term<=20:
    interest_rate= 0.10
else:
    interest_rate= 0.12

total_money = 0

print("C.I. rate= {}%".format((interest_rate*100)))

for i in range(term):
    total_money= total_money+(total_money + yearly_installment)*interest_rate

print("Total return after {} years = ${:.2f}".format(term, total_money))
# In the above line, we used '{:.2f}' to fix the decimal places in the floating point value to 2 decimal places.