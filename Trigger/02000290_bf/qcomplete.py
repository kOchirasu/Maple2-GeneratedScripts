""" trigger/02000290_bf/qcomplete.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='dungeonclear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[10003060], questStates=[2]):
            return 완료npc리젠(self.ctx)


class 완료npc리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[915])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='dungeonclear', value=1):
            return 완료npc킬(self.ctx)


class 완료npc킬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[915])


initial_state = 대기
