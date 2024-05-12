""" trigger/52000200_qd/52000200.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_quest_accept(questId=10003419) # 퀘스트 강제 수락
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[101]) # 바론
        self.create_monster(spawnIds=[102]) # 칼
        self.create_monster(spawnIds=[103]) # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02_02(self.ctx)


class CameraEffect02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000200_QD__52000200__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 여제알현(self.ctx)


class 여제알현(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__1$', illustId='Ereb_normal', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__2$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__3$', illustId='Ereb_normal', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 여제알현_02(self.ctx)


class 여제알현_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004,4005], returnView=False)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__4$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__5$', illustId='Ereb_normal', align='left', duration=4500)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__6$', illustId='Ereb_normal', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11500):
            return 여제알현_03(self.ctx)


class 여제알현_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__7$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__8$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__9$', illustId='Ereb_surprise', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 여제알현_04(self.ctx)


class 여제알현_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 여제알현_05(self.ctx)


class 여제알현_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004782, msg='$52000200_QD__52000200__10$', align='left', illustId='Ruana_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__11$', align='left', illustId='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__12$', align='right', illustId='Karl_normal', duration=4500)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__13$', align='right', illustId='Karl_normal', duration=4500)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__14$', align='left', illustId='Ereb_surprise', duration=3000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__15$', align='right', illustId='Karl_normal', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return 여제알현_06(self.ctx)


class 여제알현_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007,4008], returnView=False)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__16$', align='left', illustId='Ereb_surprise', duration=4500)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__17$', align='right', illustId='Karl_normal', duration=2800)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__18$', align='right', illustId='Karl_normal', duration=4500)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__19$', align='left', illustId='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__20$', align='left', illustId='Ereb_closeEye', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000200_QD__52000200__21$', align='left', illustId='Ereb_closeEye', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__22$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=27800):
            return 음모(self.ctx)


class 음모(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 음모_02(self.ctx)


class 음모_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000200_QD__52000200__23$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 음모_03(self.ctx)


class 음모_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11001975, msg='$52000200_QD__52000200__24$', align='left', duration=4500)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__25$', align='right', illustId='Karl_normal', duration=2800)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__26$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__27$', align='right', illustId='Karl_normal', duration=3000)
        self.add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__28$', align='left', illustId='Radin_normal', duration=4500)
        self.add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__29$', align='left', illustId='Radin_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000200_QD__52000200__30$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11000264, msg='$52000200_QD__52000200__31$', align='left', illustId='Radin_normal', duration=4000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=29000):
            return 이동(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True) # 유저 투명 처리
        self.move_user(mapId=52000190, portalId=5001)


initial_state = start
