""" trigger/02000328_bf/level_01_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[5104], isVisible=False)
        # self.create_monster(spawnIds=[10004], animationEffect=True)
        self.set_mesh(triggerIds=[31401,31402,31403,31404,31405,31406,31407,31408,31409,31410,31411,31412,31413,31414,31415,31416,31417,31418,31419], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41401,41402], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10002]):
            # self.set_cube(triggerIds=[5104], isVisible=True)
            self.set_mesh(triggerIds=[31401,31402,31403,31404,31405,31406,31407,31408,31409,31410,31411,31412,31413,31414,31415,31416,31417,31418,31419], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41401,41402], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
