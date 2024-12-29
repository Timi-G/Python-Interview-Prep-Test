'''Easy 1
nums=[1,1,1,2,2,2,4,5,8]

u_nums=list(dict.fromkeys(nums))

print(nums.count(1))

if any([n>10 or n<1 for n in u_nums]):
    print('outside boundary')'''


'''# Easy 2
n=5
lim=3

ans=0
for c1 in range(lim+1):
    for c2 in range(lim+1):
        c3=n-c1-c2
        if 0<=c3<=lim:
            ans+=1
print(ans)'''

# Medium 1
s='  42'
# step 1
s = s.strip()
# step 2
sign = 1
if s[0] == '-':
    sign = -1
    s = s.lstrip('-')

# step 3
new_s = ''
for l in s:
    if l.isnumeric():
        new_s += l
    else:
        break
fig = sign * int(new_s)

if fig < -2 ** 31:
    fig = (-2 ** 31)
    print(fig)
if fig > (2 ** (31)) - 1:
    fig = (2 ** (31)) - 1
print(fig)

'''Hard 1
nums1=[1,4,5,19]
nums2=[3,7,10]

ln1 = len(nums1)
ln2 = len(nums2)
ln = ln1 + ln2
if ln1 > 1000 or ln2 > 1000:
    print(0)
if ln < 1 or ln > 2000:
    print(0)
if any([n < -10 ** 6 or n > 10 ** 6 for n in nums1]) or any([n < -10 ** 6 or n > 10 ** 6 for n in nums2]):
    print(0)

nums = nums1 + nums2
s_nums = sorted(nums)
mid = int(ln / 2)
if ln % 2 == 0:
    median = sum(s_nums[mid - 1:mid + 1]) / 2
else:
    median = s_nums[mid]
print(median)'''

# Note:
# Work on boolean logic- and, or, not
# Work on checking program syntax carefully

s='bbabd'
s='#'+'#'.join(s)+'#'

dp=9999999+9999
print(dp)

wood=[1,7,9]

l=max(wood, key=wood.count)
fence=0
unused=[]
for p in wood:
    if p==l:
        fence+=1
    else:
        unused+=[p]

for n,p in enumerate(unused):
    for q in unused[n+1:]:
        if p+q==l:
            fence+=1
if fence > 0:
    print(fence)
else:
    print(-1)