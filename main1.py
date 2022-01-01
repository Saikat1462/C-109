import random as r
import plotly.figure_factory as px
diceresult=[]
count=[]
for i in range(0,100):
    d1=r.randint(1,6)
    d2=r.randint(1,6)
    diceresult.append(d1+d2)
    count.append(i)
print(diceresult)
fig=px.create_distplot([diceresult],["result"])
fig.show()