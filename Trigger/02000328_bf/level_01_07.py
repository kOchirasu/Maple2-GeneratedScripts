""" trigger/02000328_bf/level_01_07.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5107], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10007" arg2="1" />
        self.set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41701], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10006]):
            self.set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41701], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
