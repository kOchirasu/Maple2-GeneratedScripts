""" trigger/02010086_bf/boss.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=799, boxId=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[995,999,998])
        self.create_monster(spawnIds=[199], animationEffect=True) # (임시) 보스몹 스폰
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timerId='10'):
            return 소환_01(self.ctx)


class 소환_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[181,188], animationEffect=True) # (임시) 보스몹 스폰
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timerId='10'):
            return 소환_02(self.ctx)


class 소환_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[182,187], animationEffect=True) # (임시) 보스몹 스폰
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timerId='10'):
            return 소환_03(self.ctx)


class 소환_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[183,186], animationEffect=True) # (임시) 보스몹 스폰
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timerId='10'):
            return 소환_04(self.ctx)


class 소환_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[184,185], animationEffect=True) # (임시) 보스몹 스폰
        self.set_timer(timerId='20', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timerId='20'):
            return 소환_05(self.ctx)


class 소환_05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[996], animationEffect=True) # (임시) 보스몹 스폰

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈_개방(self.ctx)


class 포탈_개방(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[181,182,183,184,185,186,187,188,997,996,995])
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.set_mesh(triggerIds=[1098], visible=False, delay=0, scale=10) # 벽 해제
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 포탈 개방

    def on_exit(self):
        self.hide_guide_summary(entityId=112)


initial_state = 대기
