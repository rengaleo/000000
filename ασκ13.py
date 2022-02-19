from urllib.request import Request, urlopen
import json

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

print(data)
x= json.loads(data)
print(x)

last_round = x["round"]

for round in range(last_round, last_round-100, -1):
    req= Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data= urlopen(req).read()
    x=json.loads(data)
    randomness= x["randomness"]

base_16 = int(randomness,16)
binary = bin(base_16)
print(binary)
    
new_list= list(binary)
print(new_list)


pl0 = 0
pl1 = 0

for i in range(len(new_list)):
    if i == 0:
        max0 = pl0
        max1 = pl1
    if new_list[i] == '0':
        pl0 = pl0 +1
        pl1 = 0
        if pl0 > max0:
            max0 = pl0
    if new_list[i] == '1':
        pl0 =0
        pl1 = pl1+1
        if pl1 > max1 :
            max1 = pl1


print ("Max number of 0 sequence:", max0)
print ("Max number of 1 sequence:", max1)