""" trigger/99999840/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Team1Battle', value=0)
        self.set_user_value(triggerId=99990003, key='Start', value=0)
        self.set_user_value(triggerId=99990004, key='Start', value=0)
        self.set_user_value(triggerId=99990005, key='Start', value=0)
        self.set_user_value(triggerId=99990015, key='Start', value=0)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9001, boxId=6, operator='Equal'):
            return 세팅(self.ctx)


class 세팅(common.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=99999841, portalId=1, triggerId=9001, count=3)
        self.set_event_ui(type=1, arg2='잠시 후 경기가 시작됩니다.', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=1, value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='경기 시작!\n당신은 A팀입니다.', arg3='3000')
        self.set_user_value(triggerId=99990002, key='Team1Battle', value=1)
        self.set_user_value(triggerId=99990003, key='Start', value=1)
        self.set_user_value(triggerId=99990004, key='Start', value=1)
        self.set_user_value(triggerId=99990005, key='Start', value=1)
        self.set_user_value(triggerId=99990015, key='Start', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메시지1(self.ctx)


class 메시지1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='검은 군단을 해치우고 자원을 획득하세요.\n획득한 자원을 20개 모아서 보스를 불러내세요.\n한번에 최대 9개의 자원을 들 수 있습니다.', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return A팀승리(self.ctx)
        if self.dungeon_variable(varId=3, value=1):
            return B팀승리(self.ctx)


class A팀승리(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='A팀이 승리했습니다!', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class B팀승리(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='B팀이 승리했습니다!', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Team1Battle', value=0)
        self.set_user_value(triggerId=99990003, key='Start', value=0)
        self.set_user_value(triggerId=99990004, key='Start', value=0)
        self.set_user_value(triggerId=99990005, key='Start', value=0)
        self.set_interact_object(triggerIds=[10002175], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002176], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002177], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002178], state=0, arg3=False)


initial_state = 대기
