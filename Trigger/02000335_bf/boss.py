""" trigger/02000335_bf/boss.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=991, isEnable=True)
        self.enable_spawn_point_pc(spawnId=992, isEnable=False)
        self.set_mesh(triggerIds=[6311,6312,6313,6314,6315], visible=True, delay=1, scale=1) # 벽 생성
        self.set_effect(triggerIds=[6921], visible=False) # BG\Common\Eff_Com_ObjectShake.xml
        self.create_monster(spawnIds=[149], animationEffect=False) # 기본 배치 될 NPC 등장

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=710, boxId=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[149]):
            return 화물문_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=105)


class 화물문_개방(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=991, isEnable=False)
        self.enable_spawn_point_pc(spawnId=992, isEnable=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20003362) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(triggerIds=[7991,7992,7993], visible=False, delay=0, scale=0) # 문 파괴
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 화물문_개방_종료(self.ctx)
        if self.count_users(boxId=711, boxId=1):
            return 보스등장연출_00(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=106)


class 화물문_개방_종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=711, boxId=1):
            return 보스등장연출_00(self.ctx)


class 보스등장연출_00(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000335_BF__BOSS__0$', arg3='3000')
        self.set_effect(triggerIds=[6921], visible=True) # BG\Common\Eff_Com_ObjectShake.xml
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 보스등장연출_01(self.ctx)


class 보스등장연출_01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[141,142,143,144,145,146,147,148]) # 기본 배치 된 NPC 삭제
        self.set_skill(triggerIds=[5801], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[5802], enable=True) # 벽 날리는 스킬
        self.set_effect(triggerIds=[6911], visible=True)
        self.set_effect(triggerIds=[6912], visible=True)
        self.create_monster(spawnIds=[199], animationEffect=False) # 보스 몬스터 등장
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_1003')
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 보스등장연출_02(self.ctx)
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)


class 보스등장연출_02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5803], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[5804], enable=True) # 벽 날리는 스킬
        self.set_effect(triggerIds=[6913], visible=True)
        self.set_effect(triggerIds=[6914], visible=True)
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 보스등장연출_03(self.ctx)
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)


class 보스등장연출_03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5805], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[5806], enable=True) # 벽 날리는 스킬
        self.set_effect(triggerIds=[6915], visible=True)
        self.set_effect(triggerIds=[6916], visible=True)
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)


class 포탈_개방(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.set_mesh(triggerIds=[6311,6312,6313,6314,6315], visible=False, delay=0, scale=10) # 벽 해제
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 포탈 개방

    def on_exit(self):
        self.hide_guide_summary(entityId=112)


initial_state = 대기
