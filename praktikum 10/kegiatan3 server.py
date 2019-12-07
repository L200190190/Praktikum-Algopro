import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50002))
s.listen(5)
print "Server siap"
perintah =''
p=0
l=0
t=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item) == 2:
            if perintah == 'panjang':
                p = int(item[1])
                komm.send('panjang disimpan')
            elif perintah == 'lebar':
                l = int(item[1])
                komm.send('lebar disimpan')
            elif perintah == 'tinggi':
                t = int(item[1])
                komm.send('tinggi disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L = float(2*(p*l+p*t+l*t))
            response = 'luas permukaan balok dengan panjang {} lebar {} tinggi {} adalah {}'.format(p,l,t,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
        
            
                  
                  
