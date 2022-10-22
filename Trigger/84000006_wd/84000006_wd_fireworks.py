""" trigger/84000006_wd/84000006_wd_fireworks.xml """
from common import *
import state


# 불꽃놀이 발사 준비
class Staging(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Fireworks', value=1):
            return Volley()


# UV받아 불꽃놀이 연출
class Volley(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return None


