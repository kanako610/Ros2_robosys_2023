
#mypkg
このリポジトリ―はロボットシステム学2023の講義内で扱ったコードファイルが入っているリポジトリ―です。
このリポジトリ―を使うためにはパソコンにROS2がインストールされていないと使えません。

##インストール方法
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



# 必要なソフトウェア
* テストで確認済

  * python 3.7 ~3.10
# テスト環境

* Ubuntu20.04



# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。　　
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て、自身の著作としました。　　
   *  [ryuichiueda/my_slides/robosys/2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* 　©　2023 Kanako Takahashi　
