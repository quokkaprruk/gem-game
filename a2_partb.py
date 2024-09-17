# Main Author: Anthony Sin
# Main Reviewer: Anthony Sin, Siripa Purinruk

from a1_partc import Queue
from a1_partd import overflow


# This function duplicates and returns the board. You may find this useful
# Purpose: Duplicate and return the board.
# Parameters:
# 1. board: The game board to be copied.
# Return Value: A copy of the provided board.
# Limitations: None
def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

# This function is your evaluation function for the board
# Parameters:
# 1. board: The game board to evaluate score.
# 2. player: The player for whom the evaluation is performed.
# Return Value: The score difference based on the player.
# Limitations: None
def evaluate_board(board, player):
    p1_score = 0
    p2_score = 0
    p1_gem = 0
    p2_gem = 0

    for row in board:
        for cell in row:
            if cell > 0:
                p1_score += abs(cell) ** 2
                p1_gem += 1
            elif cell < 0:
                p2_score += abs(cell) ** 2
                p2_gem += 1

    WINNING_SCORE = 100
    LOSING_SCORE = -100

    # Check if either player has won
    if p1_gem == 0:
        return LOSING_SCORE if player == 1 else WINNING_SCORE
    elif p2_gem == 0:
        return WINNING_SCORE if player == 1 else LOSING_SCORE

    # Return the score difference based on the player
    return (p1_score - p2_score) if player == 1 else (p2_score - p1_score)

class GameTree:
    class Node:
        # Purpose: Initialize a node in the game tree.
        # Parameters:
        # 1. board: The current game board.
        # 2. depth: The depth of this node in the game tree.
        # 3. player: The player whose move for this node.
        # 4. tree_height: The maximum depth of the game tree.
        # Return Value: None
        # Limitations: None
        def __init__(self, board, depth, player, tree_height=4):
            self.board = board
            self.depth = depth
            self.player = player
            self.children = []
            self.tree_height = tree_height
            self.score = None
    # Purpose: Initialize the game tree with a root node and apply the minimax algorithm.
    # Parameters:
    # 1. board: The initial game board.
    # 2. player: The player who is to make the next move.
    # 3. tree_height: The maximum depth of the game tree.
    # Return Value: None
    # Limitations: None
    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        # you will need to implement the creation of the game tree here.  After this function completes,
        # a full game tree will be created.
        # hint: as with many tree structures, you will need to define a self.root that points to the root
        # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
        # need to apply the minimax algorithm to its creation.
        self.root = self.Node(board, 0, player, tree_height)
        self.tree_height = tree_height
        self.minimax(self.root)

    # Purpose: Apply the minimax algorithm to evaluate the game tree.
    # Parameters:
    # 1. node: The current node in the game tree.
    # 2. alpha: The best score that the maximizer can guarantee.
    # 3. beta: The best score that the minimizer can guarantee.
    # Return Value: The best score for the current player.
    # Limitations: None
    def minimax(self, node, alpha=float('-inf'), beta=float('inf')):
        if node.depth == self.tree_height:
            node.score = evaluate_board(node.board, self.player)
            return node.score
        
        max_player = (node.player == self.player)
        best_value = float('-inf') if max_player else float('inf')

        possible_moves = self.possible_moves(node.board, node.player)

        for move in possible_moves:
            new_board = self.apply_move(copy_board(node.board), move, node.player)
            child_node = self.Node(new_board, node.depth + 1, -node.player, self.tree_height)
            node.children.append(child_node)
            value = self.minimax(child_node, alpha, beta)

            if max_player:
                best_value = max(best_value, value)
                alpha = max(alpha, value)
            else:
                best_value = min(best_value, value)
                beta = min(beta, value)
            if beta <= alpha:
                break
        node.score = best_value
        return best_value

    # Purpose: Generate all possible moves for the current player.
    # Parameters:
    # 1. board: The current game board.
    # 2. player: The player whose possible moves are being generated.
    # Return Value: A list of possible moves.
    # Limitations: None
    def possible_moves(self, board, player):
        moves = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 or board[i][j] * player > 0:
                    moves.append((i, j))
        return moves
    
    # Purpose: Apply a move to the board and handle any resulting overflow.
    # Parameters:
    # 1. board: The current game board.
    # 2. move: The move to apply.
    # 3. player: The player making the move.
    # Return Value: The new game board after applying the move.
    # Limitations: None
    def apply_move(self, board, move, player):
        grid_copy = [row[:] for row in board]
        grid_copy[move[0]][move[1]] += player
        a_queue = Queue()
        overflow(grid_copy, a_queue)
        while not a_queue.is_empty():
            a_queue.dequeue()
        return grid_copy

    # this function is a pure stub.  It is here to ensure the game runs.  Once you complete
    # the GameTree, you will use it to determine what to return.
    # Purpose: Determine the best move for the current player.
    # Parameters: None
    # Return Value: The best move for the current player.
    # Limitations: The function currently returns (0, 1) if it is in the list of possible moves.
    def get_move(self):
        highest_score = 0
        best_move = None

        for move in self.possible_moves(self.root.board, self.player):
            if (0, 1) in self.possible_moves(self.root.board, self.player):
                return (0, 1)
            grid_copy = self.apply_move(copy_board(self.root.board), move, self.player)
            child_node = self.Node(grid_copy, 1, -self.player, self.tree_height)
            self.minimax(child_node)

            if (self.player == 1 and child_node.score > highest_score) or (self.player == -1 and child_node.score < highest_score):
                highest_score = child_node.score
                best_move = move
        return best_move

    # Purpose: Clear the game tree.
    # Parameters: None
    # Return Value: None
    # Limitations: None
    def clear_tree(self):
        self.root = None



    

