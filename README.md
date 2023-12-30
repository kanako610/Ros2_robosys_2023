
# mypkg[![test](https://github.com/kanako610/mypkg/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kanako610/mypkg/actions/workflows/test.yml)

このリポジトリ―はロボットシステム学2023の講義内で扱ったコードファイルが入っているリポジトリ―です。
このリポジトリ―を使うためにはパソコンにROS2がインストールされていないと使えません。

## インストール方法

1.使っている環境のROS2のワークスペース以下のコードを入力してコードをダウンロードします。
```
$ git clone https://github.com/kanako610/mypkg
```
または
```
$ git clone git@github.com:kanako610/mypkg
```
2．ROS2のワークスペースで以下のコマンドを実行します。
```
$ colcon build
```
そして以下のコマンドを実行してください。
```
$ source ~/.bashrc
```

# 機能
・talker.pyで1ずつ加算されていくself.nをlistener.pyで表示する。
### ノード
Talker
システムの起動からの経過時間を秒単位で記録し、その情報を送信する機能を持つエンティティです。

Listener
Talkerから受け取った時間情報をそれを時間と分、秒に変換してログに出力するシステムです。

### トピック
CountUpという0.5秒ごとに１から1ずつ増やしていくというトピックを使って通信をしています。

# 実行方法と実行例
実行方法は以下２つあります。
## １つ目
それぞれのROS2の環境のターミナルに以下のコードを打ちこみます。この時にtalkerは何も表示されません。
```
$ cd ros2_ws
$ ros2 run mypkg talker
```
次に２つ目のターミナルを作って以下のコードを打ち込みます。
```
$ cd ros2_ws
$ ros2 run mypkg listener
```
すると２つ目のターミナル（listenerを実行したターミナル）に以下のように表示されます。
```
$ ros2 run mypkg listener
[INFO] [listener]: Listen: 0
[INFO] [listener]: Listen: 1
[INFO] [listener]: Listen: 2
[INFO] [listener]: Listen: 3
・・・
```
このように表示されれば実行成功しています。

プログラムを終了させたい場合は、Ctrl + Cを押して終了させてください。　

## ２つ目
それぞれのROS2の環境のターミナルに以下のコードを打ちこみます。
```
$ cd ros2_ws
$ ros2 launch mypkg talk_listen.launch.py
```
すると以下のような実行結果表示されます。
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/canaco61/.ros/log/2023-12-30-20-14-05-186171-Kanabook-17226
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [17228]
[INFO] [listener-2]: process started with pid [17230]
[listener-2] [INFO] [1703934846.240594410] [listener]: Listen: 0
[listener-2] [INFO] [1703934846.724053956] [listener]: Listen: 1
[listener-2] [INFO] [1703934847.217700347] [listener]: Listen: 2
[listener-2] [INFO] [1703934847.714792000] [listener]: Listen: 3
[listener-2] [INFO] [1703934848.212873449] [listener]: Listen: 4
[listener-2] [INFO] [1703934848.713620380] [listener]: Listen: 5
```
プログラムを終了させたい場合は、Ctrl + Cを押して終了させてください。　

# 必要なソフトウェア
* テストで確認済
  * python 3.7 ~3.10

* ROS2
  * version: foxy
# テスト環境

* Ubuntu20.04



# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。　　
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て、自身の著作としました。　　
   *  [ryuichiueda/my_slides/robosys/2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* 　©　2023 Kanako Takahashi　
