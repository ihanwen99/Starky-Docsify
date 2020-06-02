import os

ROOT=os.getcwd()
files=os.listdir(ROOT)
md_files=[i for i in files if i[0]=='D' and i[-3:]=='.md']
md_files.sort(key=lambda x: int(x.split('-')[0][3:]),reverse=True)

f=open("README.md",'w',encoding='utf-8')
f.write("""
# DayDayUp

> Starky 每日奋斗文档
""")

for file in md_files:
	filename=file[:-3]
	f.write("### [{}](DayDayUp/{})\n".format(filename,file))

f.close()