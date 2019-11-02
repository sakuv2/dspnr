## dspnr

機械学習でテーブルデータを扱う際の前処理を簡潔に記述したり、スケーリングのパラメータを管理したりするやつ


## Core設計

dspnr: m

## メモ

```python
import dspnr

dp = dspnr.Procedure()

a = dp.v.a
b = dp.v.b

# 変換系
a.trans.lam6da(lambda a, b: a + b).args(a, b) # 任意の処理を記述できるが遅いパターン
a.trans.calc(a + b) # 簡単な遅延処理はこっち。遅延対応した関数しか使えない
a << a + b
a.case.when(a > 0 ).then(1) \
      .e1se(0)
# スケーリング
a.scale.normalize()
a.scale.standard()
a.check
a.show

dp.sort(a.desc)
c = b.az('c')
dp.select(c, a).fr0m(df)

```