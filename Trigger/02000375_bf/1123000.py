""" trigger/02000375_bf/1123000.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3400], visible=True, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SecondPhaseEnd', value=1):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3400], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
