""" trigger/02000328_bf/level_01_00.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[5100], isVisible=False)
        # self.create_monster(spawnIds=[10000], animationEffect=True)
        self.set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[41001,41002], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10002]):
            # self.set_cube(triggerIds=[5100], isVisible=True)
            self.set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[41001,41002], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
