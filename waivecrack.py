import hashlib, os, sys

_thdCnt = 0
hashed = ''

def _sha1(_pwd):
    _pwd = _pwd.encode('utf-8')
    sha1_hasher = hashlib.sha1()
    sha1_hasher.update(_pwd)
    _hashed = sha1_hasher.hexdigest()
    if _hashed.lower() == hashed.lower():
        sys.exit('\r\n \033[1m\033[31mCRACKED! PASSWORD IS: ' + _pwd.decode())

def _sha256(_pwd):
    _pwd = _pwd.encode('utf-8')
    sha256_hasher = hashlib.sha256()
    sha256_hasher.update(_pwd)
    _hashed = sha256_hasher.hexdigest()
    if _hashed.lower() == hashed.lower():
        sys.exit('\r\n \033[1m\033[31mCRACKED! PASSWORD IS: ' + _pwd.decode())

def _sha512(_pwd):
    _pwd = _pwd.encode('utf-8')
    sha512_hasher = hashlib.sha512()
    sha512_hasher.update(_pwd)
    _hashed = sha512_hasher.hexdigest()
    if _hashed.lower() == hashed.lower():
        sys.exit('\r\n \033[1m\033[31mCRACKED! PASSWORD IS: ' + _pwd.decode())

def _sha3(_pwd):
    _pwd = _pwd.encode('utf-8')
    sha3_hasher = hashlib.sha3_256()
    sha3_hasher.update(_pwd)
    _hashed = sha3_hasher.hexdigest()
    if _hashed.lower() == hashed.lower():
        sys.exit('\r\n \033[1m\033[31mCRACKED! PASSWORD IS: ' + _pwd.decode())

def main():
    global _thdCnt, hashed
    os.system('clear')
    print('''\033[22m\033[32m
  █   █  █  █ █ █ ██   ███ ███  █  ███ █ █
 ░█  ░█░█░█░ ░█ █░█░  ░█░ ░█░█░█░█░█░ ░█░█
 ░█ █░█░█░█ █░█ █░██  ░█  ░██ ░█░█░█  ░██
 ░█░█░█░███░█░█ █░█░  ░█  ░█░█░███░█  ░█░█
 ░░█░█ ░█░█░█░░█ ░██  ░███░█░█░█░█░███░█░█
  ░ ░  ░ ░ ░  ░  ░░   ░░░ ░ ░ ░ ░ ░░░ ░ ░
\033[1m\033[32m
 Select HASH algorithm:\033[22m\033[37m
 ======================
 \033[22m\033[31m{\033[1m\033[31m1\033[22m\033[31m} \033[22m\033[37mSHA-1
 \033[22m\033[31m{\033[1m\033[31m2\033[22m\033[31m} \033[22m\033[37mSHA-256
 \033[22m\033[31m{\033[1m\033[31m3\033[22m\033[31m} \033[22m\033[37mSHA-512
 \033[22m\033[31m{\033[1m\033[31m4\033[22m\033[31m} \033[22m\033[37mSHA-3
''')
        
    try:
        option = int(input(' \033[22m\033[37mOption (1-4):\033[1m\033[32m '))
        hashed = input(' \033[22m\033[37mHash to crack:\033[1m\033[32m ')
        wrdlst = input(' \033[22m\033[37mWordlist (/home/example.txt):\033[1m\033[32m ')
        thredz = int(input(' \033[22m\033[37mThreads (default 1):\033[1m\033[32m '))
        input('\r\n \033[22m\033[31mReady? Strike <ENTER> to crack and <CTRL+C> to abort...\r\n\033[22m\033[37m')
            
        _pwdz = []
        # import passwords to list
        with open(wrdlst, 'r') as f:
            for line in f:
                if "\n" in line:
                    line = line.replace("\n", "")
                _pwdz.append(line)
           
        # iterate through password list
        i = 0
        for _pwd in _pwdz:
            while _thdCnt >= thredz:
                pass
            
            i +=1
            print(' [' + str(i) + '] Attempting: ' + _pwd)
            if option == 1:
                _sha1(_pwd)
            elif option == 2:
                _sha256(_pwd)
            elif option == 3:
                _sha512(_pwd)
            elif option == 4:
                _sha3(_pwd)
            else:
                sys.exit('\r\n \033[22m\033[31mInvalid option selected.')
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        input('\r\n \033[22m\033[31mCritical error encountered! Strike <ENTER> to return to menu...\r\n')

    sys.exit('\r\n\r\n \033[22m\033[31mThank you for using WaiveCrack 1.0\r\n')

if __name__ == "__main__":
    main()

