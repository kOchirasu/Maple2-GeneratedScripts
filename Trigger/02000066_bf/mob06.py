""" trigger/02000066_bf/mob06.xml """
from common import *
import state


# 파토스
class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[902]): # 33레벨
            return 차타이머3()
        if npc_detected(boxId=102, spawnIds=[906]): # 35레벨
            return 차타이머6()
        if npc_detected(boxId=102, spawnIds=[910]): # 35레벨 하드
            return 차타이머9()
        if npc_detected(boxId=102, spawnIds=[914]):
            return 차타이머12()


class 차타이머3(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()
        if time_expired(timerId='5'):
            return 차생성3()


class 차타이머6(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()
        if time_expired(timerId='5'):
            return 차생성6()


class 차타이머9(state.State):
    def on_enter(self):
        set_timer(timerId='40', seconds=40)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()
        if time_expired(timerId='40'):
            return 차생성9()


class 차타이머12(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=20)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()
        if time_expired(timerId='20'):
            return 차생성12()


class 차생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[902]):
            return 소멸()


class 차생성6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[906]):
            return 소멸()


class 차생성9(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910]):
            return 소멸()


class 차생성12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[914]):
            return 소멸()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1299])

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


