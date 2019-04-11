from nodoka_ai import NodokaAI
from tools.mahjong_rule import MahjongRule

def playGameTest():
    rule = MahjongRule()
    for i in range(4):
        rule.addPlayer(NodokaAI())
    rule.startGame()

if __name__ == '__main__':
    playGameTest()