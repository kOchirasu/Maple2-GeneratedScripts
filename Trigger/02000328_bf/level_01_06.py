""" trigger/02000328_bf/level_01_06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5106], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10006" arg2="1" />
        self.set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41601,41602,41603], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10006]):
            self.set_cube(triggerIds=[5106], isVisible=True)
            self.set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41601,41602,41603], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
