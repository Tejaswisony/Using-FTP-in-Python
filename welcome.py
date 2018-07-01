
import ftplib

with ftplib.FTP('ftp.debian.org') as ftp:
    print(ftp.getwelcome())