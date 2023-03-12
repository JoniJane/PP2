import os 

path = input()  

print("existance :", os.access(path, os.F_OK))
print("readable :", os.access(path, os.R_OK))
print("writable :", os.access(path, os.W_OK))
print("executable :", os.access(path, os.X_OK)) 
'''
os.F_OK - проверка существования файла или каталога,
os.R_OK - проверка возможности чтения,
os.W_OK - проверка возможности записи,
os.X_OK - проверка выполнения файла или открытия директории
'''