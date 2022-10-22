""" trigger/02000090_bf/apply_01.xml """
from common import *
import state


class 대기0(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1000], visible=False)
        set_effect(triggerIds=[1001], visible=False)
        set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 대기1()
        if random_condition(rate=33):
            return 대기2()
        if random_condition(rate=34):
            return 대기3()
        if object_interacted(interactIds=[10000360], arg2=0):
            return 이펙트1()


class 대기1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_effect(triggerIds=[1000], visible=True)
        set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기0()
        if object_interacted(interactIds=[10000360], arg2=0):
            return 이펙트1()


class 대기2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=7)
        set_effect(triggerIds=[1000], visible=True)
        set_effect(triggerIds=[1001], visible=True)
        set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기0()
        if object_interacted(interactIds=[10000360], arg2=0):
            return 이펙트1()


class 대기3(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=1)
        set_effect(triggerIds=[1000], visible=True)
        set_effect(triggerIds=[1001], visible=True)
        set_interact_object(triggerIds=[10000360], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기0()
        if object_interacted(interactIds=[10000360], arg2=0):
            return 이펙트1()


class 이펙트1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        set_effect(triggerIds=[1000], visible=True)
        set_effect(triggerIds=[1001], visible=True)
        set_effect(triggerIds=[2000], visible=True)
        set_effect(triggerIds=[2001], visible=True)
        set_effect(triggerIds=[2002], visible=True)
        set_effect(triggerIds=[2003], visible=True)
        set_effect(triggerIds=[2004], visible=True)
        set_effect(triggerIds=[2005], visible=True)
        set_effect(triggerIds=[2006], visible=True)
        set_effect(triggerIds=[2007], visible=True)
        set_effect(triggerIds=[1000], visible=False)
        set_effect(triggerIds=[1001], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1000], visible=False)
        set_effect(triggerIds=[1001], visible=False)
        set_effect(triggerIds=[2000], visible=False)
        set_effect(triggerIds=[2001], visible=False)
        set_effect(triggerIds=[2002], visible=False)
        set_effect(triggerIds=[2003], visible=False)
        set_effect(triggerIds=[2004], visible=False)
        set_timer(timerId='20', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 대기0()


