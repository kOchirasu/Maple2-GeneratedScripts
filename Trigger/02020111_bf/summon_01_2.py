""" trigger/02020111_bf/summon_01_2.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 소환준비(self.ctx)


class 소환준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') >= 1:
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900005, key='Lapenta_Attack_Guide', value=1)
        # self.set_event_ui(type=1, arg2='$02020111_BF__SUMMON_01_2__0$', arg3='3000')
        self.spawn_monster(spawn_ids=[115,116,117,118])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=[52,48,38])
        self.set_directional_light(diffuse_color=[0,0,0], specular_color=[206,174,84])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon') >= 0:
            return 시작(self.ctx)


initial_state = 시작
