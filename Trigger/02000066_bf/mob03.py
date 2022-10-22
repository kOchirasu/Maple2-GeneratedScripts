""" trigger/02000066_bf/mob03.xml """
from common import *
import state


# 디펜스 모드 :  엘리트
class 대기시간(state.State):
    def on_tick(self) -> state.State:
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


class 차타이머2(state.State):
    def on_enter(self):
        set_timer(timerId='80', seconds=80)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            return 대기시간()
        if time_expired(timerId='80'):
            return 생성랜덤()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='75', seconds=75)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='75'):
            return 생성랜덤()


class 차타이머4(state.State):
    def on_enter(self):
        set_timer(timerId='68', seconds=68)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[904]):
            return 대기시간()
        if time_expired(timerId='68'):
            return 생성랜덤()


class 차타이머5(state.State):
    def on_enter(self):
        set_timer(timerId='63', seconds=63)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[905]):
            return 대기시간()
        if time_expired(timerId='63'):
            return 생성랜덤()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='58', seconds=58)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='58'):
            return 생성랜덤()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='68', seconds=68)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='68'):
            return 생성랜덤()


class 차타이머8(state.State):
    def on_enter(self):
        set_timer(timerId='62', seconds=62)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[909]):
            return 대기시간()
        if time_expired(timerId='62'):
            return 생성랜덤()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='60'):
            return 생성랜덤()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='55', seconds=55)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='55'):
            return 생성랜덤()


class 차타이머11(state.State):
    def on_enter(self):
        set_timer(timerId='52', seconds=52)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[913]):
            return 대기시간()
        if time_expired(timerId='52'):
            return 생성랜덤()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='49', seconds=49)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='49'):
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
        create_monster(spawnIds=[1201], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1202], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1203], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1204], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1205], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1206], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1207], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1208], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1201])
        destroy_monster(spawnIds=[1202])
        destroy_monster(spawnIds=[1203])
        destroy_monster(spawnIds=[1204])
        destroy_monster(spawnIds=[1205])
        destroy_monster(spawnIds=[1206])
        destroy_monster(spawnIds=[1207])
        destroy_monster(spawnIds=[1208])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


