""" trigger/02020112_bf/respawn.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.limit_spawn_npc_count(limitCount=200)
        self.set_user_value(key='respawn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=1):
            return 스폰시작(self.ctx)
        if self.user_value(key='respawn', value=2):
            return 종료(self.ctx)


class 스폰시작(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020112_BF__RESPAWN__0$', arg3='5000')
        self.create_monster(spawnIds=[141,142,143,144], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
