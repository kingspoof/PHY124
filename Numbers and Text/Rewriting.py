# we take this, and then rewrite it using a for loop
value = 448
count = 0
while value % 2 == 0:
    count = count+1
    value = value / 2

# we get the following
value_1 = 448
count_1 = 0
for _ in range(448):
    if(value_1 % 2 == 0):
        count_1 += 1
        value_1 /= 2
    else:
        break

print(count, end=", ")
print(count_1)



# second part of the excercise:
for i in range(10,-1,-1):
    print(i)

# will become this
i = 10
while i >= 0:
    print(i)
    i -= 1