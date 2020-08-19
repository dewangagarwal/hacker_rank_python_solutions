marksheet=[]
score=[]
n=int(input())
for _ in range(n):
    name = input()
    marks = float(input())
    marksheet+=[[name,marks]]
    score+=[marks]
a=sorted(list(set(score)))[1]
for b,c in sorted(marksheet):
    if c==a:
        print(b)
