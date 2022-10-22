""" trigger/66200001_gd/07_gameguide.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GameGuide', value=1):
            return GameGuide_20()


class GameGuide_20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=19, clearAtZero=True, display=False) # 20sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


#  Normal GameGuide
class NormalGameGuide_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620104, textId=26620104, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_02()


class NormalGameGuide_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620105, textId=26620105, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_03()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620104, textId=26620104, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_04()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26620105, textId=26620105, duration=4000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Reset()


#  Reset 
class Reset(state.State):
    def on_enter(self):
        set_user_value(key='GameGuide', value=0)
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


