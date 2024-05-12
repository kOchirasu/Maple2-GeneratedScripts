""" trigger/02000328_bf/qcomplete.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='clearafter', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[999999], quest_ids=[10003061], quest_states=[2]):
            return 완료npc리젠(self.ctx)


class 완료npc리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='clearafter') >= 1:
            return 완료npc킬(self.ctx)


class 완료npc킬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])


initial_state = 대기
