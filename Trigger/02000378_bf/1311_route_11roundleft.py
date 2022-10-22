""" trigger/02000378_bf/1311_route_11roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=19, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4019], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[18111], visible=True)
        set_agent(triggerIds=[18112], visible=True)
        set_effect(triggerIds=[5011], visible=False) # 11Round_BridgeApp
        set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=True, meshCount=3, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, meshCount=10, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=True) # 11Round_BridgeApp
        set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[331100,331101,331102,331103,331104,331105,331106,331107,331108,331109], visible=True, meshCount=10, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18111], visible=False)
        set_agent(triggerIds=[18112], visible=False)
        set_portal(portalId=19, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4019], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[131100,131101,131102,131103,131104,131105,131106,131107,131108,131109], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


