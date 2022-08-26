CONTROL = {'INFO': 'Info.txt', 'DEBUG': 'Debug.txt', 'ERROR': 'Error.txt'}

def Fileparse(filename):
    with open(filename) as f:
        for line in f:
            key, *_ = line.split()
            if (txt := CONTROL.get(key)):
                with open(txt, 'a') as out:
                    out.write(line)
        f.close()
if __name__=='__main__':
    filename = 'logfile.txt'
    Fileparse(filename)


                
