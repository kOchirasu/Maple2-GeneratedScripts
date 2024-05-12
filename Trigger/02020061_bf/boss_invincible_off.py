""" trigger/02020061_bf/boss_invincible_off.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombPhase', value=2):
            return 무적해제안내(self.ctx)


class 무적해제안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9002], skill_id=70002371, level=1, is_skill_set=False)
        # <유저 웨폰 오브젝트 떨구기>
        self.set_event_ui(type=1, arg2='$02020061_BF__BOSS_INVINCIBLE_OFF__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossClear', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
