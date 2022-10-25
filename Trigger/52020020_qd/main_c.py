""" trigger/52020020_qd/main_c.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200145], questStates=[1]):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='전 밖에서 기다리고 있겠습니다.', duration=2500, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return move(self.ctx)


class move(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return out(self.ctx)


class out(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])


initial_state = idle
