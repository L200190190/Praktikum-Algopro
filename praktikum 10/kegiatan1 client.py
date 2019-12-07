# nama berkas: p_tcpcli.py
# Client TCP untuk server: p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Program komunikasi tentang data diri"
while pesan.lower() != 'q':
    pesan = raw_input('Perintah:')
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print 'Jawab', response
s.close()
                  
                  
