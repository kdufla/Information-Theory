import os

for i in range(1,7):
    os.system('python3 BCH.py Tests/E/00'+str(i)+'.dat Tests/E/00'+str(i)+'.dst x')
    os.system('diff x Tests/E/00'+str(i)+'.ans -s')

