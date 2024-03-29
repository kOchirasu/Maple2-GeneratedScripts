""" trigger/02000329_bf/battlezone_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6603,6604], visible=False)
        self.set_mesh(triggerIds=[1511,1512,1513,1514,1515,1516,1517,1518,1519,1520], visible=True, arg3=0, delay=1000, scale=0)
        self.set_mesh(triggerIds=[19992], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(boxIds=[1103,1104]):
            return 섹터개방(self.ctx)


class 애플몽키소환(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        self.create_monster(spawnIds=[702], animationEffect=False)
        self.set_effect(triggerIds=[6603,6604], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1103,1104]):
            return 섹터개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 섹터개방(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[19992], visible=False)
        self.set_mesh(triggerIds=[1511,1512,1513,1514,1515,1516,1517,1518,1519,1520], visible=False, arg3=0, delay=0, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=102)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
