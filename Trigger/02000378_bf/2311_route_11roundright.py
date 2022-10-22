""" trigger/02000378_bf/2311_route_11roundright.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4010], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[28111], visible=True)
        set_agent(triggerIds=[28112], visible=True)
        set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=True) # 11Round_BridgeApp
        set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[431100,431101,431102,431103,431104,431105,431106,431107,431108,431109,431110,431111], visible=True, meshCount=12, arg4=0, delay=50) # Real
        set_agent(triggerIds=[28111], visible=False)
        set_agent(triggerIds=[28112], visible=False)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4010], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[231100,231101,231102,231103,231104,231105,231106,231107,231108,231109,231110,231111], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


