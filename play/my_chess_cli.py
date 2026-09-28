#チェスのライブラリーを学ぶ
"""
import chess
   └ チェスの盤面・駒・ルールを扱うライブラリ。
      pip install python-chess で導入できる。

 chess.Board()
   └ 新しいチェス盤を作成。初期配置（白黒の駒が並んだ状態）で開始。

 board.legal_moves
   └ 現在の局面で可能なすべての合法手（Moveオブジェクトの集合）。

 chess.Move.from_uci("e2e4")
   └ "e2e4" のようなUCI形式文字列を Move オブジェクトに変換。
      UCI (Universal Chess Interface): e2e4, g1f3, e7e8q など。

 board.push(move)
   └ Moveオブジェクトを使って盤面を更新（駒を実際に動かす）。

 board.pop()
   └ 最後の一手を取り消して、直前の局面に戻す。

 board.turn
   └ 今どちらの手番かを示す。
      chess.WHITE → 白番, chess.BLACK → 黒番。

 board.is_check()
   └ 現在の局面が「王手」かどうかを判定。

 board.is_checkmate()
   └ チェックメイト（詰み）なら True。

 board.is_stalemate()
   └ ステイルメイト（合法手がないが王手でもない引き分け）なら True。

 board.is_insufficient_material()
   └ 両者が詰み不可能（例: 王だけ同士など）なら引き分け扱い。

 board.can_claim_fifty_moves()
  └ 50手ルール（駒取りもポーン動かしも50手ない）による引き分けが成立可能か。

 board.can_claim_threefold_repetition()
   └ 同じ局面が3回出た場合にドローを主張できるか。

 print(board)
   └ 盤面をASCII文字で出力（例: ターミナルに表示用）。
"""

# chess_cli.py
import chess
import chess.svg
import random
import sys

def print_board(board):
    # board表示
    print(board)  # python-chess の ASCII 表示

#
def ask_move(board, prompt):
    while True:#無限ループ開始
        mv = input(prompt).strip()#固定入力待ち

        if mv == "help":
            print("Commands: help, resign, draw, undo, ai, quit")#利用コマンド表示
            print("Move format: UCI (e2e4, g1f3, e7e8q for promotion).")#指し（UCI）の説明表示
            continue#もう一度固定入力待ち
        if mv == "resign":#投了
            return "resign"
        if mv == "draw":#引き分け
            return "draw"
        if mv == "undo":#一手戻す
            return "undo"
        if mv == "ai":#ai切り替え
            return "ai"
        if mv == "quit":#終了
            sys.exit(0)

        # 指し手入力
        try:#例外処理開始
            move = chess.Move.from_uci(mv)#文字列を動きに変換
        except Exception:#例外キャッチ
            print("Invalid UCI format. Try again or type 'help'.")
            continue
        if move in board.legal_moves:#変換に成功した move が現在の盤で合法手かをチェック
            return move
        else:
            print("Illegal move. Try again.")

#AI関数
def random_ai_move(board):
    moves = list(board.legal_moves)#現在の盤の合法手リスト化
    return random.choice(moves) if moves else None#あれば返す。なければNoneでパス

#
def main():
    board = chess.Board()#チェス盤初期配置
    use_ai_for_black = False#人対人をデフォルト化
    print("Simple Chess CLI (python-chess)")#起動メッセージ
    print("Type 'help' for commands. By default two-player.")#案内とデフォルトが二人プレイ表示
    print("To switch black to AI, type 'ai' when prompted for a move by White or set at start (see below).")#Ai切り替え案内
    
    #開始
    # AIとするかyes/no 
    init = input("Play vs random-AI? (y/n) > ").strip().lower()
    if init == "y":
        use_ai_for_black = True

    history = []#一手戻るための記憶装置

    while True:
        print_board(board)#盤表示
        if board.is_check():#チェックメイト確認
            print("Check!")

        turn = "White" if board.turn == chess.WHITE else "Black"#手番表示
        prompt = f"{turn} move > "#白か黒の番か表示

        # 黒がAIの時の処理
        if board.turn == chess.BLACK and use_ai_for_black:
            mv = random_ai_move(board)
            if mv is None:
                break
            print(f"AI (Black) plays: {mv.uci()}")#Aiの選んだ手をUCI表示
            board.push(mv)#手を適用
            history.append(mv)#記録
        else:
            res = ask_move(board, prompt)
            if res == "resign":#ask_move を呼んでユーザー入力を受け取る
                print(f"{turn} resigns. {'Black' if turn=='White' else 'White'} wins.")
                break
            if res == "draw":
                print("Draw offered/accepted. Game ends as draw.")
                break
            if res == "undo":
                if history:#記録確認_空出ないか
                    board.pop()#履歴から最後の手を削除
                    history.pop()
                    if history: # pop twice to undo both moves if desired? Here single undo.
                        pass
                    print("Undid last move.")
                else:
                    print("No moves to undo.")
                continue
            if res == "ai":#ai切り替え
                # toggle AI for the other side
                use_ai_for_black = not use_ai_for_black#use_ai_for_black をトグル（True⇄False）する。
                print("Toggled AI for Black to:", use_ai_for_black)
                continue
            #  moveが返ってきた場合 (chess.Move)
            move = res
            board.push(move)
            history.append(move)

        # game end checks
        if board.is_checkmate():#チェックメイト判断
            print_board(board)#盤面表示
            winner = "White" if board.turn == chess.BLACK else "Black"
            print("Checkmate! Winner:", winner)#勝ち表示
            break
        if board.is_stalemate():
            print_board(board)
            print("Stalemate — draw.")
            break
        if board.is_insufficient_material():
            print_board(board)
            print("Insufficient material — draw.")
            break
        if board.can_claim_fifty_moves():
            print_board(board)
            print("50-move rule can be claimed — draw.")
            break
        if board.can_claim_threefold_repetition():#3回反復）主張可能か判定
            print_board(board)
            print("Threefold repetition can be claimed — draw.")
            break

if __name__ == "__main__":
    main()
