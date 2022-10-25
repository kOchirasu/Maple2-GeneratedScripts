""" trigger/99999841/boss_message.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=100, value=1):
            return 메시지1(self.ctx)


class 메시지1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀의 보스가 등장했습니다!', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
