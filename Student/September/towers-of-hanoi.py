# --------------------------------------
# CSCI 127, Lab 2
# September 12, 2017
# Nathan Stouffer
# --------------------------------------

def hanoi_solution(p_start, p_finish, p_middle, p_discs):
    if p_discs > 0:
        hanoi_solution(p_start, p_finish, p_middle, p_discs - 1)
        print("Move disc", p_discs, "from", p_start, "to", p_finish)
        hanoi_solution(p_middle, p_start, p_finish, p_discs - 1)

hanoi_solution("a", "b", "c", 4)
