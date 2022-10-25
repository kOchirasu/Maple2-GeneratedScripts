""" trigger/02000495_bf/broken_80.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[701], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 초대기5(self.ctx)


class 초대기5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 초대기30(self.ctx)


class 초대기30(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 스킬발동(self.ctx)


class 스킬발동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[701], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001,2101]):
            return 다리생성(self.ctx)


class 다리생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111], visible=True, arg3=0, delay=100, scale=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
