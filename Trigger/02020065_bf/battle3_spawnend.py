""" trigger/02020065_bf/battle3_spawnend.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[811,812,813,814]):
            self.set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
            return None


initial_state = 대기
