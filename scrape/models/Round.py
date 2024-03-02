class Round:
    def __init__(self, team_loadout: str, enemy_loadout: str, team_score: int, enemy_score: int, map: str, round_outcome, map_outcome):
        self.team_loadout = team_loadout
        self.enemy_loadout = enemy_loadout
        self.team_score = team_score
        self.enemy_score = enemy_score
        self.map = map
        self.round_outcome = round_outcome
        self.map_outcome = map_outcome
