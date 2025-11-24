history = {'TeamA': ['W', 'W', 'L', 'D', 'W'],'TeamB': ['D', 'W', 'W', 'L', 'L']}

def calculate_points(results):
    points = 0
    for result in results:
        if result == 'W':
            points += 3
        elif result == 'D':
            points += 1
    return points

def predict(team1, team2):
    points_team1 = calculate_points(match_history[team1])
    points_team2 = calculate_points(match_history[team2])
    print(f"{team1} points: {points_team1}, {team2} points: {points_team2}")
    if points_team1 > points_team2:
        return f"{team1} predicted to win"
    elif points_team2 > points_team1:
        return f"{team2} predicted to win"
    else:
        return "Predicted: Draw"

print(predict_winner('TeamA', 'TeamB'))
