""" trigger/02100000_bf/spawnpoint.xml """
import common


class 리스폰변경_1(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return None


initial_state = 리스폰변경_1
