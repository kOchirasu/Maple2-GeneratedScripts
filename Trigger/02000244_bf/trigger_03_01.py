""" trigger/02000244_bf/trigger_03_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[705,706], visible=False)


initial_state = 대기
