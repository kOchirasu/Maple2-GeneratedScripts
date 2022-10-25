""" trigger/02000329_bf/cage_04.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6804], visible=False)
        self.set_actor(triggerId=204, visible=True, initialSequence='Closed')
        self.create_monster(spawnIds=[1004,1104], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1104]):
            return 닭생성(self.ctx)


class 닭생성(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=204, visible=True, initialSequence='Opened')
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[6804], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 닭이동(self.ctx)


class 닭이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 닭소멸(self.ctx)


class 닭소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1004])


initial_state = 대기
