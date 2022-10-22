""" trigger/52000052_qd/2302_route_02roundback.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[28021], visible=True)
        set_agent(triggerIds=[28022], visible=True)
        set_agent(triggerIds=[28023], visible=True)
        set_agent(triggerIds=[28024], visible=True)
        set_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[430200,430201,430202,430203,430204,430205,430206,430207,430208,430209,430210,430211,430212,430213,430214,430215,430216,430217,430218,430219], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 02Round_BridgeApp
        set_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[430200,430201,430202,430203,430204,430205,430206,430207,430208,430209,430210,430211,430212,430213,430214,430215,430216,430217,430218,430219], visible=True, meshCount=20, arg4=100, delay=50) # Real
        set_agent(triggerIds=[28021], visible=False)
        set_agent(triggerIds=[28022], visible=False)
        set_agent(triggerIds=[28023], visible=False)
        set_agent(triggerIds=[28024], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[230200,230201,230202,230203,230204,230205,230206,230207,230208,230209,230210,230211,230212,230213,230214,230215,230216,230217,230218,230219], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


