""" trigger/02000328_bf/level_01_08.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5108], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10008" arg2="1" />
        self.set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41801], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10006]):
            self.set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41801], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
