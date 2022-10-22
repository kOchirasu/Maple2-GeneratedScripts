""" trigger/02000066_bf/mob01.xml """
from common import *
import state


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[900]):
            return 차타이머1()
        if npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3()
        if npc_detected(boxId=102, spawnIds=[904]):
            return 차타이머4()
        if npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6()
        if npc_detected(boxId=102, spawnIds=[908]):
            return 차타이머7()
        if npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9()
        if npc_detected(boxId=102, spawnIds=[912]):
            return 차타이머10()
        if npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return 대기시간()
        if time_expired(timerId='10'):
            return 생성랜덤()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='9'):
            return 생성랜덤()


class 차타이머4(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=8)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[904]):
            return 대기시간()
        if time_expired(timerId='8'):
            return 생성랜덤()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='7'):
            return 생성랜덤()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='5'):
            return 생성랜덤()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='4'):
            return 생성랜덤()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='3'):
            return 생성랜덤()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='3'):
            return 생성랜덤()


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
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1007], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


