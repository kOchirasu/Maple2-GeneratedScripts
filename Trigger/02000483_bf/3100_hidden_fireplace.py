""" trigger/02000483_bf/3100_hidden_fireplace.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # PortalOn
        set_actor(triggerId=4000, visible=True, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_ladder(triggerIds=[515], visible=False, animationEffect=False, animationDelay=0) # Ladder
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Wall_BehindFirePlace
        set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0) # BehindFirePlaceCover
        set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0) # FireplaceInvisible
        set_interact_object(triggerIds=[10002038], state=0) # Fireplace
        set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='HiddenRouteOpen', value=1):
            return Opened()
        if user_value(key='HiddenRouteOpen', value=2):
            return Closed()


class Opened(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        set_interact_object(triggerIds=[10002038], state=1) # Fireplace

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002038], arg2=0):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # PortalOn
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0) # FireplaceInvisible
        set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_ladder(triggerIds=[515], visible=True, animationEffect=True, animationDelay=2) # Ladder
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=3) # Wall_BehindFirePlace
        set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=3) # BehindFirePlaceCover


class Closed(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        set_interact_object(triggerIds=[10002038], state=1) # Fireplace

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002038], arg2=0):
            return NothingHappened()


class NothingHappened(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='he_in_prop_fireplace_A01_Opened') # FireplaceActor


