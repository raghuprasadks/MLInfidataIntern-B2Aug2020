# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:17:44 2020

@author: Sheshank
"""

import pandas as pd

results=pd.read_excel("results.xlsx")
print('results\n',results)

'''1.Adding another column sum'''

results["sum"]=results.sub1 + results.sub2 + results.sub3
print(results)


'''2.topper details'''

results.loc[results['sum'].idxmax()]


'''3.Topper details branches wise'''

cs_res=results[results.branch=='cs']
print(cs_res)
cs_res.loc[cs_res['sum'].idxmax()]

mech_res=results[results.branch =='mech']
print(mech_res)
mech_res.loc[mech_res["sum"].idxmax()]


#res=results.groupby('college')['sum'].agg('max')

res=results.groupby('college')['sum','name'].agg('max')
print(res)



'''4.Topper in respective colleges and branches '''


pes_res = results[(results.college=='pes') & (results.branch=='cs')]
print(pes_res)
pes_res.loc[pes_res["sum"].idxmax()]



rv_res = results[(results.college=='rv') & (results.branch=='cs')]
print(rv_res)
rv_res.loc[rv_res["sum"].idxmax()]


bmsit_res = results[(results.college=='bmsit') & (results.branch=='mech')]
print(bmsit_res)
bmsit_res.loc[bmsit_res["sum"].idxmax()]


msrit_res_res = results[(results.college=='msrit') & (results.branch=='mech')]
print(msrit_res)
msrit_res.loc[msrit_res["sum"].idxmax()]


'''5.Subject wise topper in respective colleges'''

'''pes college subject wise toppers'''

pes_res = results[(results.college=='pes')]
print(pes_res)
pes_res.loc[pes_res["sub1"].idxmax()]

pes_res = results[(results.college=='pes')]
print(pes_res)
pes_res.loc[pes_res["sub2"].idxmax()]

pes_res = results[(results.college=='pes')]
print(pes_res)
pes_res.loc[pes_res["sub3"].idxmax()]


'''rv college subject wise toppers'''

rv_res = results[(results.college=='rv')]
print(rv_res)
rv_res.loc[rv_res["sub1"].idxmax()]

rv_res = results[(results.college=='rv')]
print(rv_res)
rv_res.loc[rv_res["sub2"].idxmax()]

rv_res = results[(results.college=='rv')]
print(rv_res)
rv_res.loc[rv_res["sub3"].idxmax()]



'''bmsit college subject wise toppers'''

bmsit_res = results[(results.college=='bmsit')]
print(bmsit_res)
bmsit_res.loc[bmsit_res["sub1"].idxmax()]

bmsit_res = results[(results.college=='bmsit')]
print(bmsit_res)
bmsit_res.loc[bmsit_res["sub2"].idxmax()]

bmsit_res = results[(results.college=='bmsit')]
print(bmsit_res)
bmsit_res.loc[bmsit_res["sub3"].idxmax()]


'''msrit college subject wise toppers'''

msrit_res = results[(results.college=='msrit')]
print(msrit_res)
msrit_res.loc[msrit_res["sub1"].idxmax()]


msrit_res= results[(results.college=='msrit')]
print(msrit_res)
msrit_res.loc[msrit_res["sub2"].idxmax()]


msrit_res = results[(results.college=='msrit')]
print(msrit_res)
msrit_res.loc[msrit_res["sub3"].idxmax()]




'''6.Finding mean ,min,max and deviation of each subjects '''



results.sub1.mean()
results.sub1.min()
results.sub1.max()
results.sub1.std()


results.sub2.mean()
results.sub2.min()
results.sub2.max()
results.sub2.std()

results.sub3.mean()
results.sub3.min()
results.sub3.max()
results.sub3.std()

