def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
        if board[x][col] == num:
            return False
        if board[3*(row//3) + x//3][3*(col//3) + x%3] == num:
            return False
    
    # 対角線上のチェックを追加
    if row == col:  # 主対角線
        for x in range(9):
            if board[x][x] == num:
                return False
    if row + col == 8:  # 副対角線
        for x in range(9):
            if board[x][8-x] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_sudoku_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        print(" ".join([' ' if x == 0 else str(x) for x in row[:3]]) + " | " +
              " ".join([' ' if x == 0 else str(x) for x in row[3:6]]) + " | " +
              " ".join([' ' if x == 0 else str(x) for x in row[6:]]))

def get_user_input():
    sudoku_board = []  # 数独ボードの初期化
    print("解きたい数独を行ごとに入れてください。空白セルは0として、スペースなしで9つの数字を入力してください。")
    for i in range(9):
        while True:  # 正しい入力が得られるまでループ
            row = input(f"行 {i+1}: ")  # ユーザーからの入力を受け取る
            if len(row) == 9 and row.isdigit():  # 入力が9桁の数字であることを確認
                row_numbers = [int(num) for num in row]  # 入力された行を数値のリストに変換
                sudoku_board.append(row_numbers)  # 変換したリストを数独ボードに追加
                break  # 正しい入力が得られたのでループを抜ける
            else:
                print("入力が不正です。9つの数字をスペースなしで入力してください。")
    return sudoku_board

def prompt_for_reentry():
    while True:
        check = input("こちらの数独でよろしいですか？ y/n: ")
        if check == "y":
            return True
        elif check == "n":
            return False
        else:
            print("yかnで答えてください。")

def main():
    while True:
        sudoku_board = get_user_input()  # ユーザーからの入力を取得
        print("\n入力された数独ボード:")
        print_sudoku_board(sudoku_board)  # 入力されたボードを表示

        if prompt_for_reentry():
            if solve_sudoku(sudoku_board):
                print("\n解かれた数独ボード:")
                print_sudoku_board(sudoku_board)  # 解かれたボードを表示
                break
            else:
                print("解けませんでした。")
                break
        else:
            print("数独を再入力してください。")

if __name__ == "__main__":
    main()
