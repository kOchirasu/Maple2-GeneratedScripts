""" trigger/02000329_bf/battlezone_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6609,6610], visible=False)
        self.set_mesh(triggerIds=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], visible=True, arg3=0, delay=1000, scale=0)
        self.set_mesh(triggerIds=[19994], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(boxIds=[1109,1110]):
            return 섹터개방(self.ctx)


class 애플몽키소환(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        self.create_monster(spawnIds=[704], animationEffect=False)
        self.set_effect(triggerIds=[6609,6610], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1109,1110]):
            return 섹터개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 섹터개방(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[19994], visible=False)
        self.set_mesh(triggerIds=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], visible=False, arg3=0, delay=0, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=102)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
