# group1
最終成果物
# Name
顔判別システム

# これはなに？
嵐のメンバー5人の顔全体や顔のパーツごとのデータを用意し、学習させる。
それによって、顔全体・パーツごとにそれぞれどのくらいの割合で似ているかを判別させる。

# つかいかた

## DL，前処理
１．githubからファイルをDL，解凍，前処理．

2.icrawlerのインストール
 ```
$ pip install icrawler
```

## 機械学習
１．icrawlerによる画像の収集
```
from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "大野智"})
crawler.crawl(keyword="大野智", max_num=200)
```

２．OpenCVを利用して顔(瞳)部分を抽出し、抜き出す
```
$ python img_collection.py
$ python img_collection_eye.py
```

３．(２．)で作成したdatasetを元に学習させる．結果はグラフと正解率を表示．
```
$ python learning_2.py
```

4 . 用意しておいてオリジナルの写真で顔判別を行う
```
$ python test.py
```

# ファイルのせつめい

## img_collection.py：画像の顔の部分だけを抽出する
+  入手した画像をカスケード分類器で顔の部分を抽出する
+ 抽出に失敗した画像をfaceディレクトリに入れる

## img_collection_eye.py：画像の瞳の部分だけを抽出する
+  入手した画像をカスケード分類器で顔の部分を抽出する
+ 抽出に失敗した画像をface3ディレクトリに入れる

## learning_2.py：datasetを学習を行う
+ datasetを元に，tensorflow.kerasを用いて深層学習を行います.
+ 結果はグラフと正解率を表示．

## test.py：顔判別を行う
+ tensorflowを使い用意しておいた写真の人物と学習した顔で認証を行う
+ 結果出力で切り取られた顔写真と,それぞれのメンバー(松本潤,二宮和也,相葉雅紀,櫻井翔,大野智)に似ているかを数値で表す。


# 動作環境
+ Python 3.6.4
+ tensorflow

##作成情報

#開発メンバー
+ 185718F 喜瀬大地 
+ 185741A 呉屋厚斗
+ 185728C 山城宏太
+ 185716K 呉屋樹

#所属
+ 琉球大学 工学部 工学科 知能情報コース

# 連絡先
+ e185718@ie.u-ryukyu.ac.jp
+ e185741@ie.u-ryukyu.ac.jp
+ e185728@ie.u-ryukyu.ac.jp
+ e185716@ie.u-ryukyu.ac.jp