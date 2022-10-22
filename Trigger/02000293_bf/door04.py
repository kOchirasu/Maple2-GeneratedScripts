""" trigger/02000293_bf/door04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=1008, visible=False, initialSequence='Closed')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999997]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_actor(triggerId=1008, visible=False, initialSequence='Closed')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000530,10000521], arg2=0):
            return 트리거02시작()


class 트리거02시작(state.State):
    def on_enter(self):
        set_actor(triggerId=1008, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[2035], arg2=True)
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 트리거03시작()


class 트리거03시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[25000])
        destroy_monster(spawnIds=[25001])
        destroy_monster(spawnIds=[25002])
        destroy_monster(spawnIds=[25003])
        destroy_monster(spawnIds=[25004])
        destroy_monster(spawnIds=[25005])
        destroy_monster(spawnIds=[25006])
        destroy_monster(spawnIds=[25007])
        destroy_monster(spawnIds=[25008])
        set_actor(triggerId=1008, visible=False, initialSequence='Closed')


