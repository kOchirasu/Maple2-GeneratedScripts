""" trigger/02100002_bf/23_spawnholder_orange.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ActivateHolder', value=0) # 메인 트리거에서 받는 신호
        self.set_user_value(key='DungeonQuit', value=0) # ON
        self.set_interact_object(triggerIds=[10001252], state=2) # OFF
        self.set_interact_object(triggerIds=[10001253], state=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ActivateHolder', value=1):
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStart(self.ctx)


class SpawnStart(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001253], state=1) # ON
        self.set_interact_object(triggerIds=[10001252], state=2)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001253], stateValue=0):
            return StopDelay(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class StopDelay(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='SpawnHold', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStop(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class SpawnStop(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001253], state=2) # ON
        self.set_interact_object(triggerIds=[10001252], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001252], stateValue=0):
            return StartDelay(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class StartDelay(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='SpawnHold', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SpawnStart(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001252], state=2) # OFF
        self.set_interact_object(triggerIds=[10001253], state=0)


initial_state = Wait
