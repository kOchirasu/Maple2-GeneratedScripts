""" trigger/99999908/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_ambient_light(primary=[1,1,1])
        set_directional_light(diffuseColor=[1,1,1], specularColor=[0,0,0])
        set_timer(timerId='240', seconds=240, clearAtZero=True, display=True)


class switch(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 시작()


