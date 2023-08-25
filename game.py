import chess
import chess.engine

stockfish_url = "C:\\Users\\stutzc\\PycharmProjects\\chessalgo\\ChessEngine\\StockFish"

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_url)  # Replace with path to Stockfish engine

    def is_move_legal(self, move_str):
        move = chess.Move.from_uci(move_str)
        return move in self.board.legal_moves

    def evaluate_move(self, move_str):
        move = chess.Move.from_uci(move_str)
        with self.engine.analysis(self.board, multipv=1) as analysis:
            for info in analysis:
                if info.get("pv", [])[0] == move:
                    return info.get("score", {}).get("cp", 0) / 100.0
        return 0.0

    def moves_until_checkmate(self):
        try:
            result = self.engine.analyse(self.board, limit=chess.engine.Limit(time=2.0))
            if "mate" in result.get("score", {}).get("mate", ""):
                return int(result.get("score", {}).get("mate", "0"))
            else:
                return None
        except:
            return None

    def play_game(self):
        while not self.board.is_game_over():
            print(self.board)
            move_str = input("Enter your move in UCI format (e.g., 'e2e4'): ")

            if self.is_move_legal(move_str):
                self.board.push(chess.Move.from_uci(move_str))
                print("Move evaluation score: {:.2f}".format(self.evaluate_move(move_str)))
                moves_to_mate = self.moves_until_checkmate()
                if moves_to_mate is not None:
                    print("Approximately {} moves until checkmate.".format(moves_to_mate))
            else:
                print("Illegal move! Try again.")

        print("Game over! Result: {}".format(self.board.result()))