""" trigger/02100002_bf/22_spawnholder_skyblue.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='ActivateHolder', value=0) # 메인 트리거에서 받는 신호
        set_user_value(key='DungeonQuit', value=0) # ON
        set_interact_object(triggerIds=[10001250], state=2) # OFF
        set_interact_object(triggerIds=[10001251], state=0)

    def on_tick(self) -> state.State:
        if user_value(key='ActivateHolder', value=1):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SpawnStart()


class SpawnStart(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001251], state=1) # ON
        set_interact_object(triggerIds=[10001250], state=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001251], arg2=0):
            return StopDelay()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class StopDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=102, key='SpawnHold', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SpawnStop()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class SpawnStop(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001251], state=2) # ON
        set_interact_object(triggerIds=[10001250], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001250], arg2=0):
            return StartDelay()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class StartDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=102, key='SpawnHold', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SpawnStart()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001250], state=2) # OFF
        set_interact_object(triggerIds=[10001251], state=0)


