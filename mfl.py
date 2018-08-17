k = 21
m = 20
n = 15
N = k + m + n
#Homozygous dominant first
p_HD = k/(k+m+n)

p_HD_HD = (p_HD * ((k-1)/((k-1)+m+n)))*1
p_HD_HET = (p_HD * ((m)/((k-1)+m+n)))*1
p_HD_HR = (p_HD * ((n)/((k-1)+m+n)))*1

#HET first
p_HET = m/(k+m+n)
p_HET_HD = (p_HET * ((k)/(k+(m-1)+n)))*1
p_HET_HET = (p_HET * ((m-1)/(k+(m-1)+n)))*.75
p_HET_HR = (p_HET * ((n)/(k+(m-1)+n)))*.5

#Homozygous recessive first
p_HR = n/(k+m+n)
p_HR_HD = (p_HR * ((k)/(k+m+(n-1))))*1
p_HR_HET = (p_HR * ((m)/(k+m+(n-1))))*.5
p_HR_HR = (p_HR * ((n-1)/(k+m+(n-1))))*0

TOTAL = p_HD_HD + p_HD_HET + p_HD_HR + p_HET_HD + p_HET_HET + p_HET_HR + p_HR_HD + p_HR_HET + p_HR_HR

print(TOTAL)

print(1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) ))