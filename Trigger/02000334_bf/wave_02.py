""" trigger/02000334_bf/wave_02.xml """
from common import *
import state


#  플레이어 감지 
class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[151]):
            return 차타이머1()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 생성랜덤()


#  몬스터 랜덤 생성 
class 생성랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=12):
            return 번생성1()
        if random_condition(rate=13):
            return 번생성2()
        if random_condition(rate=12):
            return 번생성3()
        if random_condition(rate=13):
            return 번생성4()
        if random_condition(rate=12):
            return 번생성5()
        if random_condition(rate=13):
            return 번생성6()
        if random_condition(rate=12):
            return 번생성7()
        if random_condition(rate=13):
            return 번생성8()


class 번생성1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


