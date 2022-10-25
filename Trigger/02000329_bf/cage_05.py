""" trigger/02000329_bf/cage_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6805], visible=False)
        self.set_actor(triggerId=205, visible=True, initialSequence='Closed')
        self.create_monster(spawnIds=[1005,1105], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105]):
            return 닭생성(self.ctx)


class 닭생성(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=205, visible=True, initialSequence='Opened')
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[6805], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 닭이동(self.ctx)


class 닭이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 닭소멸(self.ctx)


class 닭소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1005])


initial_state = 대기
