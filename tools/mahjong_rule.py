from tools.mahjong_table import MahjongTable
import random

class MahjongRule:

    def __init__(self,init_score = 25000,init_wind = 0,init_wind_num = 1,red_dora = True):
        """
        init_score:玩家初始分数
        init_wind:初始场风
        init_wind_num:进行场风数
        """
        # 玩家初始分数
        self.init_players_score = init_score
        # 初始场风
        self.init_wind = init_wind
        # 结束场风
        self.end_wind = (self.init_wind + init_wind_num) % 4
        # 是否有红宝牌
        self.red_dora = red_dora
        # 玩家列表
        self.players = []
        # 玩家目前分数
        self.players_score = None
        # 目前场风
        self.wind = None
        # 目前桌子
        self.table = MahjongTable()
        # 初始庄家
        self.init_banker = None
        # 目前庄家
        self.banker = None

    def addPlayer(self,player):
        """
        添加玩家
        返回是否添加成功
        """
        if len(self.players) > 3:
            return False
        self.players.append(player)

    def initPlayers(self,players):
        """
        初始化玩家列表
        """
        for player in players:
            self.addPlayer(player)

    def checkGameStart(self):
        """
        检查目前游戏是否可以开始
        """
        if not len(self.players) == 4:
            return False
        return True

    def __gameInit(self):
        """
        初始化游戏
        """
        self.players_score = [self.init_players_score] * 4
        self.wind = self.init_wind
        # 初始化庄家
        self.__initBanker()

    def __initBanker(self):
        """
        初始化庄家
        """
        self.init_banker = random.randint(0,4)

    def __checkBanker(self):
        """
        确认庄家
        """
        pass

    def __gameNextInit(self,last_game_message):
        """
        游戏初始化
        """
        if last_game_message['winner'] == None:
            # 初始化游戏
            pass

    def startGame(self):
        """
        开始游戏
        """
        if not self.checkGameStart():
            print('MahjongRule Error:Not enough players!')
            return False
        # 初始化游戏
        self.__gameInit()
        # 初始化上次游戏信息
        last_game_message = {'winner':None,'score_diff':None,'fan':None,'fu':None}
        self.__gameNextInit(last_game_message)