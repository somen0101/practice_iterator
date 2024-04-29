class BaseballTeam:
    def __init__(self, name, prefecture, total_player):
        self.name = name
        self.prefecture = prefecture
        self.total_player = total_player
        self._player = []
    
    #演算子のオーバーライド
    def __iter__(self):
        return iter(self._player)
    
    #演算子のオーバーライド
    def __str__(self):
        return "チーム名:%s, 所在地:%s, 選手数:%s" % (self.name, self.prefecture, self.total_player)
    
    def get_region_by_prefecture(self):
        if self.prefecture == '兵庫県':
            return '西日本'
        else:
            return '東日本'

    