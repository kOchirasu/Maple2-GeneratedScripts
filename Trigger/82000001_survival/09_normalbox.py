""" trigger/82000001_survival/09_normalbox.xml """
from common import *
import state


#  다수의 interactObject 동시 스폰하는 경우 렉이 발생함 / 대기 지역에 배치된 나무 상자 그룹만 경기 시작 시점에 스폰 시키는 것으로 구현함 
#  10000040-10000164 나무 상자 Normal Box 
class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000205,10000206,10000207,10000208,10000209,10000210,10000211,10000212,10000213,10000214,10000215,10000216,10000217,10000218,10000219,10000220,10000221,10000222,10000223,10000224,10000225,10000226,10000227,10000228,10000229,10000230,10000231,10000232,10000233,10000234,10000235,10000236,10000237,10000238,10000239,10000240,10000241,10000242,10000243,10000244,10000245,10000246,10000247,10000248,10000249,10000250,10000251,10000252,10000253,10000254,10000255,10000256,10000257,10000258], isStart=True)
        start_combine_spawn(groupId=[10000263,10000265,10000267,10000268,10000269,10000271,10000272,10000274,10000275], isStart=True)
        start_combine_spawn(groupId=[10000277,10000278,10000279,10000280,10000281,10000282,10000283,10000284,10000285,10000286,10000287,10000288,10000289,10000290,10000291,10000292,10000293,10000294,10000295,10000296,10000297,10000298,10000299,10000300,10000301,10000302,10000303,10000304,10000305,10000306,10000307,10000308,10000309,10000310,10000311,10000312,10000313,10000314,10000315,10000316,10000317,10000318,10000319,10000320,10000321,10000322,10000323,10000324,10000325,10000326,10000327,10000328,10000329], isStart=True)
        set_user_value(key='NormaBoxOnCount', value=0)
        set_user_value(key='NormaBoxOff', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='NormaBoxOnCount', value=1):
            return Delay()


class Delay(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000259,10000260,10000261,10000262,10000264,10000266,10000270,10000273,10000276], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='NormaBoxOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000205,10000206,10000207,10000208,10000209,10000210,10000211,10000212,10000213,10000214,10000215,10000216,10000217,10000218,10000219,10000220,10000221,10000222,10000223,10000224,10000225,10000226,10000227,10000228,10000229,10000230,10000231,10000232,10000233,10000234,10000235,10000236,10000237,10000238,10000239,10000240,10000241,10000242,10000243,10000244,10000245,10000246,10000247,10000248,10000249,10000250,10000251,10000252,10000253,10000254,10000255,10000256,10000257,10000258,10000259,10000260,10000261,10000262,10000263,10000264,10000265,10000266,10000267,10000268,10000269,10000270,10000271,10000272,10000273,10000274,10000275,10000276,10000277,10000278,10000279,10000280,10000281,10000282,10000283,10000284,10000285,10000286,10000287,10000288,10000289,10000290,10000291,10000292,10000293,10000294,10000295,10000296,10000297,10000298,10000299,10000300,10000301,10000302,10000303,10000304,10000305,10000306,10000307,10000308,10000309,10000310,10000311,10000312,10000313,10000314,10000315,10000316,10000317,10000318,10000319,10000320,10000321,10000322,10000323,10000324,10000325,10000326,10000327,10000328,10000329], isStart=False) # 10000040-10000329 나무 상자 Normal Box


