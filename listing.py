import ftplib

with ftplib.FTP('ftp.debian.org') as ftp:
    
    try:
        ftp.login()  

        files = []

        ftp.dir(files.append)

        print(files)
            
    except ftplib.all_errors as e:
        print('FTP error:', e)