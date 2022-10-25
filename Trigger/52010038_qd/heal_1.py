""" trigger/52010038_qd/heal_1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001258], state=2)
        self.set_interact_object(triggerIds=[10001259], state=2)
        self.set_interact_object(triggerIds=[10001260], state=2)
        self.set_interact_object(triggerIds=[10001261], state=2)
        self.set_interact_object(triggerIds=[10001262], state=2)
        self.set_interact_object(triggerIds=[10001263], state=2)
        self.set_interact_object(triggerIds=[10001264], state=2)
        self.set_interact_object(triggerIds=[10001265], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='WoundStart', value=1):
            return 랜덤조건(self.ctx)


class 랜덤조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=13):
            return 체크10001258(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001259(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001260(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001261(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001262(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001263(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001264(self.ctx)
        if self.random_condition(rate=13):
            return 체크10001265(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001258(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001258], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001258(self.ctx)


class 생성10001258(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001258], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001259(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001259], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001259(self.ctx)


class 생성10001259(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001259], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001260(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001260], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001260(self.ctx)


class 생성10001260(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001260], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001261(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001261], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001261(self.ctx)


class 생성10001261(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001261], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001262(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001262], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001262(self.ctx)


class 생성10001262(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001262], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001263(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001263], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001263(self.ctx)


class 생성10001263(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001263], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001264(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001264], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001264(self.ctx)


class 생성10001264(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001264], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


class 체크10001265(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001265], stateValue=1):
            return 랜덤조건(self.ctx)
        if self.wait_tick(waitTick=500):
            return 생성10001265(self.ctx)


class 생성10001265(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001265], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return 랜덤조건(self.ctx)
        if self.user_value(key='WoundEnd', value=1):
            self.set_user_value(triggerId=993001, key='WoundStart', value=0)
            return 대기(self.ctx)


initial_state = 대기
