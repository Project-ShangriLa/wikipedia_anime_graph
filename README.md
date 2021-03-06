wiki\_relevance.py
-------

##概要
２つのwikipediaのページの関連度を計算します。  
声優同士の関連度の計算が目的。  
声優以外のワードでも可能?  
実行する関数の引数を指定することで、wikipediaのページのすべてのリンクを抽出するか、  
出演作品(アニメ)に限定し抽出するかを指定できます。  

##実行

```
$python3 wiki_relevance.py "声優1" "声優2"
```

声優を2人入力すると、それぞれの関連度を求めます。

##note

 - 手法としては、それぞれのページのリンクとなっている言葉を抽出、２つのページ間で一致するリンクワードから関連度を調べます。
 - 一致度としてJaccard係数を用いています。他の方法のほうが良いかも。
 - 単純に同じワードが多いほうが関連度は大きくなります。
 
 - 単語ごとに重みをつけたほうが良いかも。
 - ~~あと、ページ間で最短何リンクでたどり着けるかを考慮したほうが良いかも。~~  
 最短リンク数は声優を2つページを声優と仮定しているので1、2くらいにはなるはずなので、これはとりあえず無視。  
 - いろいろ先行研究があるのでそれを加えてみる。  
 - そのままでは関連度の値が小さいので規格化したほうが良いかも。  
 - wikipediaからアニメ作品の情報を持ってくるプログラムからキャストを取ってきて、  
 このプログラムに渡し、解析まで自動化したい。  
 →MDSまでは自動化完了
  
   
##実行結果(追加)

```
$ python3 wiki_relevance.py "悠木碧" "斎藤千和"  
1.166830897936477  
   
$ python3 wiki_relevance.py "悠木碧" "悠木碧"  
0.0  
  
$ python3 wiki_relevance.py "悠木碧" "喜多村英梨"  
1.091308325848836  
  
$ python3 wiki_relevance.py "悠木碧" "水橋かおり"  
1.3140325399303059  
  
$ python3 wiki_relevance.py "杉田智和" "中村悠一"  
0.9877815541443403  
  
$ python3 wiki_relevance.py "茅野愛衣" "島本須美"  
1.9128498242810998  
```

 - 類似度の値が小さかったので対数変換しました。  
 - 類似度の逆数を対数変換してます。  
 - 声優同士が似ているほど小さく、似ていないほど大きな値となります。  
完全一致で0となります。   
  
  
  
  
  
  
wiki\_vc\_active.py
-------

##概要

出演したアニメ作品の数を年代ごとに表示します。

##実行

```
$python3 wiki_vc_active.py "声優"
```

##note
 - 詳しくは、出演したアニメ作品の数ではなく、ポイントを表示してます。  
 - 主演アニメは３ポイント、その他は１ポイントです。  

 - 声優の活躍年代から類似声優を見つけることができそう。  
 - 年代における活躍の頻度分布の類似度を声優同士の類似度として表せそう。  
 
##実行結果
 
```
$ python3 wiki\_vc\_active.py "坂本真綾"  
1996.0 4.0  
1998.0 6.0  
1999.0 6.0  
2001.0 4.0  
2002.0 10.0  
2003.0 3.0  
2004.0 5.0  
2005.0 2.0  
2006.0 11.0  
2007.0 4.0  
2008.0 20.0  
2009.0 4.0  
2010.0 19.0  
2011.0 10.0  
2012.0 5.0  
2013.0 6.0  
2014.0 11.0
  
$ python3 wiki\_vc\_active.py "島本須美"  
1979.0 5.0  
1980.0 5.0  
1981.0 1.0  
1982.0 3.0  
1983.0 6.0  
1984.0 3.0  
1985.0 6.0  
1986.0 23.0  
1987.0 3.0  
1988.0 8.0  
1989.0 6.0  
1990.0 7.0  
1991.0 5.0  
1992.0 9.0  
1993.0 3.0  
1994.0 4.0  
1995.0 4.0  
1996.0 5.0  
1997.0 8.0  
1998.0 4.0  
1999.0 4.0  
2000.0 1.0  
2001.0 2.0  
2002.0 5.0  
2003.0 5.0  
2004.0 3.0  
2005.0 6.0  
2006.0 2.0  
2007.0 4.0  
2008.0 9.0  
2009.0 2.0  
2010.0 1.0  
2011.0 5.0  
2012.0 2.0  
2013.0 4.0  
  
$ python3 wiki\_vc\_active.py "茅野愛衣"  
2010.0 3.0  
2011.0 34.0  
2012.0 36.0  
2013.0 60.0  
2014.0 55.0  
2015.0 35.0  
  
```
  
 - 一応どの年代の人のデータも取ってこれる模様。  
 - あとは、分布間の距離でも比較したらなんかでそう。  
  
  
  
mds.py
-------

##概要
声優同士の関連度を多次元尺度構成法(MDS)を用いてグラフを描写します。  
声優一覧のデータ(cv_list.dat)を渡してます。  
  
##実行  

```
$python3 mds.py
```

```-m``` オプションで./figure にグラフを出力します。  
```-s``` オプションで座標を./data に出力します。  
  
  
  
  
  
make_json.py
-------
##概要
mds.pyの出力した座標データと声優一覧のデータ(cv_list.dat)をjson形式に変換します。  
  
  
  
結果(類似度)
-------
##node.html
make_json.pyにより出力したデータを参照して、図を描写します。  
javascriptで描写することで見やすくなりました。  
拡大縮小できるのが良い。  
以下のリンクから見れます。  
<a href="node.html" target="_blank">グラフ</a>
<!-- <iframe src="node.html" width=900 height=600></iframe>   -->

 - 声優間の距離が近い声優ほど近くに配置されます。  
 - twitterフォロワー上位50人を与えて見ました。
 - 右上に女性、左下に男性のクラスタが形成されています。  
 - 左上にはベテランの声優が、右下には若手の声優が、その中間には中堅と言える声優が固まっているように見えます。男性声優のほうがその特徴は顕著にあらわれてます。  
 - なんとなく仲良さそうな人はちゃんと近く配置されてます。  
  
  
