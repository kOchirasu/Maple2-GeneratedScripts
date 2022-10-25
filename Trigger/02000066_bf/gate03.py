""" trigger/02000066_bf/gate03.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[3003])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=False)
        self.set_interact_object(triggerIds=[10000335], state=0)
        self.create_monster(spawnIds=[3003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3003]):
            return 게이트열림(self.ctx)


class 게이트열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_interact_object(triggerIds=[10000335], state=1)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20000664, textId=20000664)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20000664)
            return 게이트닫힘(self.ctx)


class 게이트닫힘(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000335], stateValue=0):
            return 생성(self.ctx)


initial_state = 시작
