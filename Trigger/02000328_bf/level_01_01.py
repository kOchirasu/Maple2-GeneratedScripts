""" trigger/02000328_bf/level_01_01.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5101], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10001" arg2="1" />
        self.set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41101,41102], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10002]):
            self.set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41101,41102], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
