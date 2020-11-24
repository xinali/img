
import subprocess



fp = open('files2.txt', 'r')
files = fp.readlines()
for file_name in files:
    file_name = file_name.strip()
    if '/' in file_name:
        file_tmp = file_name.split('/')[-1]
    else:
        file_tmp = file_name
    print ('getting file: ', file_name)   
    subprocess.call(r'.\qshell get xinali {} -o files\{}'.format(file_name, file_tmp))
