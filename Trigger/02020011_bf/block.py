""" trigger/02020011_bf/block.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=True, arg5=5)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 딜레이()


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 사라짐()


class 사라짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=False, arg5=5)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 딜레이2()


class 딜레이2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 대기()


