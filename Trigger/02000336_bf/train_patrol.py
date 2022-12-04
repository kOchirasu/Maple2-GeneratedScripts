""" trigger/02000336_bf/train_patrol.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_mesh(triggerIds=[16004], visible=False, delay=0, scale=0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return 패트롤_01(self.ctx)
        if self.count_users(boxId=707, boxId=1):
            return 패트롤_03(self.ctx)


class 패트롤_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[147,148,149], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, boxId=1):
            return 패트롤_03(self.ctx)


class 패트롤_02(trigger_api.Trigger):
    pass


class 패트롤_03(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.
        self.create_monster(spawnIds=[191,192,193,194,195,196,197,198], animationEffect=False)
        self.set_effect(triggerIds=[7002], visible=True)
        self.set_skill(triggerIds=[5803], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[5804], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[5805], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[196]):
            return 관문_03_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=105)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(triggerIds=[8030,8031,8032,8033,8034], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
