# -*- coding: utf-8 -*-
import subprocess
import socket
import time
import threading
import subprocess
import jtalk
import DepthCam as dc
import WhelCon
import random

host = 'localhost'
port = 10500
i = 2

# Juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
res = ''

def main():
    wth = threading.Thread(target=WhelCon.main)
    dth = threading.Thread(target=dc.main)
    dth.start()
    WhelCon.setup()
    while True:

        if i == 1:
            break
        # 音声認識の区切りである「改行+.」がくるまで待つ
        while (res.find('\n.') == -1):
            # Juliusから取得した値を格納していく
            res += sock.recv(1024).decode()
            if i == 1:
                break
        word = ''
        for line in res.split('\n'):
            if i == 1:
                break
            # Juliusから取得した値から認識文字列の行を探す
            index = line.find('WORD=')
            # 認識文字列があったら...
            if index != -1:
                # 認識文字列部分だけを抜き取る
                line = line[index + 6 : line.find('"', index + 6)]
                # 文字列の開始記号以外を格納していく
                if line != '[s]':
                    word = word + line
                    print(word)
            res = ''
            if word == 'おっけいゴミこ':
                print('返答：ごようはなんでしょうか')
                jtalk.jtalk(u'ごようはなんでしょうか')
                time.sleep(4)
                while True:
                    if i == 1:
                        break
                    while (res.find('\n.') == -1):
                        # Juliusから取得した値を格納していく
                        res += sock.recv(1024).decode()
                        if i == 1:
                            break

                    word = ''
                    for line in res.split('\n'):
                        if i == 1:
                            break
                        # Juliusから取得した値から認識文字列の行を探す
                        index = line.find('WORD=')
                        # 認識文字列があったら...
                        if index != -1:
                            # 認識文字列部分だけを抜き取る
                            line = line[index + 6 : line.find('"', index + 6)]
                            # 文字列の開始記号以外を格納していく
                            if line != '[s]':
                                word = word + line
                                print(word)
                            # 文字列を認識したら...
                        if word == 'おはよう':
                            morning_word = [u'おはよう', u'おはようございます',u'ごきげんよう']
                            jtalk.jtalk(random.choice(morning_word))
                            print('返答：' )
                            time.sleep(4)
                        elif word == 'じこしょうかいをして':
                            jtalk.jtalk(u'はい、わかりました。　私はの名前はごみ箱　あなたの生活をサポートします。')
                            time.sleep(4)
                        elif word == 'うたって':
                            time.sleep(50)
                            print(0)
                        elif word == 'ついてきて':
                            jtalk.jtalk(u'はい、ついていきます')
                            time.sleep(4)
                            wth.start()


                        res = ''

                        if word == 'ばいばいごみばこ':
                            WhelCon.end()
                            i = 1
                            break
                if i == 1:
                    break
            if i == 1:
                break
        if i == 1:
            jtalk.jtalk(u'ばいばい')
            WhelCon.end()
            break
        
if __name__ == '__main__':

    main()