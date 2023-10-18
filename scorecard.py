def batscore(d):
    name=d.get('name')
    runs=d.get('runs')
    balls=d.get('balls')
    batscore=int(runs/2)
    four=d.get('4')
    six=d.get('6')

    batscore=int(runs/2)
    if batscore>=50: batscore+=5
    if batscore>=100: batscore+=10

    if runs>0:
        sr=runs*100/balls
        if sr>=80 and sr<100: batscore+=2
        if sr>=100:batscore+2*six

        return{'name':name,'batscore':batscore}
def bowlscore(d):
    name=d.get('name')
    wkt=d.get('wkts')
    balls=d.get('overs')
    runs=d.get('runs')
    bowlscore=wkt*10
    if wkt>=3: bowlscore=bowlscore+5
    if wkt>=5: bowlscore=bowlscore=bowlscore+10
    if balls>0:
        er=runs/balls
        #print("eco:",er)
        if er<=2: bowlscore=bowlscore+10
        if er>2 and er<=3.5: bowlscore=bowlscore+7
        if er>3.5 and er<=4.5: bowlscore=bowlscore+4
    return{'name':name,'bowlscore':bowlscore}
    
    
I1=[{'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0},
{'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'balls':112, 'field':0}]

I2=[{'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1},
{'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0},
{'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}]
for i in I1:
     print(batscore(i))
for i in I2:
     print(bowlscore(i))
