""" trigger/02000328_bf/level_01_11.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5111], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10011" arg2="1" />
        self.set_mesh(triggerIds=[32101,32102,32103,32104,32105,32106,32107,32108,32109,32110,32111,32112,32113,32114,32115,32116,32117,32118,32119,32120,32121,32122,32123,32124,32125,32126,32127,32128,32129,32130,32131], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[42101,42102], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10015]):
            self.set_mesh(triggerIds=[32101,32102,32103,32104,32105,32106,32107,32108,32109,32110,32111,32112,32113,32114,32115,32116,32117,32118,32119,32120,32121,32122,32123,32124,32125,32126,32127,32128,32129,32130,32131], visible=True, arg3=0, delay=100, scale=1)
            self.set_mesh(triggerIds=[42101,42102], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
