""" trigger/02100004_bf/randomspawner.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RoundStart', value=1):
            return 랜덤스폰()


class 랜덤스폰(state.State):
    def on_enter(self):
        set_user_value(triggerId=999992, key='RoundStart', value=0)

    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return 중복체크01()
        if random_condition(rate=10):
            return 중복체크02()
        if random_condition(rate=10):
            return 중복체크03()
        if random_condition(rate=10):
            return 중복체크04()
        if random_condition(rate=10):
            return 중복체크05()
        if random_condition(rate=10):
            return 중복체크06()
        if random_condition(rate=10):
            return 중복체크08()
        if random_condition(rate=10):
            return 중복체크09()
        if random_condition(rate=10):
            return 중복체크10()
        if random_condition(rate=10):
            return 중복체크11()
        if random_condition(rate=10):
            return 중복체크12()
        if random_condition(rate=10):
            return 중복체크13()


class 중복체크01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned01', value=0):
            set_user_value(triggerId=999101, key='NpcSpawn01', value=1)
            return 대기()
        if user_value(key='NpcSpawned01', value=1):
            return 랜덤스폰()


class 중복체크02(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned02', value=0):
            set_user_value(triggerId=999102, key='NpcSpawn02', value=1)
            return 대기()
        if user_value(key='NpcSpawned02', value=1):
            return 랜덤스폰()


class 중복체크03(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned03', value=0):
            set_user_value(triggerId=999103, key='NpcSpawn03', value=1)
            return 대기()
        if user_value(key='NpcSpawned03', value=1):
            return 랜덤스폰()


class 중복체크04(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned04', value=0):
            set_user_value(triggerId=999104, key='NpcSpawn04', value=1)
            return 대기()
        if user_value(key='NpcSpawned04', value=1):
            return 랜덤스폰()


class 중복체크05(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned05', value=0):
            set_user_value(triggerId=999105, key='NpcSpawn05', value=1)
            return 대기()
        if user_value(key='NpcSpawned05', value=1):
            return 랜덤스폰()


class 중복체크06(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned06', value=0):
            set_user_value(triggerId=999106, key='NpcSpawn06', value=1)
            return 대기()
        if user_value(key='NpcSpawned06', value=1):
            return 랜덤스폰()


class 중복체크08(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned08', value=0):
            set_user_value(triggerId=999108, key='NpcSpawn08', value=1)
            return 대기()
        if user_value(key='NpcSpawned08', value=1):
            return 랜덤스폰()


class 중복체크09(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned09', value=0):
            set_user_value(triggerId=999109, key='NpcSpawn09', value=1)
            return 대기()
        if user_value(key='NpcSpawned09', value=1):
            return 랜덤스폰()


class 중복체크10(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned10', value=0):
            set_user_value(triggerId=999110, key='NpcSpawn10', value=1)
            return 대기()
        if user_value(key='NpcSpawned10', value=1):
            return 랜덤스폰()


class 중복체크11(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned11', value=0):
            set_user_value(triggerId=999111, key='NpcSpawn11', value=1)
            return 대기()
        if user_value(key='NpcSpawned11', value=1):
            return 랜덤스폰()


class 중복체크12(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned12', value=0):
            set_user_value(triggerId=999112, key='NpcSpawn12', value=1)
            return 대기()
        if user_value(key='NpcSpawned12', value=1):
            return 랜덤스폰()


class 중복체크13(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NpcSpawned13', value=0):
            set_user_value(triggerId=999113, key='NpcSpawn13', value=1)
            return 대기()
        if user_value(key='NpcSpawned13', value=1):
            return 랜덤스폰()


class 종료(state.State):
    pass


