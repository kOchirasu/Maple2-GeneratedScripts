""" trigger/02020063_bf/battle3_spawnend.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[811,812,813,814]):
            self.set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
            return None


initial_state = 대기
