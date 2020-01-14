# Make Keyboard Shortcut IIllustration

Generate keyboard shortcut illustrations by GIMP python-fu 

GIMPのpython-fuを使ってキーボードのショートカットの位置イラストを一気に生成するツールのひな形用ソースです。

GIMPのキーボードイラスト(keyboard.xcf) + ショートカットと短い説明を書いたTSVファル(shortcut.csv) + キー位置座標の一覧TSVファイル(keydef.csv)  
 -> GIMPのpython-fuで変換
複数枚のキーショートカットにマークを付けたキーボードイラスト

- インストール

GIMP 2.10のプラグインディレクトリに makeShortcutPict.py をコピーして配置する(Windowsの場合 C:\Users\XXXX\AppData\Roaming\GIMP\2.10\plug-ins など)

- 実行方法  

  1. makeShortcutPict.py をコピー後、GIMPを再起動する
  2. メニューの ExTool > make shortcut pict を選択する
  3. Keyboard Picture を押して、keyboard.xcf を選択する。  
Shortcut define TSV を押して、shortcut.csv を選択する。  
Key define TSV を押して、keydef.csv を選択する。
  4. OKを押す。

keyboard.xcfと同じディレクトリに pictOut ディレクトリを生成し、その中にショートカットの図版を生成する。
![サンプル](https://github.com/mfukushim/ChromeHistoryFilter/AltDown.png )

- TSVデータフォーマット  
UTF-8のTSVです。  
  1. shortcut.csv ショートカット定義  
キー名の組み合わせ(+で分離) tab 説明文  
例  
Ctrl+F4 アクティブなエディタタブを閉じる
  2. keydef.csv キー位置定義  
キー名 tab x位置 tab y位置  
例  
F1	310	166

- 参考データ  
以下のデータを使わせていただきました。
  - キーボードショートカットデータ  
  IntelliJ のリファレンスカードを機械翻訳 (C:\Program Files\JetBrains\IntelliJ IDEA XXX\help\ReferenceCard.pdf など)
  - キーボード図版  
  http://www.sharots.com/sozai/keyboard.html の図版を自分のキーボードに近い形に加工して使わせていただきました。
  
 
