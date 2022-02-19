from scipy.stats import entropy as en
from urllib.request import Request, urlopen
import pandas as pd
sum=0
print("Results of last 20 rounds:")
for bhma in range(1,21):
    req = Request('https://drand.cloudflare.com/public/'+str(bhma), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    txt=str(data)
    t1=txt.split('"randomness":',1)
    t2=str(t1[1])
    t3=t2.split(",",1)
    t4=int((t3[0][-65:-1]),16)
    print("For round number"+str(bhma))
    print("RANDOMNESS numbers:",t3[0][-65:-1])
    print("Int part:",t4)
    print("HEX:",hex(t4))  
    t4=pd.Series(t4)
    data=t4.value_counts()
    print(en(data))
    print("End")