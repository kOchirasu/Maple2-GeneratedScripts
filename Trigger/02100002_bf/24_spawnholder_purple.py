""" trigger/02100002_bf/24_spawnholder_purple.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='ActivateHolder', value=0) # 메인 트리거에서 받는 신호
        self.set_user_value(key='DungeonQuit', value=0) # ON
        self.set_interact_object(triggerIds=[10001254], state=2) # OFF
        self.set_interact_object(triggerIds=[10001255], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ActivateHolder', value=1):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStart(self.ctx)


class SpawnStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001255], state=1) # ON
        self.set_interact_object(triggerIds=[10001254], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001255], stateValue=0):
            return StopDelay(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class StopDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=104, key='SpawnHold', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStop(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class SpawnStop(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001255], state=2) # ON
        self.set_interact_object(triggerIds=[10001254], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001254], stateValue=0):
            return StartDelay(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class StartDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=104, key='SpawnHold', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStart(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001254], state=2) # OFF
        self.set_interact_object(triggerIds=[10001255], state=0)


initial_state = Wait
