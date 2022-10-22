""" trigger/02000066_bf/mob04.xml """
from common import *
import state


# 디펜스 모드 :  원거리
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
        set_timer(timerId='25', seconds=25)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return 대기시간()
        if time_expired(timerId='25'):
            return 생성랜덤()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=23)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='23'):
            return 생성랜덤()


class 차타이머4(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=21)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[904]):
            return 대기시간()
        if time_expired(timerId='21'):
            return 생성랜덤()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=19)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='19'):
            return 생성랜덤()


class 차타이머7(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=20)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[908]):
            return 대기시간()
        if time_expired(timerId='20'):
            return 생성랜덤()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='18', seconds=18)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='18'):
            return 생성랜덤()


class 차타이머10(state.State):
    def on_enter(self):
        set_timer(timerId='16', seconds=16)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return 대기시간()
        if time_expired(timerId='16'):
            return 생성랜덤()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=14)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='14'):
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
        create_monster(spawnIds=[1301], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1302], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1303], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1304], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1305], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1306], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1307], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 번생성8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1308], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1301])
        destroy_monster(spawnIds=[1302])
        destroy_monster(spawnIds=[1303])
        destroy_monster(spawnIds=[1304])
        destroy_monster(spawnIds=[1305])
        destroy_monster(spawnIds=[1306])
        destroy_monster(spawnIds=[1307])
        destroy_monster(spawnIds=[1308])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


