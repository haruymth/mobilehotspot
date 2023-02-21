# mobilehotspot

Windowsのモバイルホットスポットを常に付けたままにするプログラム

# やりかた
## 1.TurnOnMobileHotSpot.ps1 をどこかに配置する。

## 2.mobilehotspot.py をTurnOnMobileHotSpot.ps1と同じ階層に配置する。

配置した場所のパスは控えておく。

## 3.mob.bat をどこかに配置する。

mob.batの中のところに2.で控えたパスを入れる。

配置した場所のパスは控えておく。

## 4.mob.vbs をStartUpのところに配置する。

mob.vbsの中のところに3.で控えたパスを入れる。

Win+Rで「shell:startup」と入力しOKを押して出てきたフォルダにmob.vbsを配置する。

## 4.おわり

これで多分Windows起動したらそのpythonのプログラム実行されて常にモバイルホットスポットがONになる。

モバイルホットスポットを消そうとしても消せないから気を付けてね

もし無効にしたいなら「タスクマネージャー」の「Python」のタスクを終了すれば大丈夫

# 参考

### TurnOnMobileHotSpot.ps1のプログラム（これは参考というか丸パクリ)

[https://pcvogel.sarakura.net/2019/06/06/31943](https://pcvogel.sarakura.net/2019/06/06/31943)

### mob.vbsのプログラム（これも参考というか丸パクリ)

[https://m-suta.com/bibouroku-windows-batch-background/](https://m-suta.com/bibouroku-windows-batch-background/)

