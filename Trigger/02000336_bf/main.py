""" trigger/02000336_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[16003,16004], visible=False, delay=0, scale=0) # 벽 해제
        self.create_monster(spawnIds=[122,123,301,302], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.create_monster(spawnIds=[110,111,112,113,114,116,117,120,121,124,125,126,127,128,129,131,132,133,134,135,137,139,141,142,144], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, minUsers='1'):
            return 관문_01_개방_준비(self.ctx)


class 관문_01_개방_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.
        self.create_monster(spawnIds=[309,311,313,172,173], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[127]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=105)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(triggerIds=[8010,8011,8012,8013,8014], visible=False, delay=0, scale=10) # 벽 해제
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[125]):
            return 관문_02_개방(self.ctx)


class 관문_02_개방_준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[127]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=113)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[16017,16018], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
