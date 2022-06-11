import funcs as f

ad_pr = 1000

schedule1, stats1, total_monthly1 = f.amortization_table(
    interest_rate = 1.54, 
    years = 30, 
    principal= 650000,
    yearly_tax= 3846, 
    maintenance_fee=85, 
    addl_principal=ad_pr)

schedule11, stats11, total_monthly11 = f.amortization_table(
    interest_rate = 3, 
    years = 27, 
    principal = schedule1.loc[36, 'Curr_Balance'], 
    yearly_tax= 3846, 
    maintenance_fee=85, 
    addl_principal=ad_pr)



schedule2, stats2, total_monthly2 = f.amortization_table(
    interest_rate = 2.1, 
    years = 30, 
    principal= 650000,
    yearly_tax= 3846, 
    maintenance_fee=85, 
    addl_principal=ad_pr)

schedule22, stats22, total_monthly22 = f.amortization_table(
    interest_rate = 3, 
    years = 25, 
    principal = schedule2.loc[60, 'Curr_Balance'], 
    yearly_tax= 3846, 
    maintenance_fee=85, 
    addl_principal=ad_pr)


print(schedule1.loc[36, 'Cum_Interest'] + schedule11.loc[84, 'Cum_Interest'])
print(schedule2.loc[60, 'Cum_Interest'] + schedule22.loc[60, 'Cum_Interest'])

# print(schedule1)
# print(schedule11)


# print(schedule2)
# print(schedule22)


