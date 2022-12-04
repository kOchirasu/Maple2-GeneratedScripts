""" trigger/02000293_bf/door03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1007, visible=False, initialSequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999997]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1007, visible=False, initialSequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000529,10000520], stateValue=0):
            return 트리거02시작(self.ctx)


class 트리거02시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1007, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[2034], animationEffect=True)
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 트리거03시작(self.ctx)


class 트리거03시작(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[25000])
        self.destroy_monster(spawnIds=[25001])
        self.destroy_monster(spawnIds=[25002])
        self.destroy_monster(spawnIds=[25003])
        self.destroy_monster(spawnIds=[25004])
        self.destroy_monster(spawnIds=[25005])
        self.destroy_monster(spawnIds=[25006])
        self.destroy_monster(spawnIds=[25007])
        self.destroy_monster(spawnIds=[25008])
        self.set_actor(triggerId=1007, visible=False, initialSequence='Closed')


initial_state = 대기
