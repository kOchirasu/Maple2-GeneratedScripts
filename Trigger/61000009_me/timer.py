""" trigger/61000009_me/timer.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        show_guide_summary(entityId=100, textId=40012) # 잠시 후에 시작합니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ready()
        if user_value(key='timer', value=1):
            return Ready_Idle()


class Ready_Idle(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=100)
        set_timer(timerId='1200', seconds=1200, clearAtZero=False, display=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1200'):
            return endGame()


class endGame(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$61000004_ME__TRIGGER_01__2$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=0, portalId=0)
            return end()


class end(state.State):
    pass


