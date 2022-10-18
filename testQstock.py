import qstock as qs
import pandas as wdspd
import time
#持有代码
hold=['002487','300249','002466','002428','688660','601108','600470',
'000591','600984','300581','002092','002436','300137','000830','002463','300409','688223','113629','127070']
#持有数量
shareDW=wdspd.DataFrame({'持仓':[800,900,4200,36100,13151,8000,0000,11300,7020,
1800,3600,2700,4100,1100,1000,500,3450,10,10]})
shareHJ=wdspd.DataFrame({'持仓':[0,0,0,3000,0,0,7000,0,0,
0,0,0,0,0,0,0,0,0,0]})
shareAll=shareDW+shareHJ
cashDW=1151.4
cashHJ=66.87
#获取行情数据
df=qs.realtime_data(code=hold)

TotalStock=shareAll['持仓']*df['最新']
# temp=(shareDW*df['最新']).sort_values().sum()
TotalDW=(shareDW['持仓']*df['最新']).sum()+cashDW #东吴
TotalHJ=(shareHJ['持仓']*df['最新']).sum()+cashHJ #华金


Total=TotalStock.sum()+cashDW+cashHJ

# df.insert(3,column='持仓',[1,2,3])
df.insert(2,'持仓',shareAll['持仓'])
df.insert(3,'市值',shareAll['持仓']*df['最新'])

print(df['市值'].T)
print(time.ctime())
   

