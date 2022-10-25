""" trigger/52010022_qd/main.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1003,1004], visible=True, arg3=0, delay=0, scale=0)


initial_state = idle
