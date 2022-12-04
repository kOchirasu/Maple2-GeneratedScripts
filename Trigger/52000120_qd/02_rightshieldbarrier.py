""" trigger/52000120_qd/02_rightshieldbarrier.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3200], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.destroy_monster(spawnIds=[980,981,982,983,984,985])
        self.set_skill(triggerIds=[7000], enable=False) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return ActivateShiled01(self.ctx)


class ActivateShiled01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[980,981,982,983,984,985], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            return Push01(self.ctx)


class Push01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=980, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=981, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=982, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=983, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=984, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=985, sequenceName='Attack_01_A')
        self.set_skill(triggerIds=[7000], enable=True) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1333):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            return Push01(self.ctx)


initial_state = Wait
