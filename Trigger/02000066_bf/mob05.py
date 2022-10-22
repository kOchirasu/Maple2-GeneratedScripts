""" trigger/02000066_bf/mob05.xml """
from common import *
import state


# 디펜스 모드 :  해골B
class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[901]): # 33레벨
            return 차타이머2()
        if npc_detected(boxId=102, spawnIds=[905]): # 35레벨
            return 차타이머5()
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
        set_timer(timerId='13', seconds=13)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            return 대기시간()
        if time_expired(timerId='13'):
            return 생성랜덤()


class 차타이머5(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=11)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[905]):
            return 소멸()
        if time_expired(timerId='11'):
            return 생성랜덤()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='10'):
            return 생성랜덤()


class 차타이머8(state.State):
    def on_enter(self):
        set_timer(timerId='9', seconds=9)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[909]):
            return 대기시간()
        if time_expired(timerId='9'):
            return 생성랜덤()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=8)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='8'):
            return 생성랜덤()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='7'):
            return 생성랜덤()


class 차타이머11(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[913]):
            return 대기시간()
        if time_expired(timerId='6'):
            return 생성랜덤()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='5'):
            return 생성랜덤()


class 생성랜덤(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1401], arg2=False)
        create_monster(spawnIds=[1402], arg2=False)
        create_monster(spawnIds=[1403], arg2=False)
        create_monster(spawnIds=[1404], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1401])
        destroy_monster(spawnIds=[1402])
        destroy_monster(spawnIds=[1403])
        destroy_monster(spawnIds=[1404])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


