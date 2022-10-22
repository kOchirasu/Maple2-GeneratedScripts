""" trigger/02000334_bf/wave_01.xml """
from common import *
import state


#  플레이어 감지 
class 시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[150]):
            return 생성랜덤()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[150]):
            return 차타이머1()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 생성랜덤()


#  몬스터 랜덤 생성 
class 생성랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=3):
            return 번생성1()
        if random_condition(rate=12):
            return 번생성2()
        if random_condition(rate=12):
            return 번생성3()
        if random_condition(rate=12):
            return 번생성4()
        if random_condition(rate=12):
            return 번생성5()
        if random_condition(rate=12):
            return 번생성6()
        if random_condition(rate=12):
            return 번생성7()
        if random_condition(rate=12):
            return 번생성8()


class 번생성1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


