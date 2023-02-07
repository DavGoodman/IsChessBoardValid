





def IsChessValid(board):
    piece_count = {"white_pieces": 0, "black_pieces": 0, "white_pawns": 0, "black_pawns": 0,
                   "white_king": 0, "black king": 0}

    a_h = ["a", "b", "c", "d", "e", "f", "g", "h"]
    num = [1, 2, 3, 4, 5, 6, 7, 8, "_"]
    Chess = True
    for k, v in board.items():
        if v[0] != "w" and v[0] != "b" and v != "_":
            Chess = False
            break

        if v[0] == "w":
            piece_count["white_pieces"] += 1
            if piece_count["white_pieces"] > 16:
                Chess = False
                break
        if v[0] == "b":
            piece_count["black_pieces"] += 1
            if piece_count["black_pieces"] > 16:
                Chess = False
                break

        if v == "wp":
            piece_count["white_pawns"] += 1
            if piece_count["white_pawns"] > 8:
                Chess = False
                break
        if v == "bp":
            piece_count["black_pawns"] += 1
            if piece_count["black_pawns"] > 8:
                Chess = False
                break

        if v == "wk":
            piece_count["white_king"] += 1
            if piece_count["white_king"] > 1:
                Chess = False
                break
        if v == "bk":
            piece_count["black king"] += 1
            if piece_count["black king"] > 1:
                Chess = False
                break

        if k[1] not in a_h or int(k[0]) not in num:
            Chess = False
            break
    return Chess



board = { "8a": "br", "8b": "bkn", "8c": "bb", "8d": "bq", "8e": "bk", "8f": "bb", "8g": "bkn", "8h": "br",
          "7a": "bp", "7b": "bp", "7c": "bp", "7d": "bp", "7e": "bp", "7f": "bp", "7g": "bp", "7h": "bp",
          "6a": "_", "6b": "_", "6c": "_", "6d": "_", "6e": "_", "6f": "_", "6g": "_", "6h": "_",
          "5a": "_", "5b": "_", "5c": "_", "5d": "_", "5e": "_", "5f": "_", "5g": "_", "5h": "_",
          "4a": "_", "4b": "_", "4c": "_", "4d": "_", "4e": "_", "4f": "_", "4g": "_", "4h": "_",
          "3a": "_", "3b": "_", "3c": "_", "3d": "_", "3e": "_", "3f": "_", "3g": "_", "3h": "_",
          "2a": "wp", "2b": "wp", "2c": "wp", "2d": "wp", "2e": "wp", "2f": "wp", "2g": "wp", "2h": "wp",
          "1a": "wr", "1b": "wkn", "1c": "wb", "1d": "wq", "1e": "wk", "1f": "wb", "1g": "wkn", "1h": "wr"
}
print(IsChessValid(board))

