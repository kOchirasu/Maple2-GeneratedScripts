""" trigger/52000084_qd/4100_ladder.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[4100], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4101], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4102], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4103], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        self.set_interact_object(triggerIds=[10001128], state=0, arg4=False) # LeverForLadder

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9200, spawnIds=[101]):
            return PCComeDown(self.ctx)


class PCComeDown(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9400]):
            return LadderOn(self.ctx)


class LadderOn(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[4100], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4101], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4102], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        self.set_ladder(triggerIds=[4103], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut


initial_state = Wait
