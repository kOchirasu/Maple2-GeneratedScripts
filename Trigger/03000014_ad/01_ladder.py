""" trigger/03000014_ad/01_ladder.xml """
from common import *
import state


class 유저감지(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000066], state=1)
        set_effect(triggerIds=[201,202,211,212,221,222,231,232,241,242], visible=False)
        set_ladder(triggerIds=[101], visible=False, animationEffect=False)
        set_ladder(triggerIds=[102], visible=False, animationEffect=False)
        set_ladder(triggerIds=[111], visible=False, animationEffect=False)
        set_ladder(triggerIds=[112], visible=False, animationEffect=False)
        set_ladder(triggerIds=[121], visible=False, animationEffect=False)
        set_ladder(triggerIds=[122], visible=False, animationEffect=False)
        set_ladder(triggerIds=[131], visible=False, animationEffect=False)
        set_ladder(triggerIds=[132], visible=False, animationEffect=False)
        set_ladder(triggerIds=[141], visible=False, animationEffect=False)
        set_ladder(triggerIds=[142], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000066], arg2=0):
            return 사다리생성101()


class 사다리생성101(state.State):
    def on_enter(self):
        set_effect(triggerIds=[201,202], visible=True)
        set_ladder(triggerIds=[101], visible=True, animationEffect=True)
        set_ladder(triggerIds=[102], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성102()


class 사다리생성102(state.State):
    def on_enter(self):
        set_effect(triggerIds=[211,212], visible=True)
        set_ladder(triggerIds=[111], visible=True, animationEffect=True)
        set_ladder(triggerIds=[112], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성111()


class 사다리생성111(state.State):
    def on_enter(self):
        set_effect(triggerIds=[221,222], visible=True)
        set_ladder(triggerIds=[121], visible=True, animationEffect=True)
        set_ladder(triggerIds=[122], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성112()


class 사다리생성112(state.State):
    def on_enter(self):
        set_effect(triggerIds=[231,232], visible=True)
        set_ladder(triggerIds=[131], visible=True, animationEffect=True)
        set_ladder(triggerIds=[132], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성121()


class 사다리생성121(state.State):
    def on_enter(self):
        set_effect(triggerIds=[241,242], visible=True)
        set_ladder(triggerIds=[141], visible=True, animationEffect=True)
        set_ladder(triggerIds=[142], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저감지()


class 사다리생성122(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[122], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성131()


class 사다리생성131(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[131], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성132()


class 사다리생성132(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[132], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성141()


class 사다리생성141(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[141], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 사다리생성142()


class 사다리생성142(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[142], visible=True, animationEffect=True)
        set_timer(timerId='1', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저감지()


