""" trigger/52000120_qd/01_henesysdefense.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        destroy_monster(spawnIds=[101,102,201,202,203,204,290,210,211,212,213,214,215,220,221,222,223,224,225,240,241,242,243,244,245]) # NPC
        destroy_monster(spawnIds=[300,301,302,303,304,305,306,307,308,309,310,401,402,403,404,405,406,407,408,409,410,500,501,502,503,504,505,506,507,508,509,510,601,602,603,604]) # Archer
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,921,922,923,924,925,926,927,928]) # Battle_Mob
        destroy_monster(spawnIds=[605,606,607,608,801,802,803,804,805,806,807,808,809,810,811,812,813,814]) # Actor
        destroy_monster(spawnIds=[701,702,703,704]) # Cannon
        destroy_monster(spawnIds=[710,711,712,713]) # CannonForPC
        create_monster(spawnIds=[110,111,112,120,121,122,123,124,125,126,130,131,132,133,134,135,136,140,141,142,143,144,145,146,147,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,185,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,113,114,115,116,117,118], arg2=False) # MobActor
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=0, arg4=0, arg5=0) # GratingDown
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # BridgeMesh_forTOK
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # BridgeBarrier_Invisible
        set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=False)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=False)
        set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=False) # LiftUp_Bomb
        set_local_camera(cameraId=10000, enable=False)
        set_local_camera(cameraId=10001, enable=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_effect(triggerIds=[5000], visible=False) # DarkCloud
        set_effect(triggerIds=[5001], visible=False) # DarkCloud

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[1]):
            return LoadingDelay01()
        if quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[2]):
            return Quit()


class LoadingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        create_monster(spawnIds=[605,606,607,608], arg2=False) # Actor_Training
        create_monster(spawnIds=[801,802,803,804,805,806], arg2=False) # Actor_Patrol
        create_monster(spawnIds=[807,808,809,810,811,812,813,814], arg2=False) # Actor_Standing
        create_monster(spawnIds=[101,201], arg2=False) # Actor_Unique
        create_monster(spawnIds=[501,502,507,508], arg2=False) # Archer_3rd
        create_monster(spawnIds=[401,402,403,404,405,406,407,408,409,410], arg2=False) # Archer_2nd
        create_monster(spawnIds=[710,711,712,713], arg2=False) # CannonForPC
        select_camera(triggerId=10, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LoadingDelay02()


class LoadingDelay02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LeadersTalk_Manovich01()


class LeadersTalk_Manovich01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__0$', duration=5000, align='center', illustId='Manovich_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=SetLocalTargetCamera01cskip, arg2='nextState') # action name="스킵을설정한다" arg1="LeadersTalk_Manovich01Skip"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LeadersTalk_Manovich01Skip()


class LeadersTalk_Manovich01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        remove_cinematic_talk() # action name="스킵을설정한다" arg1=""/

    def on_tick(self) -> state.State:
        if true():
            return LeadersTalk_Osckal01()


class LeadersTalk_Osckal01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__1$', duration=4000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LeadersTalk_Osckal01Skip()


class LeadersTalk_Osckal01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera(triggerId=11, enable=True)
        add_balloon_talk(spawnId=0, msg='$52000120_QD__01_HENESYSDEFENSE__2$', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LeadersLookAtPC01()


class LeadersLookAtPC01(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LeadersLookAtPC02()


class LeadersLookAtPC02(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraChange01()


class CameraChange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange02()


class CameraChange02(state.State):
    def on_enter(self):
        select_camera(triggerId=12, enable=True) # PC 등뒤에서

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange03()


class CameraChange03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTalk01()


class PCTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__3$', duration=4000, align='center', illustId='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCTalk01Skip()


class PCTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk() # action name="스킵을설정한다" arg1=""/

    def on_tick(self) -> state.State:
        if true():
            return ManovichTalk01()


class ManovichTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__4$', duration=5000, align='center', illustId='Manovich_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ManovichTalk01Skip()


class ManovichTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCTalk02()


class PCTalk02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__5$', duration=4000, align='center', illustId='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCTalk02Skip()


class PCTalk02Skip(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return ManovichTalk02()


class ManovichTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__6$', duration=4000, align='center', illustId='Manovich_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ManovichTalk02Skip()


class ManovichTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return OskhalTalk02()


class OskhalTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__7$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return OskhalTalk02Skip()


class OskhalTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_effect(triggerIds=[5000], visible=True) # DarkCloud
        set_effect(triggerIds=[5001], visible=True) # DarkCloud

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange05()


class CameraChange05(state.State):
    def on_enter(self):
        select_camera(triggerId=13, enable=True) # PC 등뒤에서

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraChange06()


class CameraChange06(state.State):
    def on_enter(self):
        select_camera(triggerId=14, enable=True) # PC 등뒤에서

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return OskhalTalk03()


class OskhalTalk03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__8$', duration=4000, align='center', illustId='Oskhal_serious') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return OskhalTalk03Skip()


class OskhalTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return OskhalTalk04()


class OskhalTalk04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__9$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return OskhalTalk04Skip()


class OskhalTalk04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CameraChange11()


class CameraChange11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange12()


class CameraChange12(state.State):
    def on_enter(self):
        set_scene_skip()
        move_user(mapId=52000120, portalId=10, boxId=9900)
        select_camera(triggerId=15, enable=True)
        destroy_monster(spawnIds=[101,201]) # Actor_Unique
        create_monster(spawnIds=[102,202,210,211,212,213,214,215], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange13()


class CameraChange13(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=False, arg3=500, arg4=0, arg5=2) # GratingDown
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=True)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange14()


class CameraChange14(state.State):
    def on_enter(self):
        set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_off') # Bridge
        select_camera(triggerId=16, enable=True)
        move_npc(spawnId=202, patrolName='MS2PatrolData_102')
        move_npc(spawnId=210, patrolName='MS2PatrolData_210')
        move_npc(spawnId=211, patrolName='MS2PatrolData_211')
        move_npc(spawnId=212, patrolName='MS2PatrolData_212')
        move_npc(spawnId=213, patrolName='MS2PatrolData_213')
        move_npc(spawnId=214, patrolName='MS2PatrolData_214')
        move_npc(spawnId=215, patrolName='MS2PatrolData_215')
        set_user_value(triggerId=10, key='DefencePhase', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraChange15()


class CameraChange15(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SetLocalTargetCamera01()


class SetLocalTargetCamera01(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=False)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=False)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, arg4=0, arg5=2) # GratingDown
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SetLocalTargetCamera02()


class SetLocalTargetCamera01cskip(state.State):
    def on_enter(self):
        set_user_value(triggerId=10, key='DefencePhase', value=1)
        move_user(mapId=52000120, portalId=10, boxId=9900)
        create_monster(spawnIds=[102], arg2=False)
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=False)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=False)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, arg4=0, arg5=2) # GratingDown
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SetLocalTargetCamera02()


class SetLocalTargetCamera02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SetLocalTargetCamera03()


class SetLocalTargetCamera03(state.State):
    def on_enter(self):
        set_local_camera(cameraId=10000, enable=True)
        set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=True) # LiftUp_Bomb

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetLocalTargetCamera04()


class SetLocalTargetCamera04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        create_monster(spawnIds=[901,902], arg2=False) # Battle_Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BattleOnTheWallGuide01()


class BattleOnTheWallGuide01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202,210,211,212,213,214,215])
        create_monster(spawnIds=[203,220,221,222,223,224,225], arg2=False)
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__10$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=BattleOnTheWallGuide01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BattleOnTheWallGuide01Skip()


class BattleOnTheWallGuide01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return BattleOnTheWallGuide02()


class BattleOnTheWallGuide02(state.State):
    def on_enter(self):
        set_scene_skip()
        set_effect(triggerIds=[5000], visible=False) # DarkCloud
        set_effect(triggerIds=[5001], visible=False) # DarkCloud
        create_monster(spawnIds=[903,904], arg2=False) # Battle_Mob
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__11$', duration=4000, align='center', illustId='Manovich_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=BattleOnTheWallGuide02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return BattleOnTheWallGuide02Skip()


class BattleOnTheWallGuide02Skip(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleOnTheWallGuide03()


class BattleOnTheWallGuide03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25101201, textId=25101201) # 가이드 : 자경단의 전투를 지원해주세요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BattleOnTheWallEnd01()


class BattleOnTheWallEnd01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25101201)
        set_user_value(triggerId=4, key='NpcDown', value=1)
        set_user_value(triggerId=5, key='NpcDown', value=1)
        set_user_value(triggerId=6, key='NpcDown', value=1)
        set_user_value(triggerId=7, key='NpcDown', value=1)
        set_user_value(triggerId=8, key='NpcDown', value=1)
        set_user_value(triggerId=9, key='NpcDown', value=1)
        create_monster(spawnIds=[905,906], arg2=False) # Battle_Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return BattleOnTheWallEnd02()


class BattleOnTheWallEnd02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[907,908], arg2=False) # Battle_Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return BattleOnTheWallEnd03()


class BattleOnTheWallEnd03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[909,910], arg2=False) # Battle_Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return CallingBackUp01()


class CallingBackUp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__12$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=PCVolunteer05CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CallingBackUp01Skip()


class CallingBackUp01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCVolunteer01()


class PCVolunteer01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_local_camera(cameraId=10000, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCVolunteer02()


class PCVolunteer02(state.State):
    def on_enter(self):
        move_user(mapId=52000120, portalId=20, boxId=9900)
        select_camera(triggerId=20, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCVolunteer03()


class PCVolunteer03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCVolunteer04()


class PCVolunteer04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return PCVolunteer05()


class PCVolunteer05(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__13$', duration=4000, align='center', illustId='0') # action name="SetSceneSkip" arg1="Battle01End01Skip" arg2="exit" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCVolunteer05Skip()


class PCVolunteer05Skip(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return Battle01Start01()


class PCVolunteer05CSkip(state.State):
    def on_enter(self):
        move_user(mapId=52000120, portalId=20, boxId=9900)
        set_user_value(triggerId=10, key='DefencePhase', value=2)
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        remove_cinematic_talk()
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if true():
            return Battle01Start01()


class Battle01Start01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01Start02()


class Battle01Start02(state.State):
    def on_enter(self):
        set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=False) # LiftUp_Bomb
        destroy_monster(spawnIds=[701,702,703,704]) # Cannon
        destroy_monster(spawnIds=[710,711,712,713]) # CannonForPC
        create_monster(spawnIds=[300,301,302,303,304,305,306,307,308,309,310], arg2=False) # Archer_1st
        create_monster(spawnIds=[500,503,504,505,506,509,510], arg2=False) # Archer_4rd
        create_monster(spawnIds=[601,602,603,604], arg2=False) # Actor_Artillery
        create_monster(spawnIds=[701,702,703,704], arg2=False) # Cannon
        move_user(mapId=52000120, portalId=30, boxId=9900)
        create_monster(spawnIds=[240,241,242,243,244,245], arg2=False)
        select_camera(triggerId=30, enable=True)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01Start03()


class Battle01Start03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # BridgeBarrier_Invisible
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=False, arg3=500, arg4=0, arg5=2) # GratingDown
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=True)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01Start04()


class Battle01Start04(state.State):
    def on_enter(self):
        set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_off') # Bridge
        move_user_path(patrolName='MS2PatrolData_1002')
        move_npc(spawnId=240, patrolName='MS2PatrolData_240')
        move_npc(spawnId=241, patrolName='MS2PatrolData_241')
        move_npc(spawnId=242, patrolName='MS2PatrolData_242')
        move_npc(spawnId=243, patrolName='MS2PatrolData_243')
        move_npc(spawnId=244, patrolName='MS2PatrolData_244')
        move_npc(spawnId=245, patrolName='MS2PatrolData_245')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01Start05()


class Battle01Start05(state.State):
    def on_enter(self):
        select_camera(triggerId=31, enable=True)
        set_user_value(triggerId=10, key='DefencePhase', value=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle01Start06()


class Battle01Start06(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enabled=False)
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], arg2=False)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, arg4=0, arg5=2) # GratingDown
        set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # BridgeBarrier_Invisible

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle01Start07()


class Battle01Start07(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        change_monster(removeSpawnId=203, addSpawnId=204)
        change_monster(removeSpawnId=240, addSpawnId=250)
        change_monster(removeSpawnId=241, addSpawnId=251)
        change_monster(removeSpawnId=242, addSpawnId=252)
        change_monster(removeSpawnId=243, addSpawnId=253)
        change_monster(removeSpawnId=244, addSpawnId=254)
        change_monster(removeSpawnId=245, addSpawnId=255)
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25101202, textId=25101202) # 가이드 : 남아있는 적군을 소탕하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return Battle01End01()


class Battle01End01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25101202)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__14$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=Battle01End01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle01End01Skip()


class Battle01End01Skip(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01End02()


class Battle01End02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25101203, textId=25101203, duration=5000) # 가이드 : 서둘러 부상당한 자경단원들을 치료해주세요!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle02Start01()


class Battle02Start01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[911,912], arg2=False) # Battle02Wave

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle02Start02()


class Battle02Start02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25101204, textId=25101204, duration=5000) # 가이드 : 자경단원들과 함께 적군을 모두 물리치세요!
        create_monster(spawnIds=[913,914], arg2=False) # Battle02Wave

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[911,912,913,914]):
            return Battle02End01()


class Battle02End01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__15$', duration=5000, align='center', illustId='Oskhal_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=Battle02End01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle02End01Skip()


class Battle02End01Skip(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        destroy_monster(spawnIds=[911,912,913,914]) # Battle02_Mob
        move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Battle03Start01()


class Battle03Start01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921,922], arg2=False) # Battle03Wave

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle03Start02()


class Battle03Start02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[923,924], arg2=False) # Battle03Wave

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Battle03Start03()


class Battle03Start03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[925,926], arg2=False) # Battle03Wave

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle03Start04()


class Battle03Start04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[927,928], arg2=False) # Battle03Wave

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[921,922,923,924,925,926,927,928]):
            return Battle03End01()


class Battle03End01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[290], arg2=False) # Turka
        destroy_monster(spawnIds=[921,922,923,924,925,926,927,928]) # Battle03_Mob
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=40, enable=True)
        move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TurkaWalkIn01()


class TurkaWalkIn01(state.State):
    def on_enter(self):
        move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        set_user_value(triggerId=4, key='BattleEnd', value=1)
        set_user_value(triggerId=5, key='BattleEnd', value=1)
        set_user_value(triggerId=6, key='BattleEnd', value=1)
        set_user_value(triggerId=7, key='BattleEnd', value=1)
        set_user_value(triggerId=8, key='BattleEnd', value=1)
        set_user_value(triggerId=9, key='BattleEnd', value=1)
        move_npc(spawnId=290, patrolName='MS2PatrolData_301')
        destroy_monster(spawnIds=[204])
        create_monster(spawnIds=[205], arg2=True)
        move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TurkaWalkIn02()


class TurkaWalkIn02(state.State):
    def on_enter(self):
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TurkaTalk01()


class TurkaTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5000], visible=True) # DarkCloud
        set_effect(triggerIds=[5001], visible=True) # DarkCloud
        add_cinematic_talk(npcId=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__16$', duration=5000, align='center', illustId='0') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=ManovichTalk03_CSkip, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TurkaTalk01Skip()


class TurkaTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return ChangeView01()


class ChangeView01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ChangeView02()


class ChangeView02(state.State):
    def on_enter(self):
        select_camera(triggerId=42, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ChangeView03()


class ChangeView03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TurkaTalk02()


class TurkaTalk02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__17$', duration=4000, align='center', illustId='Turka_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TurkaTalk02Skip()


class TurkaTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=290, patrolName='MS2PatrolData_302')
        destroy_monster(spawnIds=[980,981,982,983,984,985,990,991,992,993,994,995])
        create_monster(spawnIds=[960,961,962,963,964,965,970,971,972,973,974,975], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyRetreat01()


class EnemyRetreat01(state.State):
    def on_enter(self):
        select_camera(triggerId=43, enable=True) # 퇴각 연출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EnemyRetreat02()


class EnemyRetreat02(state.State):
    def on_enter(self):
        move_npc(spawnId=144, patrolName='MS2PatrolData_2001') # DevilWitch
        move_npc(spawnId=145, patrolName='MS2PatrolData_2105') # DevilWitch
        move_npc(spawnId=146, patrolName='MS2PatrolData_2101') # DevilWitch
        move_npc(spawnId=147, patrolName='MS2PatrolData_2003') # DevilWitch
        move_npc(spawnId=170, patrolName='MS2PatrolData_2104') # DevilJunior
        move_npc(spawnId=172, patrolName='MS2PatrolData_2102') # DevilJunior
        move_npc(spawnId=178, patrolName='MS2PatrolData_2002') # DevilJunior
        move_npc(spawnId=179, patrolName='MS2PatrolData_2104') # DevilJunior
        move_npc(spawnId=180, patrolName='MS2PatrolData_2101') # DevilJunior
        move_npc(spawnId=112, patrolName='MS2PatrolData_2103') # DevilHuge
        move_npc(spawnId=160, patrolName='MS2PatrolData_2206') # DevilJunior
        move_npc(spawnId=161, patrolName='MS2PatrolData_2203') # DevilJunior
        move_npc(spawnId=162, patrolName='MS2PatrolData_2203') # DevilJunior
        move_npc(spawnId=163, patrolName='MS2PatrolData_2202') # DevilJunior
        move_npc(spawnId=164, patrolName='MS2PatrolData_2201') # DevilJunior
        move_npc(spawnId=165, patrolName='MS2PatrolData_2205') # DevilJunior
        move_npc(spawnId=166, patrolName='MS2PatrolData_2204') # DevilJunior

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnemyRetreat03()


class EnemyRetreat03(state.State):
    def on_enter(self):
        move_npc(spawnId=171, patrolName='MS2PatrolData_2101') # DevilJunior
        move_npc(spawnId=174, patrolName='MS2PatrolData_2103') # DevilJunior
        move_npc(spawnId=175, patrolName='MS2PatrolData_2101') # DevilJunior
        move_npc(spawnId=176, patrolName='MS2PatrolData_2105') # DevilJunior
        move_npc(spawnId=177, patrolName='MS2PatrolData_2003') # DevilJunior
        move_npc(spawnId=150, patrolName='MS2PatrolData_2104') # DevilHornSpear
        move_npc(spawnId=151, patrolName='MS2PatrolData_2101') # DevilHornSpear
        move_npc(spawnId=152, patrolName='MS2PatrolData_2103') # DevilHornSpear
        move_npc(spawnId=153, patrolName='MS2PatrolData_2104') # DevilHornSpear
        move_npc(spawnId=154, patrolName='MS2PatrolData_2102') # DevilHornSpear
        move_npc(spawnId=155, patrolName='MS2PatrolData_2105') # DevilHornSpear
        move_npc(spawnId=156, patrolName='MS2PatrolData_2101') # DevilHornSpear
        move_npc(spawnId=140, patrolName='MS2PatrolData_2206') # DevilWitch
        move_npc(spawnId=141, patrolName='MS2PatrolData_2203') # DevilWitch
        move_npc(spawnId=142, patrolName='MS2PatrolData_2205') # DevilWitch
        move_npc(spawnId=143, patrolName='MS2PatrolData_2201') # DevilWitch
        move_npc(spawnId=167, patrolName='MS2PatrolData_2202') # DevilJunior
        move_npc(spawnId=168, patrolName='MS2PatrolData_2203') # DevilJunior
        move_npc(spawnId=169, patrolName='MS2PatrolData_2206') # DevilJunior

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnemyRetreat04()


class EnemyRetreat04(state.State):
    def on_enter(self):
        move_npc(spawnId=191, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        move_npc(spawnId=192, patrolName='MS2PatrolData_2103') # DevilHornIronMace
        move_npc(spawnId=193, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        move_npc(spawnId=194, patrolName='MS2PatrolData_2105') # DevilHornIronMace
        move_npc(spawnId=195, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        move_npc(spawnId=114, patrolName='MS2PatrolData_2204') # DevilHornIronMace
        move_npc(spawnId=115, patrolName='MS2PatrolData_2205') # DevilHornIronMace
        move_npc(spawnId=116, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        move_npc(spawnId=117, patrolName='MS2PatrolData_2202') # DevilHornIronMace
        move_npc(spawnId=118, patrolName='MS2PatrolData_2206') # DevilHornIronMace
        move_npc(spawnId=110, patrolName='MS2PatrolData_2203') # DevilHuge

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnemyRetreat05()


class EnemyRetreat05(state.State):
    def on_enter(self):
        move_npc(spawnId=111, patrolName='MS2PatrolData_2002') # DevilHuge
        move_npc(spawnId=187, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        move_npc(spawnId=188, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        move_npc(spawnId=189, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        move_npc(spawnId=190, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        move_npc(spawnId=120, patrolName='MS2PatrolData_2202') # DevilHornSpear
        move_npc(spawnId=121, patrolName='MS2PatrolData_2201') # DevilHornSpear
        move_npc(spawnId=122, patrolName='MS2PatrolData_2203') # DevilHornSpear
        move_npc(spawnId=123, patrolName='MS2PatrolData_2203') # DevilHornSpear
        move_npc(spawnId=124, patrolName='MS2PatrolData_2202') # DevilHornSpear
        move_npc(spawnId=125, patrolName='MS2PatrolData_2201') # DevilHornSpear
        move_npc(spawnId=126, patrolName='MS2PatrolData_2206') # DevilHornSpear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnemyRetreat06()


class EnemyRetreat06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[112,144,145,146,147,170,172,178,179,180]) # Right Group1
        destroy_monster(spawnIds=[160,161,162,163,164,165,166]) # Left Group1
        move_npc(spawnId=130, patrolName='MS2PatrolData_2101') # DevilHornSpear
        move_npc(spawnId=131, patrolName='MS2PatrolData_2003') # DevilHornSpear
        move_npc(spawnId=132, patrolName='MS2PatrolData_2002') # DevilHornSpear
        move_npc(spawnId=133, patrolName='MS2PatrolData_2001') # DevilHornSpear
        move_npc(spawnId=134, patrolName='MS2PatrolData_2001') # DevilHornSpear
        move_npc(spawnId=135, patrolName='MS2PatrolData_2002') # DevilHornSpear
        move_npc(spawnId=136, patrolName='MS2PatrolData_2003') # DevilHornSpear
        move_npc(spawnId=184, patrolName='MS2PatrolData_2102') # DevilHornIronMace
        move_npc(spawnId=113, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        move_npc(spawnId=196, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        move_npc(spawnId=197, patrolName='MS2PatrolData_2203') # DevilHornIronMace
        move_npc(spawnId=198, patrolName='MS2PatrolData_2206') # DevilHornIronMace
        move_npc(spawnId=199, patrolName='MS2PatrolData_2205') # DevilHornIronMace

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyRetreat07()


class EnemyRetreat07(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[171,174,175,176,177,150,151,152,153,154,155,156]) # Right Group2
        destroy_monster(spawnIds=[140,141,142,143,167,168,169]) # Left Group2
        move_npc(spawnId=181, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        move_npc(spawnId=182, patrolName='MS2PatrolData_2002') # DevilHornIronMace
        move_npc(spawnId=183, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        move_npc(spawnId=185, patrolName='MS2PatrolData_2002') # DevilHornIronMace
        move_npc(spawnId=186, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        move_npc(spawnId=960, patrolName='MS2PatrolData_2201') # ShieldBarrierLeft
        move_npc(spawnId=961, patrolName='MS2PatrolData_2202') # ShieldBarrierLeft
        move_npc(spawnId=962, patrolName='MS2PatrolData_2203') # ShieldBarrierLeft
        move_npc(spawnId=963, patrolName='MS2PatrolData_2203') # ShieldBarrierLeft
        move_npc(spawnId=964, patrolName='MS2PatrolData_2201') # ShieldBarrierLeft
        move_npc(spawnId=965, patrolName='MS2PatrolData_2202') # ShieldBarrierLeft
        move_npc(spawnId=970, patrolName='MS2PatrolData_2002') # ShieldBarrierRight
        move_npc(spawnId=971, patrolName='MS2PatrolData_2003') # ShieldBarrierRight
        move_npc(spawnId=972, patrolName='MS2PatrolData_2003') # ShieldBarrierRight
        move_npc(spawnId=973, patrolName='MS2PatrolData_2002') # ShieldBarrierRight
        move_npc(spawnId=974, patrolName='MS2PatrolData_2001') # ShieldBarrierRight
        move_npc(spawnId=975, patrolName='MS2PatrolData_2001') # ShieldBarrierRight

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EnemyRetreat08()


class EnemyRetreat08(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[191,192,193,194,195]) # Right Group3
        destroy_monster(spawnIds=[114,115,116,117,118,110]) # Left Group3

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return EnemyRetreat09()


class EnemyRetreat09(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,187,188,189,190]) # Right Group4
        destroy_monster(spawnIds=[120,121,122,123,124,125,126]) # Left Group4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EnemyRetreat10()


class EnemyRetreat10(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[130,131,132,133,134,135,136,184]) # Right Group5
        destroy_monster(spawnIds=[113,196,197,198,199]) # Left Group5

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EnemyRetreat11()


class EnemyRetreat11(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[181,182,183,184,185,186]) # Right Group6
        destroy_monster(spawnIds=[990,991,992,993,994,995]) # Left Group6
        destroy_monster(spawnIds=[980,981,982,983,984,985]) # Right Group7
        destroy_monster(spawnIds=[290]) # Turka
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ending01()


class Ending01(state.State):
    def on_enter(self):
        select_camera(triggerId=44, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Ending02()


class Ending02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ManovichTalk03()


class ManovichTalk03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__18$', duration=4000, align='center', illustId='Manovich_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ManovichTalk03Skip()


class ManovichTalk03_CSkip(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1]) # Turka
        select_camera(triggerId=44, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ManovichTalk03Skip()


class ManovichTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_achievement(triggerId=9900, type='trigger', achieve='henesysinvasion')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000072, portalId=1)
        set_user_value(triggerId=10, key='DefencePhase', value=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Leave()


class Leave(state.State):
    def on_enter(self):
        move_user(mapId=2000072, portalId=1) # 맵 튕기고 이동 명령 못 받을 상태를 대비한 스테이트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Leave()


