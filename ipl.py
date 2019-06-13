from matplotlib import pyplot as plt
import time
import pandas as pd

import csv


def one():
    with open("matches.csv") as matches_csv:
        matches = csv.DictReader(matches_csv)

        year = {}
        for match in matches:
            season = match.get("season")
            if not year.__contains__(season):
                year[season] = 1
            elif season in year:
                year[season] += 1
        plt.plot(list(year.keys()), list(year.values()))
        plt.ylabel("Matches Played -------")
        plt.xlabel("Years-----------")
        plt.show()


def two():
    start_time = time.time()
    with open("matches.csv") as matches_csv:
        matches = csv.DictReader(matches_csv)

        won_per_year = {}
        for match in matches:
            winner = match["winner"]
            year = match["season"]

            if not list(won_per_year.keys()).__contains__(year):
                won_per_year[year] = {}

            try:
                if not won_per_year[year].keys().__contains__(winner):
                    won_per_year[year][winner] = 1
                else:
                    won_per_year[year][winner] += 1
            except KeyError:
                print("KeyError")

        x_axis = []
        for result in won_per_year:
            for team in won_per_year[result]:
                if not x_axis.__contains__(team):
                    x_axis.append(team)

        index = pd.Index(x_axis)

        df = pd.DataFrame(won_per_year, index=index)
        ax = df.plot(kind='bar', stacked=True, figsize=(17, 10))
        ax.set_ylabel('Total matches won ------------- ')
        plt.xticks(rotation= -70)
        plt.rcParams.update({'font.size': 5})
        print("Execution time in ms: " + str((time.time() - start_time)*1000))

        plt.show()


def three():
    with open("matches.csv") as matches_csv:
        with open("deliveries.csv") as deliveries_csv:
            matches = csv.DictReader(matches_csv)
            deliveries = csv.DictReader(deliveries_csv)
            year = "2016"
            match_id = []
            team_list = {}
            for match in matches:
                try:
                    if match["season"] == year:
                        m_id = match["id"]
                        if not match_id.__contains__(m_id):
                            match_id.append(m_id)

                        team1 = match["team1"]
                        if not team_list.__contains__(team1):
                            team_list[team1] = 0
                except KeyError:
                    pass

            for delivery in deliveries:
                try:
                    m_id = delivery["match_id"]
                    if match_id.__contains__(m_id):
                        bowling_team = delivery["bowling_team"]
                        extra = delivery["extra_runs"]
                        team_list[bowling_team] += int(extra)
                except KeyError:
                    print("Key error for key : " + delivery["match_id"])

            t1 = list(team_list.keys())
            t2 = list(team_list.values())
            plt.rcParams.update({'font.size': 10})

            plt.plot(t1, t2)
            plt.xlabel("Teams in 2016 ------")
            plt.ylabel("Extras scored against these team -------------")
            plt.title("Extras Given by IPL teams in 2016")

            plt.xticks(rotation=-10)
            plt.show()
            print(team_list)


def four():
    with open("matches.csv") as matches_csv:
        with open("deliveries.csv") as deliveries_csv:
            matches = csv.DictReader(matches_csv)
            deliveries = csv.DictReader(deliveries_csv)
            year = "2015"
            match_id = []
            for match in matches:
                try:
                    if match["season"] == year:
                        m_id = match["id"]
                        if not match_id.__contains__(m_id):
                            match_id.append(m_id)
                except KeyError:
                    print("Key Error occured ")

            bowler_balls = {}
            bowler_runs = {}

            for delivery in deliveries:
                temp5 = delivery["match_id"]
                if match_id.__contains__(temp5):
                    try:
                        bowler_name = delivery["bowler"]
                        if not bowler_balls.__contains__(bowler_name):
                            bowler_balls[bowler_name] = 1
                            bowler_runs[bowler_name] = 1
                        elif bowler_balls.__contains__(bowler_name):
                            bowler_balls[bowler_name] += 1
                            bowler_runs[bowler_name] += int(delivery["total_runs"])

                    except KeyError:
                        print("Key error occured")

            bowler_average = {}
            for i in bowler_runs:
                average = float("{0:.2f}".format((bowler_runs[i] / bowler_balls[i])*6))
                bowler_average[i] = average
            sorted_bowler_average = sorted(bowler_average.items(), key=lambda x: x[1])
            top_ten = sorted_bowler_average[:10]

            t1 = []
            t2 = []

            for bowler in top_ten:
                t1.append(bowler[0])
                t2.append(bowler[1])

            plt.rcParams.update({'font.size': 10})

            plt.plot(t1, t2)
            plt.xlabel("Bowlers in IPL 2015 ------")
            plt.ylabel("Economy of bowlers -------------")
            plt.title("Top 10 Economical Bowlers of IPL 2015")

            plt.xticks(rotation=-10)
            plt.show()


def five(player):
    with open("matches.csv") as matches_csv:
        with open("deliveries.csv") as deliveries_csv:
            matches = csv.DictReader(matches_csv)
            deliveries = csv.DictReader(deliveries_csv)

            player_team = []
            player_scored = 0
            player_bowled = 0
            player_of_the_match = 0
            player_dismissed = 0
            player_match_id = []

            for delivery in deliveries:
                if delivery["batsman"] == player:                   # FOR ADDING RUNS AND TEAM OF THE PLAYER

                    if not player_match_id.__contains__(delivery["match_id"]):
                        player_match_id.append(delivery["match_id"])

                    bating_team = delivery["batting_team"]
                    if not player_team.__contains__(bating_team):
                        player_team.append(bating_team)

                    run = delivery["batsman_runs"]
                    player_scored += int(run)

                if delivery["bowler"] == player:                     # FOR ADDING WICKETS AND OVERS OF THE PLAYER
                    if not player_match_id.__contains__(delivery["match_id"]):
                        player_match_id.append(delivery["match_id"])

                    player_bowled += 1
                    if len(delivery["fielder"]) > 0:
                        player_dismissed += 1

            for match in matches:                                # FOR COUNTING 'PLAYER OF THE MATCH' OF THE PLAYER
                if match["player_of_match"] == player:
                    player_of_the_match += 1

            played_team_str = ""

            if len(player_team) > 1:
                for i in range(len(player_team)):
                    played_team_str += player_team[i]
                    if i != len(player_team)-1:
                        played_team_str += ", "

            elif len(player_team) == 1:
                played_team_str = player_team[0]

            final = "Hi i am " + player + ". I have played for " + played_team_str \
                  + " in IPL.\nBetween the year 2008 and 2017 i have scored a total of " \
                    + str(player_scored) + " runs in " + str(len(player_match_id)) + " IPL match.\nI have bowled " + str(int(player_bowled/6)) + "" \
                    + " Overs in which i have got " + str(player_dismissed) + " wickets in  IPL matches."

            if player_of_the_match > 0:
                final += " I have also named player of the match " + str(player_of_the_match) + " times."

            if len(player_team) == 0:
                print("No players found with this name")
            else:
                print(final)



five("V Kohli")