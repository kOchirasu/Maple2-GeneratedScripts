""" trigger/02000349_bf/wall_19.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[119]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[119]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
