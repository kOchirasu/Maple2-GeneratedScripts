""" trigger/02000328_bf/level_01_00.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5100], is_visible=False)
        # self.spawn_monster(spawn_ids=[10000], auto_target=True)
        self.set_mesh(trigger_ids=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[41001,41002], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10002]):
            # self.set_cube(trigger_ids=[5100], is_visible=True)
            self.set_mesh(trigger_ids=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=True, start_delay=0, interval=200, fade=2)
            self.set_mesh(trigger_ids=[41001,41002], visible=False, start_delay=0, interval=0, fade=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
