""" trigger/02000111_bf/101_2.xml """
from common import *
import state


class 시작대기중1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000165], state=1)
        set_mesh(triggerIds=[302], visible=False)
        set_effect(triggerIds=[402], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000165], arg2=0):
            return 열기1()


class 시작대기중2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000165], state=1)
        set_mesh(triggerIds=[302], visible=False)
        set_effect(triggerIds=[402], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000165], arg2=0):
            return 열기1()


class 열기1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[302], visible=True)
        set_effect(triggerIds=[402], visible=True)
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=202, spawnIds=[103]):
            return 아이템1()
        if npc_detected(boxId=202, spawnIds=[104]):
            return 아이템2()
        if npc_detected(boxId=202, spawnIds=[105]):
            return 아이템3()
        if time_expired(timerId='1'):
            return 시작대기중2()


class 아이템1(state.State):
    def on_enter(self):
        create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        set_mesh(triggerIds=[302], visible=False)
        set_interact_object(triggerIds=[10000165], state=1)
        set_effect(triggerIds=[402], visible=True)
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if true():
            return 빠지기1()


class 아이템2(state.State):
    def on_enter(self):
        create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        set_mesh(triggerIds=[302], visible=False)
        set_interact_object(triggerIds=[10000165], state=1)
        set_effect(triggerIds=[402], visible=True)
        destroy_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if true():
            return 빠지기2()


class 아이템3(state.State):
    def on_enter(self):
        create_item(spawnIds=[502], triggerId=0, itemId=10000165)
        set_mesh(triggerIds=[302], visible=False)
        set_interact_object(triggerIds=[10000165], state=1)
        set_effect(triggerIds=[402], visible=True)
        destroy_monster(spawnIds=[105])

    def on_tick(self) -> state.State:
        if true():
            return 빠지기3()


class 빠지기1(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 시작대기중2()


class 빠지기2(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 시작대기중2()


class 빠지기3(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 시작대기중2()


