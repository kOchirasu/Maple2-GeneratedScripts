""" trigger/02000066_bf/mobgroup03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1501])
        destroy_monster(spawnIds=[1502])
        destroy_monster(spawnIds=[1503])
        destroy_monster(spawnIds=[1504])
        destroy_monster(spawnIds=[1505])
        destroy_monster(spawnIds=[1506])
        destroy_monster(spawnIds=[1507])
        destroy_monster(spawnIds=[1508])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 대기시간()


# 디펜스 모드 :  해골 자코 모둠
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
        set_timer(timerId='14', seconds=14)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return 대기시간()
        if time_expired(timerId='14'):
            return 대기시간()


class 차타이머2(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            return 대기시간()
        if time_expired(timerId='6'):
            return 대기시간()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=11)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='11'):
            return 대기시간()


class 차타이머4(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=11)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[904]):
            return 대기시간()
        if time_expired(timerId='11'):
            return 대기시간()


class 차타이머5(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[905]):
            return 대기시간()
        if time_expired(timerId='5'):
            return 대기시간()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='10'):
            return 대기시간()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=11)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='11'):
            return 대기시간()


class 차타이머8(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[909]):
            return 대기시간()
        if time_expired(timerId='5'):
            return 대기시간()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='10'):
            return 대기시간()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=14)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='14'):
            return 대기시간()


class 차타이머11(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=7)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[913]):
            return 대기시간()
        if time_expired(timerId='7'):
            return 대기시간()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=13)
        create_monster(spawnIds=[1501], arg2=False)
        create_monster(spawnIds=[1502], arg2=False)
        create_monster(spawnIds=[1503], arg2=False)
        create_monster(spawnIds=[1504], arg2=False)
        create_monster(spawnIds=[1505], arg2=False)
        create_monster(spawnIds=[1506], arg2=False)
        create_monster(spawnIds=[1507], arg2=False)
        create_monster(spawnIds=[1508], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='13'):
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1501])
        destroy_monster(spawnIds=[1502])
        destroy_monster(spawnIds=[1503])
        destroy_monster(spawnIds=[1504])
        destroy_monster(spawnIds=[1505])
        destroy_monster(spawnIds=[1506])
        destroy_monster(spawnIds=[1507])
        destroy_monster(spawnIds=[1508])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


