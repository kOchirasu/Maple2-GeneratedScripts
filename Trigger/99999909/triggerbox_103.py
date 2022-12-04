""" trigger/99999909/triggerbox_103.xml """
import trigger_api


class 블록(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036,3037], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 블록생성(self.ctx)


class 블록생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[3031,3032,3033,3034,3035,3036,3037], visible=True, meshCount=4, arg4=0, delay=1)


initial_state = 블록
