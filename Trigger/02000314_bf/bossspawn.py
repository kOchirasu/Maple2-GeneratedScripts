""" trigger/02000314_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003140, textId=20003140, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(triggerId=301, enable=True)
        self.add_buff(boxIds=[102], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.create_monster(spawnIds=[99], animationEffect=False)
        self.set_skip(state=종료체크)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 종료체크(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=301, enable=False)
        self.remove_buff(boxId=102, skillId=70000107)


class 종료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 종료딜레이(self.ctx)


class 종료딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
