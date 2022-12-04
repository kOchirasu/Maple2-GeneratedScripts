""" trigger/02000328_bf/level_01_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5105], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10005" arg2="1" />
        self.set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41501,41502], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10002]):
            self.set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41501,41502], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
