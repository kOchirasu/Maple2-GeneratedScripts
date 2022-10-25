""" trigger/52000148_qd/52000148_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 잠시대기_01(self.ctx)


class 잠시대기_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_user(mapId=52000148, portalId=99)
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 잠시대기_03(self.ctx)


class 잠시대기_03(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=130000)
        self.face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 시작_01(self.ctx)


class 시작_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__0$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시작_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 시작_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작_03(self.ctx)


class 시작_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스카와대화_01(self.ctx)


class 오스카와대화_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__1$', duration=2500, align='right')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        self.set_scene_skip(state=오스카퇴장_02, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카와대화_02(self.ctx)


class 오스카와대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카와대화_03(self.ctx)


class 오스카와대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__3$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카와대화_04(self.ctx)


class 오스카와대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__4$', duration=3000, align='left')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스카와대화_05(self.ctx)


class 오스카와대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__5$', duration=4000, align='left')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 오스카와대화_06(self.ctx)


class 오스카와대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카와대화_07(self.ctx)


class 오스카와대화_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__7$', duration=3000, align='left')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__8$', duration=4000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 오스카와대화_08(self.ctx)


class 오스카와대화_08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스카와대화_09(self.ctx)


class 오스카와대화_09(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__9$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__10$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 오스카와대화_10(self.ctx)


class 오스카와대화_10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오스카와대화_11(self.ctx)


class 오스카와대화_11(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__11$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스카와대화_12(self.ctx)


class 오스카와대화_12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__12$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__13$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 오스카와대화_13(self.ctx)


class 오스카와대화_13(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__14$', duration=3500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__15$', duration=3500, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__16$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=16613):
            return 오스카와대화_14(self.ctx)


class 오스카와대화_14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__17$', duration=2500, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__18$', duration=4000, align='right')
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__19$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 오스카와대화_15(self.ctx)


class 오스카와대화_15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__20$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카와대화_16(self.ctx)


class 오스카와대화_16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__21$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스카와대화_17(self.ctx)


class 오스카와대화_17(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__22$', duration=3000, illustId='Oskhal_normal', align='left')
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__23$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 오스카와대화_18(self.ctx)


class 오스카와대화_18(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__24$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 오스카와대화_19(self.ctx)


class 오스카와대화_19(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__25$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 오스카퇴장_01(self.ctx)


class 오스카퇴장_01(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 오스카퇴장_02(self.ctx)


class 오스카퇴장_02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 독백_01(self.ctx)


class 독백_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 독백_02(self.ctx)


class 독백_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__26$', duration=2500, align='right')
        self.set_scene_skip(state=마무리_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 독백_03(self.ctx)


class 독백_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 독백_04(self.ctx)


class 독백_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__27$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 독백_05(self.ctx)


class 독백_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 독백_06(self.ctx)


class 독백_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__28$', duration=3500, align='right')
        self.face_emotion(spawnId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마무리_01(self.ctx)


class 마무리_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마무리_02(self.ctx)


class 마무리_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__29$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=13)


initial_state = 준비
