""" trigger/52000192_qd/52000192.xml """
from common import *
import state


class wait_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[6001], visible=False)
        set_effect(triggerIds=[6002], visible=False)
        set_effect(triggerIds=[6003], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_interact_object(triggerIds=[10001453], state=2)
        set_interact_object(triggerIds=[10001454], state=2)
        set_interact_object(triggerIds=[10001455], state=2)
        set_interact_object(triggerIds=[10001456], state=2)
        set_portal(portalId=5003, visible=False, enabled=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003423], questStates=[1]):
            return wait_01_02()
        if not quest_user_detected(boxIds=[2001], questIds=[10003423], questStates=[1]):
            return 이동()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_01_03()


class wait_01_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52000192, portalId=5001)
        select_camera_path(pathIds=[4001], returnView=False)
        create_monster(spawnIds=[101]) # 바론
        create_monster(spawnIds=[102]) # 여제

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불난통로_01()


class 불난통로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 불난통로_02()


class 불난통로_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004785, msg='$52000192_QD__52000192__0$', align='left', illustId='Ereb_surprise', duration=4000)
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 불난통로_03()


class 불난통로_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 불난통로_04()


class 불난통로_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__2$', duration=5000)
        add_cinematic_talk(npcId=11004787, msg='$52000192_QD__52000192__3$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 불끄기준비()


class 불끄기준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 불끄기준비_02()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 불끄기준비_02()


class 불끄기준비_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103]) # 바론
        create_monster(spawnIds=[104]) # 여제
        set_effect(triggerIds=[6001], visible=True) # 여제 지킴
        set_interact_object(triggerIds=[10001453], state=1)
        move_user(mapId=52000192, portalId=5002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불꺼라불꺼()


class 불꺼라불꺼(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000192_QD__52000192__4$', duration=3000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001453], arg2=0):
            return 불꺼라불꺼_02()


class 불꺼라불꺼_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__5$', duration=4000)
        set_effect(triggerIds=[6021], visible=False) # 불끄기
        set_effect(triggerIds=[6005], visible=True)
        set_effect(triggerIds=[6006], visible=True)
        set_effect(triggerIds=[6007], visible=True)
        set_effect(triggerIds=[6008], visible=True)
        create_monster(spawnIds=[201])
        create_monster(spawnIds=[202])
        create_monster(spawnIds=[203])
        create_monster(spawnIds=[204])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불꺼라불꺼_02_02()


class 불꺼라불꺼_02_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004787, msg='$52000192_QD__52000192__6$', illust='Baron_normal', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 불꺼라불꺼_02_01()


class 불꺼라불꺼_02_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204]):
            return 불꺼라불꺼_03()


class 불꺼라불꺼_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__7$', duration=4000)
        set_effect(triggerIds=[6001], visible=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3001')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 불꺼라불꺼_04()


class 불꺼라불꺼_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # 여제 지킴
        set_interact_object(triggerIds=[10001454], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001454], arg2=0):
            return 불꺼라불꺼_05()


class 불꺼라불꺼_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__8$', duration=4000)
        set_effect(triggerIds=[6022], visible=False) # 불끄기
        set_effect(triggerIds=[6009], visible=True)
        set_effect(triggerIds=[6010], visible=True)
        set_effect(triggerIds=[6011], visible=True)
        set_effect(triggerIds=[6012], visible=True)
        create_monster(spawnIds=[205])
        create_monster(spawnIds=[206])
        create_monster(spawnIds=[207])
        create_monster(spawnIds=[208])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[205,206,207,208]):
            return 불꺼라불꺼_06()


class 불꺼라불꺼_06(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__9$', duration=4000)
        set_effect(triggerIds=[6002], visible=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 불꺼라불꺼_07()


class 불꺼라불꺼_07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # 여제 지킴
        set_interact_object(triggerIds=[10001455], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001455], arg2=0):
            return 불꺼라불꺼_08()


class 불꺼라불꺼_08(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__10$', duration=4000)
        set_effect(triggerIds=[6023], visible=False) # 불끄기
        set_effect(triggerIds=[6013], visible=True)
        set_effect(triggerIds=[6014], visible=True)
        set_effect(triggerIds=[6015], visible=True)
        set_effect(triggerIds=[6016], visible=True)
        create_monster(spawnIds=[209])
        create_monster(spawnIds=[210])
        create_monster(spawnIds=[211])
        create_monster(spawnIds=[212])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[209,210,211,212]):
            return 불꺼라불꺼_09()


class 불꺼라불꺼_09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3005')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 불꺼라불꺼_10()


class 불꺼라불꺼_10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6004], visible=True) # 여제 지킴
        set_interact_object(triggerIds=[10001456], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001456], arg2=0):
            return 불꺼라불꺼_11()


class 불꺼라불꺼_11(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000192_QD__52000192__11$', duration=3000)
        set_effect(triggerIds=[6024], visible=False) # 불끄기
        set_effect(triggerIds=[6017], visible=True)
        set_effect(triggerIds=[6018], visible=True)
        set_effect(triggerIds=[6019], visible=True)
        set_effect(triggerIds=[6020], visible=True)
        create_monster(spawnIds=[213])
        create_monster(spawnIds=[214])
        create_monster(spawnIds=[215])
        create_monster(spawnIds=[216])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213,214,215,216]):
            return 불꺼라불꺼_12()


class 불꺼라불꺼_12(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__12$', duration=3000)
        set_effect(triggerIds=[6004], visible=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_3007')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3008')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 다왔다()


class 다왔다(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__13$', duration=3000)
        add_cinematic_talk(npcId=11004785, msg='$52000192_QD__52000192__14$', illustId='Ereb_surprise', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 밖으로()


class 밖으로(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, achieve='EscapePrisonTower')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=5003, visible=True, enabled=True)


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=2000119, portalId=20)


