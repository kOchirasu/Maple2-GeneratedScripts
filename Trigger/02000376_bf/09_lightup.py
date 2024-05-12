""" trigger/02000376_bf/09_lightup.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='1'):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LightOff01(self.ctx)


class LightOff01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9200, spawnIds=[900]):
            return LightOff02(self.ctx)
        if not self.npc_detected(boxId=9200, spawnIds=[900]):
            return RemoveTotem01(self.ctx)


class LightOff02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=2, key='InnerLight', value=1)
        self.set_user_value(triggerId=3, key='ResetInnerLight', value=1)
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LoadingDelay(self.ctx)


class RemoveTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=3, key='RemoveInnerLight', value=1)
        self.set_user_value(triggerId=2, key='InactivateLotus', value=1)
        self.set_ambient_light(primary=[96,160,157])
        self.set_directional_light(diffuseColor=[193,180,137], specularColor=[100,100,100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LoadingDelay(self.ctx)


initial_state = Wait
