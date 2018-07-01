import ftplib 

with ftplib.FTP('ftp.debian.org') as ftp:
    
    try:
        ftp.login()  
        
        # TYPE A for ASCII mode
        ftp.sendcmd('TYPE I') 

        size = ftp.size('debian/ls-lR.gz')
        print(size)

    except ftplib.all_errors as e:
        print('FTP error:', e) 