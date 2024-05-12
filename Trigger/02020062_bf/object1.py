""" trigger/02020062_bf/object1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=False)
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=0)
        self.set_interact_object(trigger_ids=[12000107], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=1):
            return 레버1_가이드메시지(self.ctx)


class 레버1_가이드메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[721], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.user_detected(box_ids=[9011]):
            self.set_event_ui(type=1, arg2='$02020062_BF__OBJECT1__0$', arg3='5000', arg4='9011')
            return 레버1_체크(self.ctx)


class 레버1_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            return 레버1_발동(self.ctx)


class 레버1_발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_interact_object(trigger_ids=[12000107], state=1)
        self.set_event_ui(type=1, arg2='$02020062_BF__OBJECT1__1$', arg3='5000', arg4='9011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000107], state=0):
            return 레버1_몬스터등장(self.ctx)


class 레버1_몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return 레버1_재활성(self.ctx)


class 레버1_재활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000107], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2) and self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000107], state=0):
            return 레버1_재활성_대기(self.ctx)


class 레버1_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2) and self.monster_dead(spawn_ids=[701]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return 레버1_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=False)
        self.set_user_value(trigger_id=99990014, key='EliteSpawn', value=2)
        self.destroy_monster(spawn_ids=[721], arg2=False)
        self.set_interact_object(trigger_ids=[12000107], state=2)


initial_state = 대기
