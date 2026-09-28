#1 
import turtle
kame=turtle.Turtle()

kame.shape("turtle")
kame.shapesize(2,2,5)


for i in range(6):
    kame.forward(100)
    kame.left(60)


turtle.done() #左キープ

"""
答え写した　Tabとか　in とか　rangeとか覚えてなかった
"""

#2
"""
    shapeはキャラ変更
    shapesizeはキャラの大きさ
    forward 前進
    backwardは後退
    lightは右
    leftは左
    circleは円
    undoは一つ前の作業取り消す
    homeは亀戻る
    clearは線全消し
    Window_widthは横幅表示
    postionは亀の座標表示
    gitoはx,y座表に亀移動
    distanceは亀と指定した座標の距離表示
    penupは線なしの亀移動
    pendownは線ありに戻す
    isdownは線ありか確認

あとはrange,while,ifあたりを勉強する

"""