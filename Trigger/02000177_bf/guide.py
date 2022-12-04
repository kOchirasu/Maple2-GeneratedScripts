""" trigger/02000177_bf/guide.xml """
import trigger_api


class guide(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return Guide_Climb(self.ctx)


class Guide_Climb(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20001771, textId=20001771, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return Guide_Climb_02(self.ctx)


class Guide_Climb_02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20001771, textId=20001771, duration=4000)


initial_state = guide
