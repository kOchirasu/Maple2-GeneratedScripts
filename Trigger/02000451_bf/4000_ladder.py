""" trigger/02000451_bf/4000_ladder.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[4001], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4002], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4003], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_interact_object(triggerIds=[10001128], state=0, arg4=False) # LeverForLadder

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9100, spawnIds=[101]):
            return PCComeDown(self.ctx)


class PCComeDown(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9300]):
            return LadderOn(self.ctx)


class LadderOn(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[4001], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4002], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4003], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut


initial_state = Wait
