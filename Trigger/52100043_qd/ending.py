""" trigger/52100043_qd/ending.xml """
from common import *
import state


class Ending_Ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[720]):
            return Ending_Camera_1()


class Ending_Camera_1(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        select_camera_path(pathIds=[500,501], returnView=False)
        set_effect(triggerIds=[5000], visible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_mesh(triggerIds=[4993], visible=False)
        set_mesh(triggerIds=[4994], visible=False)
        set_mesh(triggerIds=[4995], visible=False)
        set_mesh(triggerIds=[4996], visible=False)
        set_mesh(triggerIds=[4997], visible=False)
        set_mesh(triggerIds=[4998], visible=False)
        set_mesh(triggerIds=[4999], visible=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[600,601,602], arg2=False)
        set_mesh(triggerIds=[4993], visible=True)
        set_mesh(triggerIds=[4994], visible=True)
        set_mesh(triggerIds=[4995], visible=True)
        set_mesh(triggerIds=[4996], visible=True)
        set_mesh(triggerIds=[4997], visible=True)
        set_mesh(triggerIds=[4998], visible=True)
        set_mesh(triggerIds=[4999], visible=True)
        visible_my_pc(isVisible=True)
        move_npc(spawnId=600, patrolName='MS2PatrolData0')
        move_npc(spawnId=601, patrolName='MS2PatrolData1')
        move_npc(spawnId=602, patrolName='MS2PatrolData2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ending_Talk_1()


class Ending_Talk_1(state.State):
    def on_enter(self):
        set_skip(state=narration01)
        select_camera(triggerId=1000, enable=True)
        set_npc_emotion_sequence(spawnId=602, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001566, illustId='11001566', msg='$52100043_QD__ENDING__0$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Ending_Talk_2()


class Ending_Talk_2(state.State):
    def on_enter(self):
        select_camera(triggerId=1001, enable=True)
        set_npc_emotion_sequence(spawnId=601, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001567, illustId='11001567', msg='$52100043_QD__ENDING__1$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Ending_Talk_3()


class Ending_Talk_3(state.State):
    def on_enter(self):
        select_camera(triggerId=1002, enable=True)
        set_npc_emotion_sequence(spawnId=600, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__2$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Shake_Camera()


class Shake_Camera(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True)
        select_camera_path(pathIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4006,4007,4008,4006,4007,4005,4006,4007,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008], returnView=True)
        add_cinematic_talk(npcId=11001567, illustId='11001567', msg='$52100043_QD__ENDING__3$', duration=2000, align='left')
        destroy_monster(spawnIds=[601,602], arg2=False)
        create_monster(spawnIds=[701,702], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ending_Talk_4()


class Ending_Talk_4(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[701,702], arg2=False)
        destroy_monster(spawnIds=[601,602])
        set_effect(triggerIds=[5000], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        add_cinematic_talk(npcId=11001566, illustId='11001566', msg='$52100043_QD__ENDING__4$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ending_Talk_5()


class Ending_Talk_5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7000,7001], returnView=False)
        set_effect(triggerIds=[5001], visible=True)
        add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__5$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return del6000()


class del6000(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        destroy_monster(spawnIds=[600])
        create_monster(spawnIds=[700], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return Ending_Talk_6()


class Ending_Talk_6(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        select_camera(triggerId=6000, enable=True)
        move_npc(spawnId=700, patrolName='MS2PatrolData4')
        add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100043_QD__ENDING__6$', duration=3000, align='left')
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_time_scale(enable=True, startScale=0.8, endScale=0.03, duration=3, interpolator=1)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5006], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Ending_Talk_7()


class Ending_Talk_7(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return narration01()


class narration01(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[-1])
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__7$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return narration02()


class narration02(state.State):
    def on_enter(self):
        set_skip(state=Map_Warf)
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__8$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return narration03()


class narration03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__9$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return narration04()


class narration04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__10$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return narration05()


class narration05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__11$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return narration06()


class narration06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100043_QD__ENDING__12$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Map_Warf()


class Map_Warf(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[-1])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        move_user(mapId=52010068, portalId=1)


