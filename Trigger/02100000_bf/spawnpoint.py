""" trigger/02100000_bf/spawnpoint.xml """
import trigger_api


class 리스폰변경_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            pass


initial_state = 리스폰변경_1
