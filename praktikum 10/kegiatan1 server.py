# nama berkas: p_tcpser.py
# TCP Server untuk client p_tcpcli.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ''
kamus = {'nama':'Ramadhana Wahid Aji P', 'NIM':'L200190190', 'angkatan':'2019'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Perintah:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
                  
                  
