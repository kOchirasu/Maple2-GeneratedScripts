""" trigger/52100060_qd/main.xml """
from common import *
import state


class QuestDungeonStart(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[3]):
            return teleport02000487()
        if quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[2]):
            return Ready()
        if quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        select_camera(triggerId=1, enable=True)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[600], visible=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return narration01()


class narration01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100060_QD__MAIN__12$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Camera_Move_01()


class Camera_Move_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC_Show()


class NPC_Show(state.State):
    def on_enter(self):
        set_skip(state=teleport02000487)
        create_monster(spawnIds=[1,2], arg2=False)
        set_npc_rotation(spawnId=1, rotation=180)
        set_npc_rotation(spawnId=2, rotation=180)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC_Change_1()


class NPC_Change_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1,2], arg2=False)
        create_monster(spawnIds=[101,102], arg2=False)
        select_camera_path(pathIds=[2,3], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Talk_1()


class Talk_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        select_camera(triggerId=4, enable=True)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_A')
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__0$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Talk_2()


class Talk_2(state.State):
    def on_enter(self):
        select_camera(triggerId=5, enable=True)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__1$', duration=3000, align='Right')
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__2$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Talk_3()


class Talk_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[10,11,12], returnView=False)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__3$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Talk_4()


class Talk_4(state.State):
    def on_enter(self):
        select_camera(triggerId=4, enable=True)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__4$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Talk_5()


class Talk_5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6,7], returnView=False)
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__5$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Talk_6()


class Talk_6(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[77,78], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__6$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Talk_7()


class Talk_7(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__7$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Talk_8()


class Talk_8(state.State):
    def on_enter(self):
        select_camera(triggerId=44, enable=True)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[200])
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__8$', duration=4000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Talk_9()


class Talk_9(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[13,14,15], returnView=False)
        set_effect(triggerIds=[600], visible=False)
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__9$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Talk_10()


class Talk_10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=200, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11001593, illustId='11001593', msg='$52100060_QD__MAIN__10$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Talk_11()


class Talk_11(state.State):
    def on_enter(self):
        select_camera(triggerId=16, enable=True)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__11$', duration=2000, align='Right')
        select_camera(triggerId=8, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC_Attack_Move()


class NPC_Attack_Move(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.5, endScale=0.3, duration=3, interpolator=1)
        select_camera_path(pathIds=[8,9], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData2')
        move_npc(spawnId=102, patrolName='MS2PatrolData3')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return teleport02000487()


class teleport02000487(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[-1])
        visible_my_pc(isVisible=True)
        move_user(mapId=2000487, portalId=3) # 프론티어 재단 저택 맵 3번 회의실 앞 포탈


