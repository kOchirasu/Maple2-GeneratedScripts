""" trigger/02000451_bf/4000_ladder.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[4001], visible=False, enable=False, fade=0) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4002], visible=False, enable=False, fade=0) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4003], visible=False, enable=False, fade=0) # Ladder_Shortcut
        self.set_interact_object(trigger_ids=[10001128], state=0, arg4=False) # LeverForLadder

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9100, spawn_ids=[101]):
            # 설눈이 감지
            return PCComeDown(self.ctx)


class PCComeDown(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[4001], visible=True, enable=True, fade=2) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4002], visible=True, enable=True, fade=2) # Ladder_Shortcut
        self.set_ladder(trigger_ids=[4003], visible=True, enable=True, fade=2) # Ladder_Shortcut


initial_state = Wait
