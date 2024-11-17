def calculate_sip(sip_amount, interest, years):
    monthly_rate = interest/12/100
    months = years*12
    return round(sip_amount * ((((1+monthly_rate)**(months)-1)*(1+monthly_rate)))/monthly_rate)