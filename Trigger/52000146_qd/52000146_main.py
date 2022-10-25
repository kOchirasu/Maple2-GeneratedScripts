""" trigger/52000146_qd/52000146_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 한번더대기(self.ctx)


class 한번더대기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카메라이동_02(self.ctx)


class 카메라이동_02(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000146_QD__52000146_MAIN__0$', desc='$52000146_QD__52000146_MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카메라리셋_01(self.ctx)


class 카메라리셋_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라리셋_02(self.ctx)


class 카메라리셋_02(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라리셋_03(self.ctx)


class 카메라리셋_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 걸으며대화_01(self.ctx)


class 걸으며대화_01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 걸으며대화_02(self.ctx)


class 걸으며대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__2$', duration=3000, illustId='Hastur_normal', align='left')
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__3$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 걸으며대화_03(self.ctx)


class 걸으며대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 걸으며대화_04(self.ctx)


class 걸으며대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__5$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 걸으며대화_05(self.ctx)


class 걸으며대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__6$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 걸으며대화_06(self.ctx)


class 걸으며대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__7$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 멈춰서대화_01(self.ctx)


class 멈춰서대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 멈춰서대화_02(self.ctx)


class 멈춰서대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__9$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투_01(self.ctx)


class 전투_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[102,103,104,105,106])
        self.create_monster(spawnIds=[107,108,109,110,111], animationEffect=True)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.show_guide_summary(entityId=25201461, textId=25201461)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[107,108,109,110,111]):
            return 전투_02(self.ctx)


class 전투_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[107,108,109,110,111], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[107,108,109,110,111]):
            return 전투종료_01(self.ctx)


class 전투종료_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201461)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투종료_02(self.ctx)


class 전투종료_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000146, portalId=99)
        self.destroy_monster(spawnIds=[112])
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투종료_03(self.ctx)


class 전투종료_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투후대화_01(self.ctx)


class 전투후대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=스킵도착_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__10$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_02(self.ctx)


class 전투후대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__11$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_03(self.ctx)


class 전투후대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__12$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_04(self.ctx)


class 전투후대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__13$', duration=3500, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_05(self.ctx)


class 전투후대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__14$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_06(self.ctx)


class 전투후대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__15$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_07(self.ctx)


class 전투후대화_07(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_08(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[113])


class 전투후대화_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__16$', duration=5000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전투후대화_09(self.ctx)


class 스킵도착_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[113])
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스킵도착_02(self.ctx)


class 스킵도착_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투후대화_09(self.ctx)


class 전투후대화_09(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000146_QD__52000146_MAIN__17$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투후대화_10(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 전투후대화_10(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투후대화_11(self.ctx)


class 전투후대화_11(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=하스터찾기_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__18$', duration=4000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__19$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7500):
            return 하스터찾기_01(self.ctx)


class 하스터찾기_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201462, textId=25201462)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201462)
        self.move_user(mapId=52000147, portalId=1)


initial_state = 준비
