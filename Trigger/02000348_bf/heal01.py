""" trigger/02000348_bf/heal01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000803], state=0)
        self.set_skill(triggerIds=[701], enable=False)


initial_state = 대기
