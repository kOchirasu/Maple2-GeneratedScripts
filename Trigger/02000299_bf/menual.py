""" trigger/02000299_bf/menual.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=False)
        self.set_interact_object(triggerIds=[10000490], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000490], stateValue=0):
            return 안내시작(self.ctx)


class 안내시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.select_camera(triggerId=301, enable=True)
        self.add_buff(boxIds=[104], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20003011, textId=20003011, duration=2500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 안내01(self.ctx)


class 안내01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20003012, textId=20003012, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 안내02(self.ctx)


class 안내02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.select_camera(triggerId=302, enable=True)
        self.show_guide_summary(entityId=20003013, textId=20003013, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 안내03(self.ctx)


class 안내03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.select_camera(triggerId=303, enable=True)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)
        self.show_guide_summary(entityId=20003014, textId=20003014, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 안내04(self.ctx)


class 안내04(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[104], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)
        self.set_effect(triggerIds=[604], visible=True)
        self.select_camera(triggerId=301, enable=True)
        self.show_guide_summary(entityId=20003015, textId=20003015, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 안내05(self.ctx)


class 안내05(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=104, skillId=70000107)
        self.set_effect(triggerIds=[604], visible=True)
        self.select_camera(triggerId=303, enable=False)
        self.show_guide_summary(entityId=20003016, textId=20003016, duration=2000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대기(self.ctx)


initial_state = 대기
