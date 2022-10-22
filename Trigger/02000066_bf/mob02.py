""" trigger/02000066_bf/mob02.xml """
from common import *
import state


# 디펜스 모드 :  해골A
class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[900]):
            return 차타이머1()
        if npc_detected(boxId=102, spawnIds=[901]):
            return 차타이머2()
        if npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3()
        if npc_detected(boxId=102, spawnIds=[904]):
            return 차타이머4()
        if npc_detected(boxId=102, spawnIds=[905]):
            return 차타이머5()
        if npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6()
        if npc_detected(boxId=102, spawnIds=[908]):
            return 차타이머7()
        if npc_detected(boxId=102, spawnIds=[909]):
            return 차타이머8()
        if npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9()
        if npc_detected(boxId=102, spawnIds=[912]):
            return 차타이머10()
        if npc_detected(boxId=102, spawnIds=[913]):
            return 차타이머11()
        if npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=12)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return 대기시간()
        if time_expired(timerId='12'):
            return 생성랜덤()


class 차타이머2(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
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


class 차타이머5(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[905]):
            return 대기시간()
        if time_expired(timerId='7'):
            return 생성랜덤()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='6'):
            return 생성랜덤()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='3'):
            return 생성랜덤()


class 차타이머8(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[909]):
            return 대기시간()
        if time_expired(timerId='3'):
            return 생성랜덤()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='3'):
            return 생성랜덤()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='3'):
            return 생성랜덤()


class 차타이머11(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[913]):
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
        create_monster(spawnIds=[1101], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1102], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1103], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1104], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1105], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1106], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1107], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1108], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1101])
        destroy_monster(spawnIds=[1102])
        destroy_monster(spawnIds=[1103])
        destroy_monster(spawnIds=[1104])
        destroy_monster(spawnIds=[1105])
        destroy_monster(spawnIds=[1106])
        destroy_monster(spawnIds=[1107])
        destroy_monster(spawnIds=[1108])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


