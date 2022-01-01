import pandas as p
import plotly.figure_factory as ff
import csv
import statistics
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["Height(Inches)"].to_list()],["height"],show_hist=False)
fig.show()

#doing the statical calculation
height=df["Height(Inches)"].to_list()
heightmean=statistics.mean(height)
heightmode=statistics.mode(height)
heightmedian=statistics.median(height)
heightstd=statistics.stdev(height)
print("mean,median and mode of height is {},{} and {}".format(heightmean,heightmedian,heightmode))
print("standard deviation of height is {}".format(heightstd))

#calculating 1st,2nd and 3rd standard deviation
height1stdstart,height1stdend=heightmean-heightstd,heightmean+heightstd
print(height1stdstart,height1stdend)
height2stdstart,height2stdend=heightmean-(heightstd*2),heightmean+(heightstd*2)
print(height2stdstart,height2stdend)
height3stdstart,height3stdend=heightmean-(heightstd*3),heightmean+(heightstd*3)
print(height3stdstart,height3stdend)

#percentage of data lying between 1st,2nd and 3rd standard deviation
hstdp1st=[r for r in height if r >height1stdstart and r <height1stdend]
hstdp2nd=[r for r in height if r >height2stdstart and r <height2stdend]
hstdp3rd=[r for r in height if r >height3stdstart and r <height3stdend]
print("{}% of data lies within 1st standard deviation".format(len(hstdp1st)*100.0/len(height)))
print("{}% of data lies within 2nd standard deviation".format(len(hstdp2nd)*100.0/len(height)))
print("{}% of data lies within 3rd standard deviation".format(len(hstdp3rd)*100.0/len(height)))