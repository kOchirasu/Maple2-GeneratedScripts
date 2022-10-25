""" trigger/02000328_bf/level_01_00.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5100], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10000" arg2="1" />
        self.set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41001,41002], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10002]):
            self.set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41001,41002], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
