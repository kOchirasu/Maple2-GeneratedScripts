""" trigger/52010002_qd/monster_02.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=701, spawnIds=[102]):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[102]):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.set_conversation(type=1, spawnId=112, script='$52010002_QD__MONSTER_02__0$', arg4=2, arg5=1)


class End(common.Trigger):
    pass


initial_state = idle
