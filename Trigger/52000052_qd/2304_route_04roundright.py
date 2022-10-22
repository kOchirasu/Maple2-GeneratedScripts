""" trigger/52000052_qd/2304_route_04roundright.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[28041], visible=True)
        set_agent(triggerIds=[28042], visible=True)
        set_agent(triggerIds=[28043], visible=True)
        set_agent(triggerIds=[28044], visible=True)
        set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # 04Round_BridgeApp
        set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[430400,430401,430402,430403,430404,430405,430406,430407,430408,430409,430410,430411,430412,430413,430414,430415,430416,430417,430418,430419], visible=True, meshCount=20, arg4=0, delay=50) # Real
        set_agent(triggerIds=[28041], visible=False)
        set_agent(triggerIds=[28042], visible=False)
        set_agent(triggerIds=[28043], visible=False)
        set_agent(triggerIds=[28044], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[230400,230401,230402,230403,230404,230405,230406,230407,230408,230409,230410,230411,230412,230413,230414,230415,230416,230417,230418,230419], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


