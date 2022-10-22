""" trigger/51000003_dg/cannon_projectile.xml """
from common import *
import state


#  플레이어 감지 
#  큐브스킬형 캐논 발사체 
class Round_check(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112,113,114,115,116,117,118])

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
            return Round_05()
        if user_value(key='Round_06', value=1):
            return Round_06()


class Round_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True, arg3=600)
        create_monster(spawnIds=[118], arg2=True, arg3=1500)

    def on_tick(self) -> state.State:
        if user_value(key='Round_02', value=1):
            return Round_02()
        if user_value(key='Reset', value=1):
            return End()


class Round_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114], arg2=True, arg3=700)
        create_monster(spawnIds=[117], arg2=True, arg3=1100)

    def on_tick(self) -> state.State:
        if user_value(key='Round_03', value=1):
            return Round_03()
        if user_value(key='Reset', value=1):
            return End()


class Round_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112], arg2=True, arg3=800)
        create_monster(spawnIds=[116], arg2=True, arg3=1300)

    def on_tick(self) -> state.State:
        if user_value(key='Round_04', value=1):
            return Round_04()
        if user_value(key='Reset', value=1):
            return End()


class Round_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True, arg3=300)
        create_monster(spawnIds=[115], arg2=True, arg3=900)

    def on_tick(self) -> state.State:
        if user_value(key='Round_05', value=1):
            return Round_05()
        if user_value(key='Reset', value=1):
            return End()


class Round_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112,113,114,115,116,117,118])
        create_monster(spawnIds=[101], arg2=True, arg3=1000)
        create_monster(spawnIds=[102], arg2=True, arg3=2000)
        create_monster(spawnIds=[103], arg2=True, arg3=3000)
        create_monster(spawnIds=[104], arg2=True, arg3=4000)
        create_monster(spawnIds=[105], arg2=True, arg3=5000)
        create_monster(spawnIds=[106], arg2=True, arg3=6000)
        create_monster(spawnIds=[107], arg2=True, arg3=7000)
        create_monster(spawnIds=[108], arg2=True, arg3=0)

    def on_tick(self) -> state.State:
        if user_value(key='Round_06', value=1):
            return Round_check()
        if user_value(key='Reset', value=1):
            return End()


class Round_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121], arg2=True, arg3=1000)
        create_monster(spawnIds=[122], arg2=True, arg3=3000)
        create_monster(spawnIds=[123], arg2=True, arg3=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return None # Missing State: Round_06_02
        if user_value(key='Reset', value=1):
            return End()


class End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118])


