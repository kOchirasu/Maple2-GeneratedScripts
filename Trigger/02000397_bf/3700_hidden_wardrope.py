""" trigger/02000397_bf/3700_hidden_wardrope.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=False) # PortalOn
        set_ladder(triggerIds=[540], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[541], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[542], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[543], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[544], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[545], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_mesh(triggerIds=[3700], visible=True, arg3=0, arg4=0, arg5=0) # Wall_BehindWardrope
        set_mesh(triggerIds=[3701,3704], visible=True, arg3=0, arg4=0, arg5=0) # BehindWardropeCover01
        set_mesh(triggerIds=[3702], visible=True, arg3=0, arg4=0, arg5=0) # Wardrope
        set_mesh(triggerIds=[3703], visible=True, arg3=0, arg4=0, arg5=0) # WardropeInvisible
        set_interact_object(triggerIds=[10001146], state=0) # Wardrope
        set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='HiddenRouteOpen', value=1):
            return Opened()
        if user_value(key='HiddenRouteOpen', value=2):
            return Closed()


class Opened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3702], visible=False, arg3=100, arg4=0, arg5=2) # Wardrope
        set_interact_object(triggerIds=[10001146], state=1) # Wardrope

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001146], arg2=0):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # PortalOn
        set_mesh(triggerIds=[3700], visible=False, arg3=0, arg4=0, arg5=3) # Wall_BehindWardrope
        set_mesh(triggerIds=[3701,3704], visible=False, arg3=0, arg4=0, arg5=3) # BehindWardropeCover
        set_mesh(triggerIds=[3703], visible=False, arg3=0, arg4=0, arg5=0) # WardropeInvisible
        set_ladder(triggerIds=[540], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[541], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[542], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[543], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[544], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[545], visible=True, animationEffect=True, animationDelay=2) # Ladder


class Closed(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3702], visible=False, arg3=100, arg4=0, arg5=2) # Wardrope
        set_interact_object(triggerIds=[10001146], state=1) # Wardrope

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001146], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3702], visible=True, arg3=0, arg4=0, arg5=0) # Wardrope


