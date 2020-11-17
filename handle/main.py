import string
import math
import _thread
import threading
from datetime import datetime
import handle.cipher.ceasar as ceasar
import handle.cipher.vigenere as vigenere

class multithread_cipher (threading.Thread):
    def __init__(self, threadID, cipher,encrypt,key,_string):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.cipher = cipher
        self.encrypt = encrypt
        self._string = _string
        self.key = key

        self._return = None
    
    def run(self):
        if(self._return == None):
            self._return = ""
            ## Type Of Cipher
            if(self.cipher == "Ceasar"):
                self._return = ceasar.encrypt(self._string,self.key) if (self.encrypt) else ceasar.decrypt(self._string,self.key)
            elif self.cipher == "Vigenere":
                self._return = vigenere.encrypt(self._string,self.key) if (self.encrypt) else vigenere.decrypt(self._string,self.key)
            else:
                print("nothing")

    def join(self):
        threading.Thread.join(self) 
        return self._return


def diff_times_in_seconds(t1, t2):
    diff = t2-t1
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis


def sequential(cipher,encrypt,key,input_file,output_file):
    _string = open(input_file, 'r').read()
    
    _time_begin = datetime.today()
    _cipher = ""
    ## Type Of Cipher
    if(cipher == "Ceasar"):
        _cipher = ceasar.encrypt(_string,key) if (encrypt) else ceasar.decrypt(_string,key)
    elif cipher == "Vigenere":
        big_key = key * (len(_string) // len(key)) + key[:len(_string) % len(key)]
        _cipher = vigenere.encrypt(_string,big_key) if (encrypt) else vigenere.decrypt(_string,big_key)
    else:
        print("nothing")
    _time_end = datetime.today()
    output = open(output_file.replace(".txt", "")+"_sequential.txt", 'w')
    output.write(_cipher)
    output.close() 
    return diff_times_in_seconds(_time_begin,_time_end)

def parallel(cipher,encrypt,key,input_file,output_file,thread):
    threads = []
    results = []
    big_key = None
    big_keys = None
    _string = open(input_file, 'r').read()
    x = math.ceil(len(_string) / thread)
    strings = [(_string[i:i+x]) for i in range(0, len(_string), x)] 
    if cipher == "Vigenere":
        big_key = key * (len(_string) // len(key)) + key[:len(_string) % len(key)]
        big_keys = [(big_key[i:i+x]) for i in range(0, len(big_key), x)] 
        
    for i in range(len(strings)):
        final_key = big_keys[i] if (cipher == "Vigenere") else key
        threads.append(multithread_cipher(i,cipher,encrypt,final_key,strings[i]))
        threads[i].start()
    _time_begin = datetime.today()
    for i in range(len(threads)):
        results.append(threads[i].join())
    _time_end = datetime.today()   
    _cipher = "".join(results)
    output = open(output_file.replace(".txt", "")+"_parallel.txt", 'w')
    output.write(_cipher)
    output.close() 
    return diff_times_in_seconds(_time_begin,_time_end)
    
    



