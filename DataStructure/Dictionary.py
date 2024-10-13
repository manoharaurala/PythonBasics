holdings={"titan":410,"PFC":125,"DIVIS":20,"Zomatao":195}


titan_holding=holdings["titan"]
print(titan_holding)

print(holdings)
print("PFC" in holdings)
print("Castrol" in holdings)

print("keys: "+str(holdings.keys()))
for key in holdings:
    print("stock name: "+key+" Qty: "+str(holdings[key]))

print(holdings.items())

for stock,qty in holdings.items():
    print("stock name: " + stock + " Qty: " + str(qty))
