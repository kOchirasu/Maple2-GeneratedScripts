""" trigger/52000141_qd/main.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 침대로이동(self.ctx)


class 침대로이동(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000141, portalId=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라연출_01(self.ctx)


class 카메라연출_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_B', duration=100000)
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라연출_02(self.ctx)


class 카메라연출_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라연출_03(self.ctx)


class 카메라연출_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 루아나와알론대화_01(self.ctx)


class 루아나와알론대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=정리, action='exit')
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 루아나와알론대화_02(self.ctx)


class 루아나와알론대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__1$', duration=3000)
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__2$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 루아나와알론대화_03(self.ctx)


class 루아나와알론대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__3$', duration=2200)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__4$', duration=2200)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 루아나줌인_01(self.ctx)


class 루아나줌인_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버즈아이뷰_01(self.ctx)


class 버즈아이뷰_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루아나워킹_01(self.ctx)


class 루아나워킹_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 알론워킹_01(self.ctx)


class 알론워킹_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다시루아나와알론대화_01(self.ctx)


class 다시루아나와알론대화_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200):
            return 다시루아나와알론대화_02(self.ctx)


class 다시루아나와알론대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__6$', duration=3000)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__7$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6300):
            return 다시루아나와알론대화_03(self.ctx)


class 다시루아나와알론대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6300):
            return 다시루아나와알론대화_04(self.ctx)


class 다시루아나와알론대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__10$', duration=3000)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__11$', duration=2500)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 다시루아나와알론대화_05(self.ctx)


class 다시루아나와알론대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 다시루아나와알론대화_06(self.ctx)


class 다시루아나와알론대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__14$', duration=3000)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__15$', duration=3000)
        self.add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__16$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9300):
            return 알론퇴장_01(self.ctx)


class 알론퇴장_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 루아나퇴장_01(self.ctx)


class 루아나퇴장_01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루아나퇴장_02(self.ctx)


class 루아나퇴장_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 루아나퇴장_03(self.ctx)


class 루아나퇴장_03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100000)
        self.face_emotion(spawnId=0, emotionName='Point_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 우울한PC_01(self.ctx)


class 우울한PC_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프레데릭등장_01(self.ctx)


class 프레데릭등장_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8009], returnView=False)
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프레데릭등장_02(self.ctx)


class 프레데릭등장_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 우울한PC_02(self.ctx)


class 우울한PC_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 프레데릭등장_03(self.ctx)


class 프레데릭등장_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 프레데릭과대화_01(self.ctx)


class 프레데릭과대화_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 프레데릭과대화_02(self.ctx)


class 프레데릭과대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 프레데릭과대화_03(self.ctx)


class 프레데릭과대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__19$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 프레데릭과대화_04(self.ctx)


class 프레데릭과대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__20$', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프레데릭과대화_05(self.ctx)


class 프레데릭과대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__21$', duration=2500)
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__22$', duration=3000)
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__23$', duration=2000)
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__24$', duration=3000)
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__25$', duration=3000)
        self.add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__26$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=17000):
            return 프리스트의독백_01(self.ctx)


class 프리스트의독백_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8008,8006], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Sit_Ground_Bore_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프리스트의독백_02(self.ctx)


class 프리스트의독백_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__27$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200):
            return 프리스트의독백_03(self.ctx)


class 프리스트의독백_03(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__28$', duration=3000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 암전_01(self.ctx)


class 정리(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 암전_01(self.ctx)


class 암전_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=2000062, portalId=13)


initial_state = 준비
