# Sudoku Solver Collection

このリポジトリには、標準的な数独とクロス数独の問題を解くためのPythonスクリプトが含まれています。

## ファイル

- `normal_sudoku.py`: 標準的な9x9の数独パズルを解くスクリプトです。
- `cross_sudoku.py`: クロス数独パズルを解くスクリプトです。クロス数独は、標準的な数独に加えて、2つの大きな対角線上にも1から9までの数字が重複しないという追加のルールがあります。

## 機能

- 9x9の数独ボードを解く
- 対角線上の数字が重複しないルールを考慮
- ユーザーが数独のパズルを入力
- 解けない数独があれば、その旨を通知

## 使用方法

プロジェクトをローカルにクローンまたはダウンロードした後、以下のコマンドを実行してください。
プログラムが起動したら、指示に従って数独パズルを行ごとに入力してください。空白セルは`0`として、スペースなしで9つの数字を入力してください。

解きたい数独を全て入力した後、プログラムは解を計算し、結果を表示します。

## 入力例
行 1: 530070000
行 2: 600195000
行 3: 098000060
行 4: 800060003
行 5: 400803001
行 6: 700020006
行 7: 060000280
行 8: 000419005
行 9: 000080079

