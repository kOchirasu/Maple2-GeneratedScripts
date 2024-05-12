""" trigger/02010058_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=True)


initial_state = 시작
