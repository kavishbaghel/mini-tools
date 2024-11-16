def calculate_sip(sip_amount, interest, years):
    monthly_rate = interest/12/100
    months = years*12
    return round(sip_amount * ((((1+monthly_rate)**(months)-1)*(1+monthly_rate)))/monthly_rate)

sip_amount = float(input("Enter SIP Amount: "))
interest = float(input("Enter rate of interest: "))
years = int(input("Enter number of years: "))
val = calculate_sip(sip_amount, interest, years)
print(f"Your sip of rupees {sip_amount} after {years} years will have a value of {val}")