""" trigger/52100053_qd/3600_hidden_woodbox.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=False) # PortalOn
        set_ladder(triggerIds=[530], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[531], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[532], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[533], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[534], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[535], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_mesh(triggerIds=[3600], visible=True, arg3=0, arg4=0, arg5=0) # Wall_BehindWoodBox
        set_mesh(triggerIds=[3601], visible=True, arg3=0, arg4=0, arg5=0) # BehindWoodBoxCover
        set_mesh(triggerIds=[3602], visible=True, arg3=0, arg4=0, arg5=0) # WoodBox
        set_mesh(triggerIds=[3603], visible=True, arg3=0, arg4=0, arg5=0) # WoodBoxInvisible
        set_interact_object(triggerIds=[10002096], state=0) # WoodBox
        set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='HiddenRouteOpen', value=1):
            return Opened()
        if user_value(key='HiddenRouteOpen', value=2):
            return Closed()


class Opened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3602], visible=False, arg3=100, arg4=0, arg5=2) # WoodBox
        set_interact_object(triggerIds=[10002096], state=1) # WoodBox

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002096], arg2=0):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True) # PortalOn
        set_mesh(triggerIds=[3600], visible=False, arg3=0, arg4=0, arg5=3) # Wall_BehindWoodBox
        set_mesh(triggerIds=[3601], visible=False, arg3=0, arg4=0, arg5=3) # BehindWoodBoxCover
        set_mesh(triggerIds=[3603], visible=False, arg3=0, arg4=0, arg5=0) # WoodBoxInvisible
        set_ladder(triggerIds=[530], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[531], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[532], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[533], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[534], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[535], visible=True, animationEffect=True, animationDelay=2) # Ladder


class Closed(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3602], visible=False, arg3=100, arg4=0, arg5=2) # WoodBox
        set_interact_object(triggerIds=[10002096], state=1) # WoodBox

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002096], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3602], visible=True, arg3=0, arg4=0, arg5=0) # WoodBox


