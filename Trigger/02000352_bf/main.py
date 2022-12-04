""" trigger/02000352_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[900001], visible=False) # Sound EFfect Off
        self.set_effect(triggerIds=[900002], visible=False) # Sound EFfect Off
        self.set_effect(triggerIds=[900003], visible=False) # Sound EFfect Off
        self.set_effect(triggerIds=[900004], visible=False) # Sound EFfect Off
        self.set_effect(triggerIds=[900005], visible=False) # Sound EFfect Off
        self.set_interact_object(triggerIds=[10000822], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return 관문01_시작(self.ctx)
        if self.count_users(boxId=703, boxId=1):
            return 관문_03_시작(self.ctx)


class 관문01_시작(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[11,12,13,14,15,16,17], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[11,12,13,14,15,16,17]):
            return 관문_01_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000822], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 관문_02_시작(self.ctx)


class 관문_02_시작(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[21,22,23,24,25,26,27,28,29], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[21,22,23,24,25,26,27,28,29]):
            return 관문_02_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요
        self.set_interact_object(triggerIds=[10000823], state=1)
        self.set_interact_object(triggerIds=[10000824], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return 관문_03_시작(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)


class 관문_03_시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[31,32,33], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[31,32]):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6004], visible=False, delay=0, scale=10) # 벽 해제
        self.set_mesh(triggerIds=[6007], visible=True, delay=0, scale=10) # 화살표 표시
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)


initial_state = 시작
