import ftplib 

with ftplib.FTP('ftp.debian.org') as ftp:
    
    try:
        ftp.login()  

        size = ftp.size('debian/README')
        print(size)

    except ftplib.all_errors as e:
        print('FTP error:', e) 