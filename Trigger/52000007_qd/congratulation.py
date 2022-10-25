""" trigger/52000007_qd/congratulation.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200], visible=False)
        self.set_effect(triggerIds=[201], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 축하대기1(self.ctx)


class 축하대기1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.bonus_game_reward_detected(boxId=101, arg2=True):
            return 축하1(self.ctx)


class 축하1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200], visible=True)
        self.set_effect(triggerIds=[201], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 축하2(self.ctx)


class 축하2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$52000007_QD__CONGRATULATION__0$')
        self.set_conversation(type=1, spawnId=101, script='$52000007_QD__CONGRATULATION__1$')
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 완료(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[200], visible=False)
        self.set_effect(triggerIds=[201], visible=False)


class 완료(common.Trigger):
    pass


initial_state = 대기
