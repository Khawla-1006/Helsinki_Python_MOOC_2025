import json

class HockeyPlayer :
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def total_points(self):
        return self.assists + self.goals

    def __str__(self):
        return f"{self.name:21}{self.team}  {self.goals:2} + {self.assists:2} ={self.total_points():4}"

class HockeyApplication:
    def __init__(self):
        self.players = []

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for players")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def get_data(self):
        file = input("file name: ")
        with open(file) as my_file:
            data = my_file.read()
        my_data= json.loads(data)

        for item in my_data :
            item = HockeyPlayer(item["name"],item["nationality"],item["assists"],item["goals"],item["penalties"],item["team"],item["games"])
            self.players.append(item)
        
        print(f"read the data of {len(self.players)} players")

#WE GOT OUR LIST OF OBJECTS YAAAAAAYY !!!!

    def get_player(self):
        name = input("name: ")
        for player in self.players:
            if player.name == name:
                print(player)

    def get_teams(self):
        teams = sorted(set(list(map(lambda player : player.team, self.players))))
        for team in teams :
            print(team) 

    def get_countries(self):
        countries = sorted(set(list(map(lambda player: player.nationality, self.players))))
        for c in countries:
            print(c)

    def players_in_team(self):
        team = input("team: ")
        team_players = sorted(set(list(filter(lambda player: player.team == team,self.players))),key=(lambda player: player.total_points()),reverse=True)
        for player in team_players:
            print(player)

    def player_in_country(self):
        country = input("country: ")
        team_c = sorted(set(list(filter(lambda player: player.nationality == country,self.players))),key=(lambda player: player.total_points()),reverse=True)
        for player in team_c:
            print(player)
    
    def most_points(self):
        n = int(input("how many: "))
        goals_sorted = sorted(self.players,key=(lambda player: player.goals),reverse=True)
        pts_sorted = sorted(goals_sorted, key=(lambda player: player.total_points()),reverse=True)
        for i, player in zip(range(n), pts_sorted):
            print(player)
    #i need to sort a sorted list of players according the higher number of goals

    def most_goals(self):
    #i need to sort a sorted list of players according the higher number of games
        n = int(input("how many: "))
        games_sorted = sorted(self.players,key=(lambda player : player.games))
        goals_sorted = sorted(games_sorted, key=(lambda player : player.goals),reverse=True)
        for i, player in zip(range(n),goals_sorted):
            print(player)


    def execute(self):
        self.get_data()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.get_player()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.player_in_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()

application = HockeyApplication()
application.execute()
