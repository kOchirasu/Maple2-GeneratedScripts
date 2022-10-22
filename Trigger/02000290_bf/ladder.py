""" trigger/02000290_bf/ladder.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=True, arg3=0, arg4=0, arg5=0) # WaterDisApp
        set_ladder(triggerIds=[511], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[512], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[513], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[514], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[515], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[516], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[517], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[518], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[519], visible=False, animationEffect=False) # LadderTheFall
        set_ladder(triggerIds=[520], visible=False, animationEffect=False) # LadderTheFall
        set_effect(triggerIds=[5100], visible=False) # LadderAppear
        set_effect(triggerIds=[5102], visible=False) # WaterDisApp
        set_effect(triggerIds=[5200], visible=False) # LeverArrow
        set_interact_object(triggerIds=[10000429], state=0) # Lever

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 폭포안내()


class 폭포안내(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000429], state=1) # Lever
        set_effect(triggerIds=[5200], visible=True) # LeverArrow
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        show_guide_summary(entityId=20002902, textId=20002902) # 레버를 당겨 보세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000429], arg2=0):
            return 폭포갈라짐()


class 폭포갈라짐(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002902)
        set_effect(triggerIds=[5102], visible=True) # WaterDisApp
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=False, arg3=0, arg4=200, arg5=2)
        set_effect(triggerIds=[5200], visible=False) # LeverArrow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 사다리생김()


class 사다리생김(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002907, textId=20002907, duration=5000) # 폭포 위로 올라갈 수 있는 사다리가 나타났어요.
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_effect(triggerIds=[5100], visible=True) # LadderAppear
        set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        set_ladder(triggerIds=[515], visible=True, animationEffect=True)
        set_ladder(triggerIds=[516], visible=True, animationEffect=True)
        set_ladder(triggerIds=[517], visible=True, animationEffect=True)
        set_ladder(triggerIds=[518], visible=True, animationEffect=True)
        set_ladder(triggerIds=[519], visible=True, animationEffect=True)
        set_ladder(triggerIds=[520], visible=True, animationEffect=True)


