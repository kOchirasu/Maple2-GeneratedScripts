""" trigger/02000328_bf/level_01_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5109], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10009" arg2="1" />
        self.set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41901], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10006]):
            self.set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41901], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
