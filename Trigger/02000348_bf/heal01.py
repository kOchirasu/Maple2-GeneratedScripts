""" trigger/02000348_bf/heal01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000803], state=0)
        self.set_skill(trigger_ids=[701], enable=False)


initial_state = 대기
