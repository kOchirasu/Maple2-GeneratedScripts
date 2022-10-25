""" trigger/52000093_qd/52000093_trigger.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=False)
        self.destroy_monster(spawnIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008])

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[50100490], questStates=[1]):
            return 진행중일때20002274(self.ctx)
        if self.quest_user_detected(boxIds=[9100], questIds=[20002274], questStates=[1]):
            return 진행중일때20002274(self.ctx)


class 진행중일때20002274(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008], animationEffect=False) # ,90537,90539

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008]):
            return 진행중일때20002274(self.ctx)


initial_state = 대기
