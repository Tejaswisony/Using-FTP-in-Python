import ftplib 

with ftplib.FTP('ftp.example.com') as ftp:
    
    filename = 'README'
    
    try:    
        ftp.login('user7', 's$cret')  
        
        with open(filename, 'rb') as fp:
            
            res = ftp.storlines("STOR " + filename, fp)
            
            if not res.startswith('226 Transfer complete'):
                
                print('Upload failed')

    except ftplib.all_errors as e:
        print('FTP error:', e) 