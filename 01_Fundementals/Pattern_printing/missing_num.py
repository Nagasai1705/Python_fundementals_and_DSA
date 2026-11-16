n=[1,2,3,5,6,7,8,9,10]
m=10
act_sum=0
exp_sum= (m*(m+1))//2
for i in (n):
    act_sum=act_sum+i
diff= exp_sum-act_sum
print("missing value:",diff)


