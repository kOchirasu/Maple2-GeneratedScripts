""" trigger/80000021_bonus/80000021_main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198], visible=True) # 뒷문준비 / 막힌 상태
        self.create_monster(spawnIds=[101,102,103,104,105], animationEffect=False) # 101-4: 용병 우르자들 / 105:연출용 핑크빈
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 출구포털준비 / 꺼놓은 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 안내(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=1, textId=26300734, duration=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 몬스터체크(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=1, textId=26300734, duration=10000) # 가이드 텍스트 ON : 슈퍼파워 핑크빈의 용병, 험상궂은 우르자들을 처치하세요!

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104]):
            return 길을열어라(self.ctx)


class 길을열어라(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Dead_A') # 핑크빈 빠잉
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 출구포털 / 활성화
        self.create_item(spawnIds=[5001]) # 초록코인

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 문열기00(self.ctx)


class 문열기00(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=2, textId=26300735, duration=10000) # 가이드 텍스트 ON : 문이 열렸어요. 출구에 있는 초록 코인을 주운 후 이동하세요.
        self.set_mesh(triggerIds=[198], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기01(self.ctx)


class 문열기01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[180,182,184], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기02(self.ctx)


class 문열기02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[181,183,185], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기03(self.ctx)


class 문열기03(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[186,188,190], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기04(self.ctx)


class 문열기04(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[187,189,191], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기05(self.ctx)


class 문열기05(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[192,194,196], visible=False) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 문열기06(self.ctx)


class 문열기06(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[193,195,197], visible=False) # 뒷문 / 열기
        self.destroy_monster(spawnIds=[105]) # 핑크빈 소멸

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
