""" trigger/52010030_qd/main.xml """
import common


# 시련의 동굴 : 52010030
# 에바고르 좌절씬
class idle(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[101], animationEffect=True) # 에바고르: 11003391

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에바고르_독백_01(self.ctx)


class 에바고르_독백_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=200000) # 에바고르 좌절모션
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__0$', arg3=False)
        self.set_scene_skip(state=종료, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_독백_02(self.ctx)


class 에바고르_독백_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__1$', arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_독백_02_01(self.ctx)


class 에바고르_독백_02_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__2$', arg3=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_독백_03(self.ctx)


class 에바고르_독백_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__3$', arg3=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_독백_04(self.ctx)


class 에바고르_독백_04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__4$', arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_좌절_01(self.ctx)


class 에바고르_좌절_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4004,4001], returnView=False) # 에바고르 정면
        self.add_cinematic_talk(npcId=11003391, msg='$52010030_QD__MAIN__5$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_좌절_02(self.ctx)


class 에바고르_좌절_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__6$', duration=2000, align='Left')
        self.add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__7$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에바고르_좌절_03(self.ctx)


class 에바고르_좌절_03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=200000) # 에바고르 좌절모션
        self.add_cinematic_talk(npcId=11003391, msg='$52010030_QD__MAIN__8$', duration=2000, align='Left')
        self.select_camera_path(pathIds=[4002], returnView=False) # 에바고르 얼굴 돌림

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 뮤테라피온_등장_01(self.ctx)


class 뮤테라피온_등장_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        # <action name="몬스터를생성한다" arg1="201" arg2="1" />
        self.add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__9$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 뮤테라피온_등장_02(self.ctx)


class 뮤테라피온_등장_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2002,4003], returnView=False) # 뮤테라 피온 줌인
        self.add_cinematic_talk(npcId=11003470, msg='$52010030_QD__MAIN__10$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 잠시뒤(self.ctx)


class 잠시뒤(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__11$', arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 잠시뒤_1(self.ctx)


class 잠시뒤_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000146, portalId=3)


initial_state = idle
