""" trigger/02000328_bf/qcomplete.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='clearafter', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[999999], questIds=[10003061], questStates=[2]):
            return 완료npc리젠(self.ctx)


class 완료npc리젠(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='clearafter', value=1):
            return 완료npc킬(self.ctx)


class 완료npc킬(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2002])


initial_state = 대기
