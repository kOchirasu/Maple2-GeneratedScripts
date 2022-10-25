""" trigger/80000007_bonus/trigger_14.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[303]):
            return 막힘(self.ctx)


class 막힘(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409], visible=False)


initial_state = 대기
