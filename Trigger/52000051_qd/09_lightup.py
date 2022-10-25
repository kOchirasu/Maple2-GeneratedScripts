""" trigger/52000051_qd/09_lightup.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FindLotus', value=1):
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LightOff01(self.ctx)


class LightOff01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9200, spawnIds=[900]):
            return LightOff02(self.ctx)
        if not self.npc_detected(boxId=9200, spawnIds=[900]):
            return RemoveTotem01(self.ctx)


class LightOff02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='InnerLight', value=1)
        self.set_user_value(triggerId=3, key='ResetInnerLight', value=1)
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LoadingDelay(self.ctx)


class RemoveTotem01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='RemoveInnerLight', value=1)
        self.set_user_value(triggerId=2, key='InactivateLotus', value=1)
        self.set_ambient_light(primary=[96,160,157])
        self.set_directional_light(diffuseColor=[193,180,137], specularColor=[100,100,100])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LoadingDelay(self.ctx)


initial_state = Wait
