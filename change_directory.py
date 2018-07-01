import ftplib

with ftplib.FTP('ftp.debian.org') as ftp:
    
    try:
        ftp.login()  
        
        wdir = ftp.pwd()
        print(wdir)

        ftp.cwd('debian')

        wdir2 = ftp.pwd()
        print(wdir2)

    except ftplib.all_errors as e:
        print('FTP error:', e) 