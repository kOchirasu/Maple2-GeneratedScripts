""" trigger/02010026_bf/06_ladder14.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000909], state=1)
        set_ladder(triggerIds=[201], visible=False, animationEffect=False)
        set_ladder(triggerIds=[202], visible=False, animationEffect=False)
        set_ladder(triggerIds=[203], visible=False, animationEffect=False)
        set_ladder(triggerIds=[204], visible=False, animationEffect=False)
        set_ladder(triggerIds=[205], visible=False, animationEffect=False)
        set_ladder(triggerIds=[206], visible=False, animationEffect=False)
        set_ladder(triggerIds=[207], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000909], arg2=0):
            return 사다리생성01()


class 사다리생성01(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[201], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성02()


class 사다리생성02(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[202], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성03()


class 사다리생성03(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[203], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성04()


class 사다리생성04(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[204], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성05()


class 사다리생성05(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[205], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성06()


class 사다리생성06(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[206], visible=True, animationEffect=True, animationDelay=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 사다리생성07()


class 사다리생성07(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[207], visible=True, animationEffect=True, animationDelay=5)
        set_timer(timerId='1', seconds=10, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


