""" trigger/52000131_qd/52000131_main.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 침대로이동(self.ctx)


class 침대로이동(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000131, portalId=99)
        self.set_cinematic_ui(type=1)
        # <action name="연출UI를설정한다" arg1="3"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=80000)
        self.face_emotion(spawnId=0, emotionName='Think_A')
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 페이드인1_01(self.ctx)


class 페이드인1_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 독백_01(self.ctx)


class 독백_01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000131_QD__52000131_MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동1_01(self.ctx)


class 카메라이동1_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 버튼등장_01(self.ctx)


class 버튼등장_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼등장_02(self.ctx)


class 버튼등장_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 버튼등장_03(self.ctx)


class 버튼등장_03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_01(self.ctx)


class 버튼과대화_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_02(self.ctx)


class 버튼과대화_02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=마무리, action='exit')
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__1$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_03(self.ctx)


class 버튼과대화_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.face_emotion(spawnId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_04(self.ctx)


class 버튼과대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_05(self.ctx)


class 버튼과대화_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_06(self.ctx)


class 버튼과대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__3$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 버튼과대화_07(self.ctx)


class 버튼과대화_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_08(self.ctx)


class 버튼과대화_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_09(self.ctx)


class 버튼과대화_09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_10(self.ctx)


class 버튼과대화_10(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_11(self.ctx)


class 버튼과대화_11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_12(self.ctx)


class 버튼과대화_12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_13(self.ctx)


class 버튼과대화_13(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_14(self.ctx)


class 버튼과대화_14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__7$', duration=4000, align='right')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 버튼과대화_15(self.ctx)


class 버튼과대화_15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버튼과대화_16(self.ctx)


class 버튼과대화_16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__9$', duration=4000, align='right')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 버튼과대화_17(self.ctx)


class 버튼과대화_17(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__10$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 버튼과대화_18(self.ctx)


class 버튼과대화_18(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__11$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__12$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 버튼과대화_19(self.ctx)


class 버튼과대화_19(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__13$', duration=3000, align='right')
        self.add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 버튼과대화_20(self.ctx)


class 버튼과대화_20(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 버튼과대화_21(self.ctx)


class 버튼과대화_21(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__15$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마무리(self.ctx)


class 마무리(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=13)


initial_state = 준비
