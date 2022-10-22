""" trigger/52100300_qd/monsterspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='SpawnRoomEnd', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Spawn', value=1):
            return 스폰1()


class 스폰1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,121,131,141], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 스폰2()


class 스폰2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112,122,132,142], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 스폰5()


# 스폰3, 4는 스킵, 바로 5로 넘어감(1,2,5), 전체적인 전투 시간을 고려하여 밸런스 조정. 추후 수정 가능
class 스폰3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113,123,133,143], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 스폰4()


class 스폰4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114,124,134,144], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 스폰5()


# 필요에 따라 웨이브 하나씩 열어줄 수 있도록 코드 남겨둠.
class 스폰5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115,125,135,145], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115,121,122,123,124,125,131,132,133,134,135,141,142,143,144,145]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='SpawnRoomEnd', value=1)


