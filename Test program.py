# scoop=[]
# print(scoop)
# for x in range (3):
#     scop=[]
#     for y in range (2):
#         z=x+y+1
#         # scop.append(z)
#         # scoop.pop([x][y])
#         scop.append(z)
#         print(scop)
#         # print(scoop)
#     scoop.append(scop)
# print(scoop)

from itertools import chain, combinations, groupby

k=[4,6,5,3]
tsubs=[]
osubs=[4,6,5,3]
subs=list(chain.from_iterable(combinations(k,r)for r in range(2,len(k)+1)))
# sub=[[8,9]]+[10]
# print(sub)
# while len(osubs)<=len(k):
#     for i in osubs:
#         print(osubs)
#         for j in k:
#             if i != j:
#                 if isinstance(i,list):
#                     if j not in i:
#                         s = i+[j]
#                         tsubs += [s]
#                 else:
#                     s = [i]+[j]
#                     tsubs += [s]
#     n=len(k) if len(k) <= len(osubs) else len(osubs)
#     osubs=tsubs[-n:-1]
# tsubs.sort()
# tsubs=list(tsubs for tsubs,_ in groupby(tsubs))

# subs=set(tsubs)
subs_with_even=[s for s in subs if any(n%2==0 for n in s)]
sum_even_sub=sum([sum(es) for es in subs_with_even])
# print(subs_with_even)
print(sum_even_sub)

strs = ['armenia','arabia','argentina']
# all_letters=[]
it = min([len(l) for l in strs])
all_letters=[[lett[n] for lett in strs] for n in range(it)]
# for n in range(it):
#     letters = []
#     for word in strs:
#         letters += [word[n]]
#     all_letters += [letters]

res=[]
for letters in all_letters:
    if all(l == letters[0] for l in letters):
        res += letters[0]
    else:
        if res:
            print(''.join(res))
            break
        else:
            print('no preceding string')
            break

a=[20,42,50,19]
nres=[]
for n in a:
    nres+=[sum([int(i) for i in str(n)])]
res=sorted(nres)

print(res)

integer=1680
romans={1:['I','V'],10:['X','L'],100:['C','D'],1000:['M']}
keys=list(romans)

intstr=str(integer)[::-1]
romans_list=[]
for n,loop in enumerate(intstr):
    fig=int(loop)
    # unit
    if fig==4 or fig==9:
        romans_list+=[romans[keys[n]][0]+romans[keys[n]][1]]
    elif fig-5==0:
        romans_list+=[romans[keys[n]][1]]
    elif fig-5>=1:
        romans_list += [romans[keys[n]][1]+(romans[keys[n]][0]*(fig-5))]
    else:
        romans_list+=[romans[keys[n]][0]*fig]
romans_list=romans_list[::-1]
final_romans=''.join(romans_list)
print(final_romans)


word='tuuuuurrriinnnngg'
letters=list(word)

uword=list(dict.fromkeys(letters))
for ul in uword:
    n=word.count(ul)
    if n>3:
        word=word.replace(ul,'',n-3)
print(word)

rletters='abbab'
rl_list=list(rletters)
u_rl={k:[] for k in list(dict.fromkeys(rl_list))}
for n,l in enumerate(rl_list,1):
    u_rl[l]+=[n]
print(u_rl)

string='abcdcf'
s=[]
count=0
for n in range(len(string)-3):
    s+=[string[n:n+4]]

for l in s:
    print(l)
    if all([l[n]>l[n+1] for n in range(3)]):
        count+=0
    if all([l[n]<l[n+1] for n in range(3)]):
        count+=1
print(count)

num=[n for n in range(1,50)]
print(num)
for n in range(1,50):
    if sum(num[:n])==sum(num[n-1:]):
        print(sum(num[:n]), sum(num[n-1:]))
        print(n)

digits={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

inp='26'
vals=max([len(l) for l in digits.values()])
out=[]
while True:
    for lent in range(len(inp)):
        ini = []
        for n in range(vals):
            ini+=[digits[int(inp[n])][lent]]
        out+=[ini]