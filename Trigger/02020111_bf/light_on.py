""" trigger/02020111_bf/light_on.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 대기()
        if all_of():
            return 시작()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라이트_변경()


class 라이트_변경(state.State):
    def on_enter(self):
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> state.State:
        if all_of():
            return 시작()


