""" trigger/52000007_qd/exit.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 초5(self.ctx)


class 초5(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.create_item(spawnIds=[9001,9002,9003,9004,9005], triggerId=101)
            self.add_buff(boxIds=[101], skillId=70000019, level=1)
            return 초30(self.ctx)


class 초30(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='300', seconds=300, startDelay=0)
        self.set_event_ui(type=1, arg2='$52000007_QD__EXIT__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='300'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.move_user(mapId=2000064, portalId=800, boxId=0)
            return 유저감지(self.ctx)


initial_state = 유저감지
