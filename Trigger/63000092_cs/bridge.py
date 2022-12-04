""" trigger/63000092_cs/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4023,4024], visible=False)
            self.set_mesh(triggerIds=[4021,4022,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 일요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4024], visible=False)
            self.set_mesh(triggerIds=[4021,4022,4023,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 월요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[3], desc='화요일'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=False, desc='바운딩 메쉬를 끈다')
            return 화요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4026,4027], visible=False)
            self.set_mesh(triggerIds=[4025], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 수요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4027], visible=False)
            self.set_mesh(triggerIds=[4025,4026], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 목요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026], visible=False)
            self.set_mesh(triggerIds=[4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 금요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4022,4023,4024], visible=False)
            self.set_mesh(triggerIds=[4021,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 토요일(self.ctx)


class 일요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 월요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 화요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[3], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 수요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 목요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 금요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            return 대기(self.ctx)


class 토요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            return 대기(self.ctx)


initial_state = 대기
