""" trigger/02000066_bf/mobgroup01.xml """
from common import *
import state


# 디펜스 모드 :  좀비모둠
class 시작(state.State):
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
        if user_detected(boxIds=[103]):
            return 대기시간()


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
        set_timer(timerId='51', seconds=51)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return 대기시간()
        if time_expired(timerId='51'):
            return 대기시간()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='42', seconds=42)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='42'):
            return 대기시간()


class 차타이머4(state.State):
    def on_enter(self):
        set_timer(timerId='37', seconds=37)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[904]):
            return 대기시간()
        if time_expired(timerId='37'):
            return 대기시간()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='33', seconds=33)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='33'):
            return 대기시간()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='30'):
            return 대기시간()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='27', seconds=27)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='27'):
            return 대기시간()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=25)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='25'):
            return 대기시간()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=20)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='20'):
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


