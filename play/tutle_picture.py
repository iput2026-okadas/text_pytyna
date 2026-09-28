#!/usr/bin/env python3
"""
photo2turtle.py
写真を輪郭化して turtle でなぞるスクリプト

使い方例:
  python3 photo2turtle.py --input photo.jpg --method opencv --scale 0.8 --threshold 50 --speed 0

依存:
  Pillow が必要 (pip install pillow)
  OpenCV を使う場合は opencv-python (pip install opencv-python) あるいは opencv-python-headless
"""

import argparse#コマンド因数
import sys#Python インタプリタに関する機能を提供
import math#数学関数（平方根・三角関数・円周率など）を使える
from PIL import Image, ImageFilter, ImageOps#Pillow（ピロー）**という画像処理ライブラリから3つのモジュールを読み込

"""tutleインポート出来ない場合"""
try:
    import turtle
except Exception as e:#eは例外オブジェクトを受け取る
    print("turtle をインポートできませんでした。GUI 環境が必要です。", e)
    sys.exit(1)

"""
img_path：読み込む画像ファイルへのパス（文字列）。
scale：後で描画時に画像を縮小／拡大するための倍率（1.0 = 原寸）。
threshold：二値化（白黒化）する際の閾値（0〜255）。ここではエッジ画像を白/黒にするために使う想定。
speed：turtle の描画速度（0 が最速、1〜10 が遅い方）。
invert：エッジ画像を反転するかどうかのブール値（True/False）
"""



'''画像ファイル（写真）を読み込み → 輪郭を検出 → turtle で線をなぞる'''
def pillow_method(img_path, scale=1.0, threshold=50, speed=3, invert=False):
    img = Image.open(img_path)
    # グレースケール → エッジ検出（Pillow の FIND_EDGES を重ねる）   
    img = img.convert("L")#光の強さ調節

    # 軽めにぼかしてノイズを減らす（オプション）
    img = img.filter(ImageFilter.GaussianBlur(radius=1)) #radius=1 はぼかしの強さ（半径）で、小さめの値
    edge = img.filter(ImageFilter.FIND_EDGES)
    if invert:
        edge = ImageOps.invert(edge)
    # 二値化
    edge = edge.point(lambda p: 255 if p > threshold else 0)
    w, h = edge.size
    # 縮尺
    w_s = int(w * scale)
    h_s = int(h * scale)
    edge = edge.resize((w_s, h_s), Image.NEAREST)
    pixels = edge.load()

    # turtle 初期化
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("photo2turtle (Pillow)")
    screen.setup(width=min(1200, w_s + 100), height=min(800, h_s + 100))
    screen.setworldcoordinates(0, h_s, w_s, 0)  # 画像座標系に合わせる（左上が 0,0）
    t.hideturtle()
    t.speed(speed)
    t.width(1)

    # 行スキャン法：各行の連続する白ピクセル（エッジ）を線で描画
    for y in range(h_s):
        x = 0
        while x < w_s:
            # find start of run
            while x < w_s and pixels[x, y] == 0:
                x += 1
            if x >= w_s:
                break
            start = x
            while x < w_s and pixels[x, y] != 0:
                x += 1
            end = x - 1
            # 描画（小さな線分）
            t.up()
            t.goto(start + 5, y + 5)
            t.down()
            t.goto(end + 5, y + 5)
        # optional: allow screen update
    screen.update()
    turtle.done()

def opencv_method(img_path, scale=1.0, threshold1=100, threshold2=200, approx_eps=2.0, speed=0, invert=False):
    # opencv がない場合は案内する
    try:
        import cv2
        import numpy as np
    except Exception as e:
        print("OpenCV (cv2) が必要です。pip install opencv-python などで入れてください。")
        raise

    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 軽くぼかし
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    # Canny エッジ
    edges = cv2.Canny(gray, threshold1, threshold2)
    if invert:
        edges = cv2.bitwise_not(edges)
    # 輪郭抽出
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # スケール変換
    h, w = edges.shape[:2]
    w_s = int(w * scale)
    h_s = int(h * scale)

    # turtle 初期化
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("photo2turtle (OpenCV)")
    screen.setup(width=min(1400, w_s + 200), height=min(900, h_s + 200))
    screen.setworldcoordinates(0, h_s, w_s, 0)  # 画像座標系
    t.hideturtle()
    t.speed(speed)
    t.width(1)

    # 輪郭ごとに近似して描画
    for cnt in contours:
        if cnt.shape[0] < 6:
            continue
        # 近似
        epsilon = approx_eps
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if approx is None or len(approx) < 2:
            continue
        # 大きすぎる輪郭は省く（ノイズ低減）
        area = cv2.contourArea(cnt)
        if area < 10:
            continue
        # 描画
        pts = [(int(p[0][0] * scale), int(p[0][1] * scale)) for p in approx]
        t.up()
        t.goto(pts[0][0] + 0.5, pts[0][1] + 0.5)
        t.down()
        for (x,y) in pts[1:]:
            t.goto(x + 0.5, y + 0.5)
        # close path
        t.goto(pts[0][0] + 0.5, pts[0][1] + 0.5)

    screen.update()
    turtle.done()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True, help="入力画像ファイルパス")
    p.add_argument("--method", "-m", choices=("pillow","opencv"), default="pillow", help="処理方法")
    p.add_argument("--scale", type=float, default=0.6, help="描画スケール（1.0=原寸）")
    p.add_argument("--threshold", type=int, default=50, help="Pillow 二値化閾値（pillow 方法）")
    p.add_argument("--canny1", type=int, default=100, help="Canny low threshold (opencv)")
    p.add_argument("--canny2", type=int, default=200, help="Canny high threshold (opencv)")
    p.add_argument("--approx", type=float, default=2.0, help="輪郭近似 eps (opencv)")
    p.add_argument("--speed", type=int, default=2, help="turtle speed (0=fastest..10=slow)")
    p.add_argument("--invert", action="store_true", help="エッジ画像を反転（白→黒）")
    args = p.parse_args()

    if args.method == "pillow":
        pillow_method(args.input, scale=args.scale, threshold=args.threshold, speed=args.speed, invert=args.invert)
    else:
        opencv_method(args.input, scale=args.scale, threshold1=args.canny1, threshold2=args.canny2, approx_eps=args.approx, speed=args.speed, invert=args.invert)

if __name__ == "__main__":
    main()
