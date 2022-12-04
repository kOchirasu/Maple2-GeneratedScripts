""" trigger/51000001_dg/chest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000013,11000014,11000015,11000016,11000017], state=2)


initial_state = 대기
