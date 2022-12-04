""" trigger/80000011_bonus/mainprocess_christmastree.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 이벤트대기중(self.ctx)


class 이벤트대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[201], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[202], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[203], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[204], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 사다리나타남(self.ctx)


class 사다리나타남(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[201], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[202], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[203], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[204], visible=True, animationEffect=True)
        self.set_timer(timerId='2', seconds=30, startDelay=1, interval=1, vOffset=-90)
        self.show_guide_summary(entityId=26300385, textId=26300385)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26300385)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
