""" trigger/63000092_cs/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4023,4024], visible=False)
            self.set_mesh(triggerIds=[4021,4022,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 일요일(self.ctx) # 일요일이면 다리5단
        if self.day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4024], visible=False)
            self.set_mesh(triggerIds=[4021,4022,4023,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 월요일(self.ctx) # 월요일이면 다리6단
        if self.day_of_week(dayOfWeeks=[3], desc='화요일'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=False, desc='바운딩 메쉬를 끈다')
            # 화요일이면 다리7단(다 놓임. 완성. 바운딩도 꺼짐)
            return 화요일(self.ctx)
        if self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4026,4027], visible=False)
            self.set_mesh(triggerIds=[4025], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 수요일(self.ctx) # 수요일이면 다리1단
        if self.day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4027], visible=False)
            self.set_mesh(triggerIds=[4025,4026], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 목요일(self.ctx) # 목요일이면 다리2단
        if self.day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026], visible=False)
            self.set_mesh(triggerIds=[4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 금요일(self.ctx) # 금요일이면 다리3단
        if self.day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            self.set_mesh(triggerIds=[4022,4023,4024], visible=False)
            self.set_mesh(triggerIds=[4021,4025,4026,4027], visible=True)
            self.set_mesh(triggerIds=[4030], visible=True)
            return 토요일(self.ctx) # 토요일이면 다리4단


class 일요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 월요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 화요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[3], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 수요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 목요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 금요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


class 토요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            return 대기(self.ctx) # 다음날이면 다시 체크


initial_state = 대기
