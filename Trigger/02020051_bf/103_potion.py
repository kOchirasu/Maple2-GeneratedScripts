""" trigger/02020051_bf/103_potion.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Main', value=1):
            return 포션사용_준비()


class 포션사용_준비(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002131], state=2)
        set_user_value(triggerId=101, key='Potion', value=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=720000):
            return 포션사용()


class 포션사용(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002131], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002131], arg2=0):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=101, key='Potion', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Main', value=2):
            return 준비()


