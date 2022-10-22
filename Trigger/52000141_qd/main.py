""" trigger/52000141_qd/main.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 침대로이동()


class 침대로이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000141, portalId=10)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라연출_01()


class 카메라연출_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Down_Idle_B', duration=100000)
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라연출_02()


class 카메라연출_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라연출_03()


class 카메라연출_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 루아나와알론대화_01()


class 루아나와알론대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=정리, arg2='exit')
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 루아나와알론대화_02()


class 루아나와알론대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__1$', duration=3000)
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 루아나와알론대화_03()


class 루아나와알론대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__3$', duration=2200)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__4$', duration=2200)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 루아나줌인_01()


class 루아나줌인_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버즈아이뷰_01()


class 버즈아이뷰_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루아나워킹_01()


class 루아나워킹_01(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 알론워킹_01()


class 알론워킹_01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동_01()


class 카메라이동_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다시루아나와알론대화_01()


class 다시루아나와알론대화_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 다시루아나와알론대화_02()


class 다시루아나와알론대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__6$', duration=3000)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6300):
            return 다시루아나와알론대화_03()


class 다시루아나와알론대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__8$', duration=3000)
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6300):
            return 다시루아나와알론대화_04()


class 다시루아나와알론대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__10$', duration=3000)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__11$', duration=2500)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 다시루아나와알론대화_05()


class 다시루아나와알론대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003330, msg='$52000141_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3300):
            return 다시루아나와알론대화_06()


class 다시루아나와알론대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__14$', duration=3000)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__15$', duration=3000)
        add_cinematic_talk(npcId=11003328, msg='$52000141_QD__MAIN__16$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9300):
            return 알론퇴장_01()


class 알론퇴장_01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 루아나퇴장_01()


class 루아나퇴장_01(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루아나퇴장_02()


class 루아나퇴장_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 루아나퇴장_03()


class 루아나퇴장_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100000)
        face_emotion(spawnId=0, emotionName='Point_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 우울한PC_01()


class 우울한PC_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프레데릭등장_01()


class 프레데릭등장_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8009], returnView=False)
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 프레데릭등장_02()


class 프레데릭등장_02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 우울한PC_02()


class 우울한PC_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 프레데릭등장_03()


class 프레데릭등장_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8008], returnView=False)
        face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 프레데릭과대화_01()


class 프레데릭과대화_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3300):
            return 프레데릭과대화_02()


class 프레데릭과대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3300):
            return 프레데릭과대화_03()


class 프레데릭과대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__19$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3300):
            return 프레데릭과대화_04()


class 프레데릭과대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__20$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프레데릭과대화_05()


class 프레데릭과대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__21$', duration=2500)
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__22$', duration=3000)
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__23$', duration=2000)
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__24$', duration=3000)
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__25$', duration=3000)
        add_cinematic_talk(npcId=11003331, msg='$52000141_QD__MAIN__26$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return 프리스트의독백_01()


class 프리스트의독백_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8008,8006], returnView=False)
        face_emotion(spawnId=0, emotionName='Sit_Ground_Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프리스트의독백_02()


class 프리스트의독백_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__27$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 프리스트의독백_03()


class 프리스트의독백_03(state.State):
    def on_enter(self):
        face_emotion(spawnId=0)
        add_cinematic_talk(npcId=0, msg='$52000141_QD__MAIN__28$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 암전_01()


class 정리(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 암전_01()


class 암전_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=2000062, portalId=13)


