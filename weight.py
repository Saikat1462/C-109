import pandas as p
import plotly.figure_factory as ff
import statistics

df=p.read_csv("data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].to_list()],["weight"],show_curve=False)
fig.show()

weight=df["Weight(Pounds)"].to_list()
weightmean=statistics.mean(weight)
weightmedian=statistics.median(weight)
weightmode=statistics.mode(weight)
weightstd=statistics.stdev(weight)
print("Mean,Median and Mode of weight is {},{} and {}".format(weightmean,weightmedian,weightmode))
print("Standard Deviation of weight is {}".format(weightstd))

weight1stdstart,weight1stdend=weightmean-weightstd,weightmean+weightstd
print(weight1stdstart,weight1stdend)
weight2stdstart,weight2stdend=weightmean-(weightstd*2),weightmean+(weightstd*2)
print(weight2stdstart,weight2stdend)
weight3stdstart,weight3stdend=weightmean-(weightstd*3),weightmean+(weightstd*3)
print(weight3stdstart,weight3stdend)

wstdp1st=[w for w in weight if w > weight1stdstart and w < weight1stdend]
wstdp2nd=[w for w in weight if w > weight2stdstart and w < weight2stdend]
wstdp3rd=[w for w in weight if w > weight3stdstart and w < weight3stdend]
print("{}% of data lies within 1st standard deviation".format(len(wstdp1st)*100.0/len(weight)))
print("{}% of data lies within 2nd standard deviation".format(len(wstdp2nd)*100.0/len(weight)))
print("{}% of data lies within 3rd standard deviation".format(len(wstdp3rd)*100.0/len(weight)))