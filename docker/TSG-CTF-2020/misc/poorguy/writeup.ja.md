# Poor Stego Guy Writeup (ja)

## 問題

PNGファイルとその生成スクリプトが与えられる。生成スクリプトはまず以下のImagemagickコマンドでランダムなJPEGファイルを作成し、

```
docker run -v `pwd`:/mnt dpokidov/imagemagick:7.0.10-9 -size 128x128 xc:"gray(50%)" +noise random -level -20%,120%,1.0 -quality 50 /mnt/noise.jpg
```

生成した画像の各ピクセルのLSBをフラグとXORしてPNGとして出力するものである。

各ビットのLSBを塗りつぶす、ステガノグラフィーの典型テクニック⋯⋯と思いきや、XORなので元のJPEGファイルがないとフラグを復元できない。いかにするべきか。という問題である。

## 解法

まず本問が原理的に回答可能であることを確認しておこう。最初にImagemagickコマンドで生成されるのがPNGファイルである場合、本問は回答不可能である。なぜならランダムに生成されたピクセル値と平文をXORすることは本質的にワンタイムパッドと同一であり、元の乱数値が予測できない限り解読できないからである。

ここで重要なのは、当然、最初に生成されるのがPNGファイルではなくJPEGファイルであることである。JPEGファイルは不可逆圧縮であり、画像の情報量を落とすことによって圧縮を実現している。つまり情報量が落とされた状態において取りうる画像ピクセルの状態は単なるランダムなノイズ画像と比較して疎であり、これの取りうる状態の一つに特定の操作を加えた画像から元の画像を復元することは、原理上可能である。

この性質を用いて元の画像を入手し、生成されたoutput.pngと比較することによってフラグを復元することが可能である。ただしこれを行うにはJPEGに関する深い知識が必要となる。具体的な手法について以下に説明しよう。

まず、JPEGの圧縮原理について簡単に述べる。JPEGではおおよそ以下の手順で圧縮を行う。

1. 画像を8x8ピクセルのブロックに分割する (以降各ブロックごとに処理を行う)
1. ピクセル値に二次元離散コサイン変換を行い周波数成分に変換する
1. 周波数成分の値を量子化し指定されたベクトルの倍数に丸める

二次元離散コサイン変換は画像のピクセル値を離散信号とみなして周波数領域にマッピングする変換手法のひとつですが、難しいことを抜きにして考えれば最終的に以下のような64種類のパターンの線形な重ね合わせによって表現するというものです。

![](https://abyx.be/images/2431007f3188e37f4e156a8374b4f611.png)

DCT係数は通常実数値をとりますが、JPEGではこれをさらに圧縮して、パターンごとに特定の値の倍数になるように丸めてしまいます。これを量子化と呼び、このパターンごとの「特定の値」の一覧を量子化テーブルと呼びます。

量子化テーブルはJPEGファイル内で定義されるため多様な値を取ることができますが、libjpegを始めとする標準的なエンコーダーではあらかじめ定義された固定の量子化テーブルを用いるのが一般的です。特に画質パラメータを50に設定した場合は[JPEG仕様書のセクションK1に記されている量子化テーブル](https://github.com/LuaDist/libjpeg/blob/6c0fcb8ddee365e7abc4d332662b06900612e923/jcparam.c#L64-L87)を用いるため上のImagemagickコマンドで生成されたJPEGファイルの量子化テーブルを知ることは簡単です。

さて、では改めてこのJPEGの圧縮手法について考えてみましょう。JPEGによって出力されるピクセルパターンは上の64通りのパターンの線形な重ね合わせによって表現され、さらにその係数は特定の値の倍数に丸められています。crypto問題に詳しい方はもうわかったと思いますが、このような空間的性質を持つ数学的構造として**格子が挙げられます。すなわち、JPEGでエンコードされた各ブロックの値はそのまま64次元の格子上の特定の状態であるとみなすことができます。**

その上でこの問題の趣旨を振り返ってみましょう。我々の目標は、JPEGの数学的構造において取りうるある値に小さなノイズを加えたものが与えられ、そこから元の値を復元するというものです。このような問題は格子理論において最近ベクトル問題 (CVP) と呼ばれ、LLLを用いたある程度効率的な解法が知られています。特に次元が64次元程度である場合現実的な時間で元の係数を復元することが可能です。

いま、格子を構成するための各パターンとその量子化テーブル、そして目標とするベクトル値が明らかになりました。よって元のJPEG画像のピクセル値を復元することが可能であり、ここからフラグを復元することができます。

なお、通常JPEGデコーダによる逆離散コサイン変換には多少の誤差が含まれるため、問題で与えられたPillowライブラリによるデコードを完全に模倣しないとフラグを得ることができません (高精度な逆離散コサイン変換の計算を行うと逆にフラグが出てきません)。一番簡単なのは、DCT係数を得たあと一度JPEGファイルとして書き出し、それをPythonのPillowで読み込み直すことでしょう。

SageMathを用いたソルバの例が[solve.sage](solver/solve.sage)にあります。