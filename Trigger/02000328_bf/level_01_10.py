""" trigger/02000328_bf/level_01_10.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5110], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10010" arg2="1" />
        self.set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[42001], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10006]):
            self.set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[42001], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
