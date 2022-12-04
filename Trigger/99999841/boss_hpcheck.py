""" trigger/99999841/boss_hpcheck.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=110, value=1):
            return 메시지1(self.ctx)


class 메시지1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀의 보스 체력이 70% 이하입니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=120, value=1):
            return 메시지2(self.ctx)


class 메시지2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀의 보스 체력이 50% 이하입니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=130, value=1):
            return 메시지3(self.ctx)


class 메시지3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀의 보스 체력이 30% 이하입니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=140, value=1):
            return 메시지4(self.ctx)


class 메시지4(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀의 보스 체력이 10% 이하입니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
