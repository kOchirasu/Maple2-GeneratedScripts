""" trigger/02000378_bf/1304_route_04roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[18041], visible=True)
        set_agent(triggerIds=[18042], visible=True)
        set_agent(triggerIds=[18043], visible=True)
        set_agent(triggerIds=[18044], visible=True)
        set_effect(triggerIds=[5004], visible=False) # 04Round_BridgeApp
        set_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330400,330401,330402,330403,330404,330405,330406,330407,330408,330409,330410,330411,330412,330413,330414,330415,330416,330417,330418,330419], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # 04Round_BridgeApp
        set_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330400,330401,330402,330403,330404,330405,330406,330407,330408,330409,330410,330411,330412,330413,330414,330415,330416,330417,330418,330419], visible=True, meshCount=20, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18041], visible=False)
        set_agent(triggerIds=[18042], visible=False)
        set_agent(triggerIds=[18043], visible=False)
        set_agent(triggerIds=[18044], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130400,130401,130402,130403,130404,130405,130406,130407,130408,130409,130410,130411,130412,130413,130414,130415,130416,130417,130418,130419], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


