from tools.mahjong_player import MahjongPlayer

class MahjongAI(MahjongPlayer):
    def discardTile(self):
        raise NotImplementedError

    def callKan(self):
        raise NotImplementedError

    def callMinKan(self, tile136):
        raise NotImplementedError

    def callPeng(self, tile136):
        raise NotImplementedError

    def callChi(self,tile136):
        raise NotImplementedError

    def callReach(self):
        raise NotImplementedError

    def deal(self,message):
        raise NotImplementedError