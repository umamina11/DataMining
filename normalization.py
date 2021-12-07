import statistics
import scipy.stats as stats
import math


# calculating mean
def getmean(list1):
    size=len(list1)
    totsum=0
    for i in list1:
        totsum=totsum+i
    mean=totsum/size
    return mean

# calculating standard deviation
def getstd(list1,mean):
    size=len(list1)
    d=0
    for i in list1:
        d +=(float(i) - mean) ** 2
    variance = d/float(size)
    sd=math.sqrt(variance)
    return sd
