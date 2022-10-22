""" trigger/52000052_qd/2309_route_09roundright.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=16, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4016], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[28091], visible=True)
        set_agent(triggerIds=[28092], visible=True)
        set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5009], visible=True) # 09Round_BridgeApp
        set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[430900,430901,430902,430903,430904,430905,430906,430907,430908,430909], visible=True, meshCount=10, arg4=0, delay=50) # Real
        set_agent(triggerIds=[28091], visible=False)
        set_agent(triggerIds=[28092], visible=False)
        set_portal(portalId=16, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4016], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[230900,230901,230902,230903,230904,230905,230906,230907,230908,230909], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


