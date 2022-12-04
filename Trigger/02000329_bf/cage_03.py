""" trigger/02000329_bf/cage_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6803], visible=False)
        self.set_actor(triggerId=203, visible=True, initialSequence='Closed')
        self.create_monster(spawnIds=[1003,1103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1103]):
            return 닭생성(self.ctx)


class 닭생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=203, visible=True, initialSequence='Opened')
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[6803], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 닭이동(self.ctx)


class 닭이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 닭소멸(self.ctx)


class 닭소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003])


initial_state = 대기
