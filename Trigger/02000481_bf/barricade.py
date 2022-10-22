""" trigger/02000481_bf/barricade.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_user():
            return CheckUser04_GuildRaid()


class CheckUser04_GuildRaid(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=False, arg5=0) # 최대 30초 대기

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4, operator='GreaterEqual'):
            return MaxCount04_Start()
        if count_users(boxId=701, boxId=4, operator='Less'):
            return MaxCount04_Wait()


class MaxCount04_Wait(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=4, operator='GreaterEqual'):
            return MaxCount04_Start()
        if time_expired(timerId='1'):
            return MaxCount04_Start()
        if wait_tick(waitTick=6000):
            return MaxCount04_Wait()


class MaxCount04_Start(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if true():
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 대기()

state.DungeonStart = DungeonStart


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='start', value=1)
        set_effect(triggerIds=[70001], visible=False)
        set_effect(triggerIds=[70002], visible=False)
        set_effect(triggerIds=[70003], visible=False)
        set_effect(triggerIds=[70004], visible=False)
        set_effect(triggerIds=[70005], visible=False)
        set_mesh(triggerIds=[80000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 유저감지()


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000481_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[70001], visible=True)
        set_effect(triggerIds=[70002], visible=True)
        set_effect(triggerIds=[70003], visible=True)
        set_effect(triggerIds=[70004], visible=True)
        set_effect(triggerIds=[70005], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


