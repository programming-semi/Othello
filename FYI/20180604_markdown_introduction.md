# Test Markdown

## 1. Markdown とは何か
　Markdownは、文書を記述するためのマークアップ言語のひとつ.

#### Markdownメリット

* 手軽に文章構造を明示できること
* 簡単で、覚えやすいこと
* 読み書きに特別なアプリを必要としないこと
* 対応アプリを使えば快適に読み書きできること
* Githubでも使用ができる


## 2. Markdownの書き方
#### 2.1. 見出し
htmlでは &lt;h&gt;タグのようなイメージ。  
"#" をつければつけるだけ、字が小さくなっていく。(6段階)  
(ex) 以下のように書けば良い。(以下、同様にcode block の中には、例を記述して行く. )
```
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
```
---
#### 2.2. イタリック表記(斜体)、大文字
*イタリック表記* は、 "\*" もしくは "\_" で囲む。  
**太文字** は、"\*\*" もしくは、 "\_\_" で囲む。  
***イタリックAND大文字*** は"\*\*\*" もしくは "\_\_\_" で囲む。

```
*イタリック表記(斜体)*
**太文字**
***イタリックかつ大文字***
```

---
#### 2.3. 取り消し戦
~~取り消し線~~ は、"~~"で囲む。
```
~~取り消し線~~
```

---
#### 2.4. 改行
半角スペース2つを入れる。  
```
abc(半角スペース)(半角スペース)  
def
```
abc  
def

---
#### 2.5. ブロックオート
">"をつける。
```
> asdf
>> asdf  
>> asdf  

> asdf
```
> asdf
>> asdf  
>> asdf

> asdf

---
#### 2.6. リスト
番号付きリスト : "-" を付ける。  
番号なしリスト : "(番号).(半角スペース)" を付ける。
```
- list1
- list2

1. list1
2. list2
```
- list1
- list2

1. list1  
2. list2
あれ、Atom上では動かね。

---
#### 2.7. リンク
&lt;&gt;で囲む。
```
<http://google.com>
```
<http://google.com>


---
#### 2.8. エスケープ
特殊文字の表示には、"\"を付ける。Macでは、[option] + [¥]。


---
#### 2.9. 水平線

"\*\*\*" "---" "___" が水平線になる。
```
***
```

---
#### 2.10. コード記法
バッククウォート3つで囲むと、下のような、四角の中にコードが書ける。
```

```
