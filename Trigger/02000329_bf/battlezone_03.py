""" trigger/02000329_bf/battlezone_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6605,6606,6607,6608], visible=False)
        self.set_mesh(triggerIds=[1521,1522,1523,1524,1525,1526,1527,1528,1529,1530], visible=True, arg3=0, delay=1000, scale=0)
        self.set_mesh(triggerIds=[19993], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[703]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(boxIds=[1105,1106,1107,1108]):
            return 섹터개방(self.ctx)


class 애플몽키소환(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        self.create_monster(spawnIds=[703], animationEffect=False)
        self.set_effect(triggerIds=[6605,6606,6607,6608], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105,1106,1107,1108]):
            return 섹터개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 섹터개방(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[19993], visible=False)
        self.set_mesh(triggerIds=[1521,1522,1523,1524,1525,1526,1527,1528,1529,1530], visible=False, arg3=0, delay=0, scale=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=102)


class 종료(common.Trigger):
    pass


initial_state = 대기
