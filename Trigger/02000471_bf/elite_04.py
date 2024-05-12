""" trigger/02000471_bf/elite_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_value(key='10002022clear', value=1) and self.user_value(key='SpawnCheck', value=1):
            return spawn(self.ctx)


class spawn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Buff', value=1):
            return buff(self.ctx)


class buff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1999], skill_id=70002031, level=1, is_player=True, is_skill_set=False)
        self.add_buff(box_ids=[304], skill_id=70002031, level=1, is_player=True, is_skill_set=False)


initial_state = idle
