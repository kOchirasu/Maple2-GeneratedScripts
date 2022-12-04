""" trigger/99999841/invasion_portal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=0)
        self.set_interact_object(triggerIds=[10002184], state=2, arg3=False)


class 포탈열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1)
        self.set_interact_object(triggerIds=[10002184], state=1, arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            self.reset_timer(timerId='1')
            return 포탈닫힘(self.ctx)
        if self.object_interacted(interactIds=[10002184], stateValue=2):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=1000, value=1):
            return 포탈열림(self.ctx)


class 포탈닫힘(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990010, key='PCmove', value=0)
        self.set_timer(timerId='2', seconds=60, startDelay=1)
        self.set_interact_object(triggerIds=[10002184], state=2, arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.time_expired(timerId='2'):
            self.reset_timer(timerId='2')
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002184], state=2, arg3=False)


initial_state = 대기
