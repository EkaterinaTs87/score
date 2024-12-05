ball_Argentina = 5
ball_Jamaica = 0


def score_ball(Argentina, Jamaica):
    if Argentina < 0 or Jamaica < 0:
        return "Количество мячей не может быть отрицательным!"

    if Argentina > Jamaica:
        result = f"Какая боль! Какая боль! Аргентина - Ямайка {Argentina} : {Jamaica}!"
    elif Jamaica > Argentina:
        result = f"Ямайка выиграла со счётом {Jamaica} : {Argentina}"
    else:
        result = f"Ничья со счётом {Argentina} : {Jamaica}"

    return result


result = score_ball(ball_Argentina, ball_Jamaica)
print(result)
