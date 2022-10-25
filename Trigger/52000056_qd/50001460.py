""" trigger/52000056_qd/50001460.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, delay=0, scale=0)
        self.set_gravity(gravity=-9.8)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103,104,105,106]):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000056, portalId=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선01(self.ctx)


class PC말풍선01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__0$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 낙하준비(self.ctx)


class 낙하준비(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008], visible=False, arg3=0, delay=200, scale=2)
        self.set_gravity(gravity=-37)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 낙하시작(self.ctx)


class 낙하시작(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 낙하종료(self.ctx)


class 낙하종료(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__1$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC말풍선03(self.ctx)


class PC말풍선03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__2$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_effect(triggerIds=[601], visible=True)
            self.set_effect(triggerIds=[602], visible=True)
            self.set_effect(triggerIds=[603], visible=True)
            self.set_effect(triggerIds=[604], visible=True)
            self.set_effect(triggerIds=[605], visible=True)
            self.set_effect(triggerIds=[606], visible=True)
            self.set_effect(triggerIds=[607], visible=True)
            self.set_effect(triggerIds=[608], visible=True)
            self.set_effect(triggerIds=[609], visible=True)
            self.set_effect(triggerIds=[610], visible=True)
            self.set_effect(triggerIds=[611], visible=True)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.set_gravity(gravity=-9.8)
            return 이펙트종료대기(self.ctx)


class 이펙트종료대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            self.set_effect(triggerIds=[601], visible=False)
            self.set_effect(triggerIds=[602], visible=False)
            self.set_effect(triggerIds=[603], visible=False)
            self.set_effect(triggerIds=[604], visible=False)
            self.set_effect(triggerIds=[605], visible=False)
            self.set_effect(triggerIds=[606], visible=False)
            self.set_effect(triggerIds=[607], visible=False)
            self.set_effect(triggerIds=[608], visible=False)
            self.set_effect(triggerIds=[609], visible=False)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_effect(triggerIds=[611], visible=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
