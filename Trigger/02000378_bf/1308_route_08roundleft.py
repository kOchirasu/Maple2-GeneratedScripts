""" trigger/02000378_bf/1308_route_08roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[18081], visible=True)
        set_agent(triggerIds=[18082], visible=True)
        set_agent(triggerIds=[18083], visible=True)
        set_agent(triggerIds=[18084], visible=True)
        set_effect(triggerIds=[5008], visible=False) # 08Round_BridgeApp
        set_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330800,330801,330802,330803,330804,330805,330806,330807,330808,330809,330810,330811,330812,330813,330814,330815,330816,330817,330818,330819], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5008], visible=True) # 08Round_BridgeApp
        set_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330800,330801,330802,330803,330804,330805,330806,330807,330808,330809,330810,330811,330812,330813,330814,330815,330816,330817,330818,330819], visible=True, meshCount=20, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18081], visible=False)
        set_agent(triggerIds=[18082], visible=False)
        set_agent(triggerIds=[18083], visible=False)
        set_agent(triggerIds=[18084], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130800,130801,130802,130803,130804,130805,130806,130807,130808,130809,130810,130811,130812,130813,130814,130815,130816,130817,130818,130819], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


