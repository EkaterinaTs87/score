ball_team1 = 3
ball_team2 = 2


def score_ball(team1, team2):
    if team1 < 0 or team2 < 0:
        return "Количество мячей не может быть отрицательным."

    if team1 > team2:
        result = f"Команда1 выиграла со счетом {team1} : {team2}."
    elif team2 > team1:
        result = f"Команда2 выиграла со счетом {team2} : {team1}."
    else:
        result = f"Ничья со счетом {team1} : {team2}."

    return result


result = score_ball(ball_team1, ball_team2)
print(result)
