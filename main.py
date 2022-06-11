import funcs as f


schedule1, stats1, total_monthly1 = f.amortization_table(
    interest_rate = 2.1, 
    years = 30, 
    principal= 840000-195000, 
    yearly_tax= 4122, 
    maintenance_fee=300, 
    addl_principal=0)
print('*************************************************************************************************************')
print(stats1)
# print('Clean Mortgage: ', stats1.loc[0, 'Period_Payment'])
print('Total Monthly: ', total_monthly1)
# print(schedule1.iloc[-10:])