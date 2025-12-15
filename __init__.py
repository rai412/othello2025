# Generation ID: Hutch_1764573603248_dopxjwac5 (前半)

def myai(board, color):
    """
    オセロの最適な着手位置を返す関数
    minimax法とαβプルーニングを使用した高度なAI
    """
    BLACK = 1
    WHITE = 2
    opponent = WHITE if color == BLACK else BLACK

    def get_board_size(b):
        return len(b)

    def is_valid_move(b, col, row, c):
        size = get_board_size(b)
        if col < 0 or col >= size or row < 0 or row >= size:
            return False
        if b[row][col] != 0:
            return False

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dx, dy in directions:
            x, y = col + dx, row + dy
            if 0 <= x < size and 0 <= y < size and b[y][x] == opponent:
                while 0 <= x < size and 0 <= y < size:
                    if b[y][x] == 0:
                        break
                    if b[y][x] == c:
                        return True
                    x += dx
                    y += dy
        return False

    def get_valid_moves(b, c):
        size = get_board_size(b)
        moves = []
        for row in range(size):
            for col in range(size):
                if is_valid_move(b, col, row, c):
                    moves.append((col, row))
        return moves

    def apply_move(b, col, row, c):
        size = get_board_size(b)
        new_board = [row[:] for row in b]
        new_board[row][col] = c

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dx, dy in directions:
            x, y = col + dx, row + dy
            to_flip = []
            while 0 <= x < size and 0 <= y < size and new_board[y][x] == opponent:
                to_flip.append((x, y))
                x += dx
                y += dy
            if 0 <= x < size and 0 <= y < size and new_board[y][x] == c and to_flip:
                for fx, fy in to_flip:
                    new_board[fy][fx] = c
        return new_board

    def evaluate(b, c):
        opp = WHITE if c == BLACK else BLACK
        score = 0
        size = get_board_size(b)

        corner_weight = 100
        edge_weight = 10
        normal_weight = 1

        corners = [(0,0), (size-1,0), (0,size-1), (size-1,size-1)]
        for cx, cy in corners:
            if b[cy][cx] == c:
                score += corner_weight
            elif b[cy][cx] == opp:
                score -= corner_weight

        for i in range(size):
            if b[0][i] == c:
                score += edge_weight
            elif b[0][i] == opp:
                score -= edge_weight
            if b[size-1][i] == c:
                score += edge_weight
            elif b[size-1][i] == opp:
                score -= edge_weight
            if b[i][0] == c:
                score += edge_weight
            elif b[i][0] == opp:
                score -= edge_weight
            if b[i][size-1] == c:
                score += edge_weight
            elif b[i][size-1] == opp:
                score -= edge_weight

        for row in range(size):
            for col in range(size):
                if b[row][col] == c:
                    score += normal_weight
                elif b[row][col] == opp:
                    score -= normal_weight

        return score

    def minimax(b, depth, c, is_maximizing, alpha, beta):
        moves = get_valid_moves(b, c if is_maximizing else opponent)

        if depth == 0 or not moves:
            return evaluate(b, color), None

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for col, row in moves:
                new_b = apply_move(b, col, row, c)
                eval_score, _ = minimax(new_b, depth - 1, c, False, alpha, beta)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = (col, row)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for col, row in moves:
                new_b = apply_move(b, col, row, opponent)
                eval_score, _ = minimax(new_b, depth - 1, c, True, alpha, beta)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = (col, row)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    valid_moves = get_valid_moves(board, color)
    if not valid_moves:
        return None

    depth = 6 if len(board) == 6 else 5
    _, best_move = minimax(board, depth, color, True, float('-inf'), float('inf'))

    return best_move if best_move else valid_moves[0]

# Generation ID: Hutch_1764573603248_dopxjwac5 (後半)
