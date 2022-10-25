""" trigger/02000336_bf/boss.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90,92,93])
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return 시작_01(self.ctx)


class 시작_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7015], visible=True)
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 조직원등장(self.ctx)


class 조직원등장(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_mesh(triggerIds=[8041,8042,8043,8044], visible=False, delay=0, scale=10) # 벽 해제
        self.set_skill(triggerIds=[5801], enable=True) # 벽 날리는 스킬
        self.create_monster(spawnIds=[181,182,183])
        self.set_timer(timerId='2', seconds=2, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 웨이홍_대사01(self.ctx)


class 웨이홍_대사01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91])
        self.destroy_monster(spawnIds=[90])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=8001, enable=True)
        self.set_conversation(type=2, spawnId=11003124, script='$02000336_BF__BOSS__0$', arg4=3) # 웨이홍 대사
        self.set_skip(state=웨이홍_대사02)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이홍_대사02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 웨이홍_대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003124, script='$02000336_BF__BOSS__1$', arg4=3) # 웨이홍 대사
        self.set_skip(state=종료)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 종료(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.select_camera(triggerId=8001, enable=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 시작
