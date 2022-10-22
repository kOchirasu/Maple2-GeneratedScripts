""" trigger/52000051_qd/09_lightup.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='FindLotus', value=1):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LightOff01()


class LightOff01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9200, spawnIds=[900]):
            return LightOff02()
        if not npc_detected(boxId=9200, spawnIds=[900]):
            return RemoveTotem01()


class LightOff02(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='InnerLight', value=1)
        set_user_value(triggerId=3, key='ResetInnerLight', value=1)
        set_ambient_light(primary=[0,0,0])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LoadingDelay()


class RemoveTotem01(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='RemoveInnerLight', value=1)
        set_user_value(triggerId=2, key='InactivateLotus', value=1)
        set_ambient_light(primary=[96,160,157])
        set_directional_light(diffuseColor=[193,180,137], specularColor=[100,100,100])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LoadingDelay()


