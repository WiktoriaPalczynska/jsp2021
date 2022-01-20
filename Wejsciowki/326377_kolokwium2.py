#326377 Wiktoria Pałczyńska 02.12.2021

a={'name:':'Wiktoria','number':'2'}
b={'index:':'326377','number':'3'}

def slowniki(d1,d2):
    d3=d1
    for key in d2:
        if key in d3:
            d3[key]=[d2[key],d3[key]]
        else:
            d3[key]=d2[key]
    return d3

print(slowniki(a,b))