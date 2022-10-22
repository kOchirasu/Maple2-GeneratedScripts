""" trigger/02000376_bf/11_innerlightguide.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='DungeonStart', value=0)
        set_effect(triggerIds=[5100], visible=False) # 화살표
        set_effect(triggerIds=[5101], visible=False) # 화살표
        set_effect(triggerIds=[5102], visible=False) # 화살표
        set_effect(triggerIds=[5103], visible=False) # 화살표
        set_effect(triggerIds=[5104], visible=False) # 화살표

    def on_tick(self) -> state.State:
        if user_value(key='DungeonStart', value=1):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideOn()


class GuideOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000376_BF__11_INNERLIGHTGUIDE__0$', arg3='4000', arg4='0')
        set_effect(triggerIds=[5100], visible=True) # 화살표
        set_effect(triggerIds=[5101], visible=True) # 화살표
        set_effect(triggerIds=[5102], visible=True) # 화살표
        set_effect(triggerIds=[5103], visible=True) # 화살표
        set_effect(triggerIds=[5104], visible=True) # 화살표

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100], visible=False) # 화살표
        set_effect(triggerIds=[5101], visible=False) # 화살표
        set_effect(triggerIds=[5102], visible=False) # 화살표
        set_effect(triggerIds=[5103], visible=False) # 화살표
        set_effect(triggerIds=[5104], visible=False) # 화살표


