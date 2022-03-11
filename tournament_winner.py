# problem
    # find out which team won.
    # 0 means away team won and 1 means home team won

#logic
    # maintain hashtable of teams and score and currentBestTeam

# O(n) time O(k) space --> k is number of teams
def tournamentWinner(competitions, result):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for idx, competition in enumerate(competitions):
        home_team, away_team = competition

        winningTeam = home_team if result[idx] == 1 else away_team

        if winningTeam in scores:
            scores[winningTeam] += 3
        else:
            scores[winningTeam] = 3

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


if __name__ == "__main__":
    competitions = [
        ['HTML', 'C#'],
        ['C#', 'Python'],
        ['Python', 'HTML']
    ]
    result = [0, 0, 1]
    print(tournamentWinner(competitions, result))