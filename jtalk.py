# -*- coding: utf-8 -*-

import subprocess
from datetime import datetime

def jtalk(tt):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    subprocess.run(cmd,input=tt.encode())
    aplay = ['aplay','-q','open_jtalk.wav']
    subprocess.run(aplay)

if __name__ == '__main__':
    jtalk()
#

