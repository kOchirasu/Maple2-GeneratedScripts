""" trigger/99999840/invasion_portal.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=0)
        self.set_interact_object(triggerIds=[10002183], state=2, arg3=False)


class 포탈열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1)
        self.set_interact_object(triggerIds=[10002183], state=1, arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            self.reset_timer(timerId='1')
            return 포탈닫힘(self.ctx)
        if self.object_interacted(interactIds=[10002183], stateValue=2):
            return 유저이동(self.ctx)


class 유저이동(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=1)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=2000, value=1):
            return 포탈열림(self.ctx)


class 포탈닫힘(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=0)
        self.set_timer(timerId='2', seconds=60, startDelay=1)
        self.set_interact_object(triggerIds=[10002183], state=2, arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.time_expired(timerId='2'):
            self.reset_timer(timerId='2')
            return 대기(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002183], state=2, arg3=False)


initial_state = 대기
