""" trigger/52010002_qd/monster_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=701, spawnIds=[103]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.set_conversation(type=1, spawnId=113, script='$52010002_QD__MONSTER_03__0$', arg4=2, arg5=1)


class End(trigger_api.Trigger):
    pass


initial_state = idle
