""" trigger/52010038_qd/heal_1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001258], state=2)
        set_interact_object(triggerIds=[10001259], state=2)
        set_interact_object(triggerIds=[10001260], state=2)
        set_interact_object(triggerIds=[10001261], state=2)
        set_interact_object(triggerIds=[10001262], state=2)
        set_interact_object(triggerIds=[10001263], state=2)
        set_interact_object(triggerIds=[10001264], state=2)
        set_interact_object(triggerIds=[10001265], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='WoundStart', value=1):
            return 랜덤조건()


class 랜덤조건(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=13):
            return 체크10001258()
        if random_condition(rate=13):
            return 체크10001259()
        if random_condition(rate=13):
            return 체크10001260()
        if random_condition(rate=13):
            return 체크10001261()
        if random_condition(rate=13):
            return 체크10001262()
        if random_condition(rate=13):
            return 체크10001263()
        if random_condition(rate=13):
            return 체크10001264()
        if random_condition(rate=13):
            return 체크10001265()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001258(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001258], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001258()


class 생성10001258(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001258], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001259(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001259], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001259()


class 생성10001259(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001259], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001260(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001260], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001260()


class 생성10001260(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001260], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001261(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001261], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001261()


class 생성10001261(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001261], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001262(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001262], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001262()


class 생성10001262(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001262], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001263(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001263], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001263()


class 생성10001263(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001263], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001264(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001264], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001264()


class 생성10001264(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001264], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


class 체크10001265(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001265], arg2=1):
            return 랜덤조건()
        if wait_tick(waitTick=500):
            return 생성10001265()


class 생성10001265(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001265], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return 랜덤조건()
        if user_value(key='WoundEnd', value=1):
            set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기()


