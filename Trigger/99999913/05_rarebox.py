""" trigger/99999913/05_rarebox.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_user_value(key='RareBoxOnCount', value=0)
        set_user_value(key='RareBoxOff', value=0)
        set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxOnCount', value=1):
            return Delay()


class Delay(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=180000):
            return BoxOn()


class BoxOn(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='머쉬룸 타워 근처에 황금 상자가 나타났습니다!\n황금 상자를 차지해보세요!', arg3='5000', arg4='0')
        set_interact_object(triggerIds=[11000038], state=1) # Rare Box

    def on_tick(self) -> state.State:
        if user_value(key='RareBoxOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()


