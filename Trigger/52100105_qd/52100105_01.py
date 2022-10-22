""" trigger/52100105_qd/52100105_01.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50101020], questStates=[2]):
            return wait_03()
        if quest_user_detected(boxIds=[2002], questIds=[50101030], questStates=[3]):
            return 장치가동_04()


class wait_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카_클라디아()


class 투르카_클라디아(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 클라디아
        create_monster(spawnIds=[102], arg2=False) # 투르카
        create_monster(spawnIds=[103], arg2=False) # 검은 군단 병사
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        set_cinematic_ui(type=1)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 투르카_클라디아_02()


class 투르카_클라디아_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카_클라디아_03()


class 투르카_클라디아_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__0$', duration=4000)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__1$', duration=4000)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__2$', duration=4000)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 투르카_클라디아_04()


class 투르카_클라디아_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='left', msg='$52100105_QD__52100105_01__3$', duration=3500)
        add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='left', msg='$52100105_QD__52100105_01__4$', duration=3500)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__5$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 투르카_클라디아_05()


class 투르카_클라디아_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='left', msg='$52100105_QD__52100105_01__6$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 장치가동_01()


class 장치가동_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_rotation(spawnId=102, rotation=270)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='left', msg='$52100105_QD__52100105_01__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 장치가동_01_02()


class 장치가동_01_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 장치가동_01_03()


class 장치가동_01_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 장치가동_02()


class 장치가동_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 장치가동_02_01()


class 장치가동_02_01(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=102, rotation=360)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_loop(spawnId=101, sequenceName='Quest_Attack_A', duration=5000) # 클라디아
        add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='right', msg='$52100105_QD__52100105_01__8$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 장치가동_03()


class 장치가동_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4008], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Quest_Effect_A', duration=12000) # 클라디아
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 장치가동_04()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리()


class 장치가동_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리()


class 정리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        destroy_monster(spawnIds=[105])
        destroy_monster(spawnIds=[106])
        destroy_monster(spawnIds=[107])
        visible_my_pc(isVisible=True)
        move_user(mapId=52100110, portalId=1)


