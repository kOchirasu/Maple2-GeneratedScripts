""" trigger/02000397_bf/3200_hidden_bookcase.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False) # PortalOn
        set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[523], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[524], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_mesh(triggerIds=[3200], visible=True, arg3=0, arg4=0, arg5=0) # Wall_BehindBookcase
        set_mesh(triggerIds=[3201], visible=True, arg3=0, arg4=0, arg5=0) # BehindBookcaseCover
        set_mesh(triggerIds=[3202], visible=True, arg3=0, arg4=0, arg5=0) # Bookcase
        set_mesh(triggerIds=[3203], visible=True, arg3=0, arg4=0, arg5=0) # BookcaseInvisible
        set_interact_object(triggerIds=[10001141], state=0) # Bookcase
        set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='HiddenRouteOpen', value=1):
            return Opened()
        if user_value(key='HiddenRouteOpen', value=2):
            return Closed()


class Opened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3202], visible=False, arg3=0, arg4=0, arg5=0) # Bookcase
        set_interact_object(triggerIds=[10001141], state=1) # Bookcase

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001141], arg2=0):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # PortalOn
        set_mesh(triggerIds=[3203], visible=False, arg3=0, arg4=0, arg5=0) # BookcaseInvisible
        set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[523], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[524], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_mesh(triggerIds=[3200], visible=False, arg3=0, arg4=0, arg5=3) # Wall_BehindBookcase
        set_mesh(triggerIds=[3201], visible=False, arg3=0, arg4=0, arg5=3) # BehindBookcaseCover


class Closed(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3202], visible=False, arg3=0, arg4=0, arg5=0) # Bookcase
        set_interact_object(triggerIds=[10001141], state=1) # Bookcase

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001141], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3202], visible=True, arg3=0, arg4=0, arg5=0) # Bookcase


