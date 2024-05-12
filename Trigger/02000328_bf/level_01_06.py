""" trigger/02000328_bf/level_01_06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5106], is_visible=False)
        # self.spawn_monster(spawn_ids=[10006], auto_target=True)
        self.set_mesh(trigger_ids=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[41601,41602,41603], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10006]):
            self.set_cube(trigger_ids=[5106], is_visible=True)
            self.set_mesh(trigger_ids=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=True, start_delay=0, interval=200, fade=2)
            self.set_mesh(trigger_ids=[41601,41602,41603], visible=False, start_delay=0, interval=0, fade=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
