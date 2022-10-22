""" trigger/99999946/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[500,501,502,503,504,505,506,507,508,509], randomCount=10, isVisible=False)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006], arg2=False)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 시작대기()


class 시작대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    pass


