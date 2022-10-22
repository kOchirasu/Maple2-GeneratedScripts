""" trigger/51000003_dg/normal_projectile_02.xml """
from common import *
import state


#  플레이어 감지 
#  직사형 일반발사체 
class Round_check(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01()
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Round_03', value=1):
            return Round_03()
        if user_value(key='Round_04', value=1):
            return Round_04()
        if user_value(key='Round_05', value=1):
            return None # Missing State: Round_05
        if user_value(key='Round_06', value=1):
            return None # Missing State: Round_06


class Round_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[351,352])
        create_monster(spawnIds=[302], arg2=True, arg3=1000)
        create_monster(spawnIds=[303], arg2=True, arg3=2000)

    def on_tick(self) -> state.State:
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


class Round_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[353,354])
        create_monster(spawnIds=[304], arg2=True, arg3=500)
        create_monster(spawnIds=[305], arg2=True, arg3=1500)

    def on_tick(self) -> state.State:
        if user_value(key='Round_03', value=1):
            return Round_03()
        if user_value(key='Reset', value=1):
            return End()


class Round_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[355,356])
        create_monster(spawnIds=[306], arg2=True, arg3=1000)
        create_monster(spawnIds=[301], arg2=True, arg3=2000)

    def on_tick(self) -> state.State:
        if user_value(key='Round_04', value=1):
            return Round_04()
        if user_value(key='Reset', value=1):
            return End()


class Round_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[312], arg2=True, arg3=500)
        create_monster(spawnIds=[311], arg2=True, arg3=1500)

    def on_tick(self) -> state.State:
        if user_value(key='Reset', value=1):
            return End()


class End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])


