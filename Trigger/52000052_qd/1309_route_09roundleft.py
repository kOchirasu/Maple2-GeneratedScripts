""" trigger/52000052_qd/1309_route_09roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=15, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4015], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[18091], visible=True)
        set_agent(triggerIds=[18092], visible=True)
        set_effect(triggerIds=[5009], visible=False) # 09Round_BridgeApp
        set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return StartDazzling01()


class StartDazzling01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5009], visible=True) # 09Round_BridgeApp
        set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330900,330901,330902,330903,330904,330905,330906,330907,330908,330909,330910,330911], visible=True, meshCount=12, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18091], visible=False)
        set_agent(triggerIds=[18092], visible=False)
        set_portal(portalId=15, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4015], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130900,130901,130902,130903,130904,130905,130906,130907,130908,130909,130910,130911], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


