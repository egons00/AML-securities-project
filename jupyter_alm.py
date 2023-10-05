import pandas as pd

balance_data = pd.read_csv('balance_data.csv')
nsfr_haircut = pd.read_csv('nsfr_haircut.csv')

pd.options.display.float_format = '{:,.2f}'.format

def task_4(balance_data, nsfr_haircut):
    balance_data = balance_data.copy()
    nsfr_haircut = nsfr_haircut.copy()


    merged_data = pd.merge(balance_data, nsfr_haircut, how='inner', on=['BALANCE_GROUP', 'NSFR_GROUP', 'GAP'])

    merged_data['NSFR'] = merged_data['TOTAL_BALANCE_EUR'] / merged_data['NSFR_HAIRCUT']

 
    print('\n4. Task solution')
    print('\nCurrent NSFR is {:.2%}'.format(merged_data['NSFR'].mean()))
    print('!Your comment goes here!\n')

 
    balance_by_gap = merged_data.pivot_table(index=['NSFR_GROUP', 'BALANCE_GROUP'],
                                             columns='GAP',
                                             values='TOTAL_BALANCE_EUR',
                                             aggfunc='sum')

    weighted_haircuts = merged_data.pivot_table(index=['NSFR_GROUP', 'BALANCE_GROUP'],
                                                values='NSFR_HAIRCUT',
                                                aggfunc='mean')

    print('\nDaily balance by balance groups and time gaps:')
    display(balance_by_gap)

    print('\nWeighted NSFR haircuts by balance groups:')
    display(weighted_haircuts)

task_4(balance_data, nsfr_haircut)
