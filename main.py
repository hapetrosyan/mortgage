import funcs as f


schedule1, stats1, total_monthly1 = f.amortization_table(
    interest_rate = 1.6, 
    years = 25, 
    principal= 685000-220000, 
    yearly_tax=2000, 
    maintenance_fee=600, 
    addl_principal=0)
print('*************************************************************************************************************')
print(stats1)
# print('Clean Mortgage: ', stats1.loc[0, 'Period_Payment'])
print('Total Monthly: ', total_monthly1)
# print(schedule1.iloc[55:65])