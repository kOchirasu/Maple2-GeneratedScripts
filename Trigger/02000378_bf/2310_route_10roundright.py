""" trigger/02000378_bf/2310_route_10roundright.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=18, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4018], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[28101], visible=True)
        set_agent(triggerIds=[28102], visible=True)
        set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=True, meshCount=4, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, meshCount=12, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5010], visible=True) # 10Round_BridgeApp
        set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[431000,431001,431002,431003,431004,431005,431006,431007,431008,431009,431010,431011], visible=True, meshCount=12, arg4=0, delay=50) # Real
        set_agent(triggerIds=[28101], visible=False)
        set_agent(triggerIds=[28102], visible=False)
        set_portal(portalId=18, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4018], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[231000,231001,231002,231003,231004,231005,231006,231007,231008,231009,231010,231011], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


