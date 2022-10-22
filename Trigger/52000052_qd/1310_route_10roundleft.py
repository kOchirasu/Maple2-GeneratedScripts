""" trigger/52000052_qd/1310_route_10roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=17, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4017], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[18101], visible=True)
        set_agent(triggerIds=[18102], visible=True)
        set_effect(triggerIds=[5010], visible=False) # 10Round_BridgeApp
        set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5010], visible=True) # 10Round_BridgeApp
        set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[331000,331001,331002,331003,331004,331005,331006,331007,331008,331009,331010,331011], visible=True, meshCount=12, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18101], visible=False)
        set_agent(triggerIds=[18102], visible=False)
        set_portal(portalId=17, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4017], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[131000,131001,131002,131003,131004,131005,131006,131007,131008,131009,131010,131011], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


