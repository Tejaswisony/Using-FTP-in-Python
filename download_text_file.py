
import ftplib 
import os

with ftplib.FTP('ftp.debian.org') as ftp:
    
    file_orig = '/debian/README'
    file_copy = 'README'
    
    try:
        ftp.login()  
        
        with open(file_copy, 'w') as fp:
            
            res = ftp.retrlines('RETR ' + file_orig, fp.write)
            
            if not res.startswith('226 Transfer complete'):
                
                print('Download failed')
                if os.path.isfile(file_copy):
                    os.remove(file_copy)          

    except ftplib.all_errors as e:
        print('FTP error:', e) 
        
        if os.path.isfile(file_copy):
            os.remove(file_copy)