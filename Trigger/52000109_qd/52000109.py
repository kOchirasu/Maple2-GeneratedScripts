""" trigger/52000109_qd/52000109.xml """
import common


class Wait01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[200], animationEffect=False) # 아이샤등장
        self.create_monster(spawnIds=[2001], animationEffect=False) # 아이샤등장

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10010]):
            return Wait02(self.ctx)


class Wait02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait03(self.ctx)


class Wait03(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000109_QD__52000109__0$', desc='$52000109_QD__52000109__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=6000, scale=2.5)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.move_user(mapId=52000109, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에델슈타인전경씬01(self.ctx)


class 에델슈타인전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1000], returnView=False)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(spawnId=0, msg='$52000109_QD__52000109__2$', duration=5000, delayTick=1000)
        self.add_balloon_talk(spawnId=200, msg='$52000109_QD__52000109__3$', duration=6000, delayTick=4000)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=15000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬02(self.ctx)


class 에델슈타인전경씬02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__4$', duration=4000, align='right')
        self.set_onetime_effect(id=3000982, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000982.xml')
        self.set_onetime_effect(id=50, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬03(self.ctx)


class 에델슈타인전경씬03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__5$', duration=4000, align='right')
        self.set_onetime_effect(id=60, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬04(self.ctx)


class 에델슈타인전경씬04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__6$', duration=4000, align='right')
        self.set_onetime_effect(id=3000983, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000983.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬05(self.ctx)


class 에델슈타인전경씬05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__7$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬06(self.ctx)


class 에델슈타인전경씬06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__8$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬07(self.ctx)


class 에델슈타인전경씬07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__9$', duration=4000, align='right')
        self.set_onetime_effect(id=3000984, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000984.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬08(self.ctx)


class 에델슈타인전경씬08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__10$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬10(self.ctx)


class 에델슈타인전경씬10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1001], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_Isha')
        self.move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬11(self.ctx)


class 에델슈타인전경씬11(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__11$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬12(self.ctx)


class 에델슈타인전경씬12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__12$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬13(self.ctx)


class 에델슈타인전경씬13(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1002,1003], returnView=False)
        self.add_balloon_talk(spawnId=0, msg='$52000109_QD__52000109__13$', duration=5000, delayTick=1000)
        self.add_balloon_talk(spawnId=200, msg='$52000109_QD__52000109__14$', duration=6000, delayTick=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에델슈타인전경씬14(self.ctx)


class 에델슈타인전경씬14(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트대기01_20002302(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_Isha')
        self.move_user(mapId=52000109, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트대기01_20002302(self.ctx)


class 퀘스트대기01_20002302(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201091, textId=25201091, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002304], questStates=[2]):
            return 라딘대화씬03(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002303], questStates=[3]):
            return 라딘대화씬01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002302], questStates=[3]):
            return 라딘등장씬01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[20002302], questStates=[2]):
            return 라딘등장씬01(self.ctx)


# ########################20002302, 라딘 등장########################
class 라딘등장씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[2002], animationEffect=False) # 라딘등장

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라딘등장씬02(self.ctx)


class 라딘등장씬02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_radin')
        self.select_camera_path(pathIds=[1004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라딘등장씬03(self.ctx)


class 라딘등장씬03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003295, illustId='Radin_normal', msg='$52000109_QD__52000109__15$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 라딘등장씬04(self.ctx)


class 라딘등장씬04(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=200, emotionName='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000109_QD__52000109__16$', desc='$52000109_QD__52000109__17$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 라딘등장씬04_1(self.ctx)


class 라딘등장씬04_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라딘등장씬05(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_radin')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라딘등장씬05(self.ctx)


class 라딘등장씬05(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002303], questStates=[2]):
            return 라딘대화씬01(self.ctx)


# ########################20002302, 라딘 등장########################
class 라딘대화씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[2004,302], animationEffect=False) # 라딘등장
        self.destroy_monster(spawnIds=[2002,200])
        self.move_user(mapId=52000109, portalId=11)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라딘대화씬02(self.ctx)


class 라딘대화씬02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[20002304], questStates=[2]):
            return 라딘대화씬03(self.ctx)


class 라딘대화씬03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=라딘대화씬05, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 라딘대화씬04(self.ctx)


class 라딘대화씬04(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000109_QD__52000109__18$', desc='$52000109_QD__52000109__19$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 라딘대화씬04_1(self.ctx)


class 라딘대화씬04_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라딘대화씬05(self.ctx)


class 라딘대화씬05(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=13)


initial_state = Wait01
