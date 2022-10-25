""" trigger/02000328_bf/level_01_03.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5103], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10003" arg2="1" />
        self.set_mesh(triggerIds=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41301,41302,41303], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10002]):
            self.set_mesh(triggerIds=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41301,41302,41303], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
