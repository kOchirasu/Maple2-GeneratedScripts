""" trigger/52010023_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[7001], visible=False)
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002500], questStates=[2]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$52010023_QD__MAIN__0$', arg4=5)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[101]):
            return Npc_out(self.ctx)


class Npc_out(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7001], visible=True)
        self.destroy_monster(spawnIds=[101])


initial_state = idle
