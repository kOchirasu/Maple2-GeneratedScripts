""" trigger/52000120_qd/01_henesysdefense.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.destroy_monster(spawnIds=[101,102,201,202,203,204,290,210,211,212,213,214,215,220,221,222,223,224,225,240,241,242,243,244,245]) # NPC
        self.destroy_monster(spawnIds=[300,301,302,303,304,305,306,307,308,309,310,401,402,403,404,405,406,407,408,409,410,500,501,502,503,504,505,506,507,508,509,510,601,602,603,604]) # Archer
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,921,922,923,924,925,926,927,928]) # Battle_Mob
        self.destroy_monster(spawnIds=[605,606,607,608,801,802,803,804,805,806,807,808,809,810,811,812,813,814]) # Actor
        self.destroy_monster(spawnIds=[701,702,703,704]) # Cannon
        self.destroy_monster(spawnIds=[710,711,712,713]) # CannonForPC
        self.create_monster(spawnIds=[110,111,112,120,121,122,123,124,125,126,130,131,132,133,134,135,136,140,141,142,143,144,145,146,147,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,185,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,113,114,115,116,117,118], animationEffect=False) # MobActor
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=0, delay=0, scale=0) # GratingDown
        # <action name="메쉬를설정한다" arg1="3110-3112" arg2="0" arg3="0" arg4="0" arg5="0" />   GratingUp 사용 안함
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # BridgeMesh_forTOK
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # BridgeBarrier_Invisible
        self.set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=False)
        self.set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=False) # LiftUp_Bomb
        self.set_local_camera(cameraId=10000, enable=False)
        self.set_local_camera(cameraId=10001, enable=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[5000], visible=False) # DarkCloud
        self.set_effect(triggerIds=[5001], visible=False) # DarkCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[1]):
            return LoadingDelay01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[2]):
            # 맵 튕기고 완료가능 상태일 때 대비 위한 스테이트
            return Quit(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.create_monster(spawnIds=[605,606,607,608], animationEffect=False) # Actor_Training
        self.create_monster(spawnIds=[801,802,803,804,805,806], animationEffect=False) # Actor_Patrol
        self.create_monster(spawnIds=[807,808,809,810,811,812,813,814], animationEffect=False) # Actor_Standing
        self.create_monster(spawnIds=[101,201], animationEffect=False) # Actor_Unique
        self.create_monster(spawnIds=[501,502,507,508], animationEffect=False) # Archer_3rd
        self.create_monster(spawnIds=[401,402,403,404,405,406,407,408,409,410], animationEffect=False) # Archer_2nd
        self.create_monster(spawnIds=[710,711,712,713], animationEffect=False) # CannonForPC
        self.select_camera(triggerId=10, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            # LoadingDelay02
            # 테스트용 임시
            return LoadingDelay02(self.ctx) # CameraChange12


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LeadersTalk_Manovich01(self.ctx)


class LeadersTalk_Manovich01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__0$', duration=5000, align='center', illustId='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        # 씬스킵으로 바로 전투 시작
        # self.set_scene_skip(state=OskhalTalk04Skip, action='exit')
        self.set_scene_skip(state=SetLocalTargetCamera01cskip, action='nextState')
        # self.set_skip(state=LeadersTalk_Manovich01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return LeadersTalk_Manovich01Skip(self.ctx)


class LeadersTalk_Manovich01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # Missing State: State
        # self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return LeadersTalk_Osckal01(self.ctx)


class LeadersTalk_Osckal01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__1$', duration=4000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return LeadersTalk_Osckal01Skip(self.ctx)


class LeadersTalk_Osckal01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera(triggerId=11, enable=True)
        self.add_balloon_talk(spawnId=0, msg='$52000120_QD__01_HENESYSDEFENSE__2$', duration=2000, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return LeadersLookAtPC01(self.ctx)


class LeadersLookAtPC01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LeadersLookAtPC02(self.ctx)


class LeadersLookAtPC02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraChange01(self.ctx)


class CameraChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange02(self.ctx)


class CameraChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=12, enable=True) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange03(self.ctx)


class CameraChange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTalk01(self.ctx)


class PCTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__3$', duration=4000, align='center', illustId='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCTalk01Skip(self.ctx)


class PCTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        # self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ManovichTalk01(self.ctx)


class ManovichTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__4$', duration=5000, align='center', illustId='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ManovichTalk01Skip(self.ctx)


class ManovichTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCTalk02(self.ctx)


class PCTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__5$', duration=4000, align='center', illustId='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCTalk02Skip(self.ctx)


class PCTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ManovichTalk02(self.ctx)


class ManovichTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__6$', duration=4000, align='center', illustId='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ManovichTalk02Skip(self.ctx)


class ManovichTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return OskhalTalk02(self.ctx)


class OskhalTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__7$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return OskhalTalk02Skip(self.ctx)


class OskhalTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_effect(triggerIds=[5000], visible=True) # DarkCloud
        self.set_effect(triggerIds=[5001], visible=True) # DarkCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange05(self.ctx)


class CameraChange05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=13, enable=True) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraChange06(self.ctx)


class CameraChange06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=14, enable=True) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return OskhalTalk03(self.ctx)


class OskhalTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__8$', duration=4000, align='center', illustId='Oskhal_serious')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return OskhalTalk03Skip(self.ctx)


class OskhalTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return OskhalTalk04(self.ctx)


class OskhalTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__9$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return OskhalTalk04Skip(self.ctx)


class OskhalTalk04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CameraChange11(self.ctx)


class CameraChange11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange12(self.ctx)


class CameraChange12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.move_user(mapId=52000120, portalId=10, boxId=9900)
        self.select_camera(triggerId=15, enable=True)
        self.destroy_monster(spawnIds=[101,201]) # Actor_Unique
        self.create_monster(spawnIds=[102,202,210,211,212,213,214,215], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange13(self.ctx)


class CameraChange13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=False, arg3=500, delay=0, scale=2) # GratingDown
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=True)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange14(self.ctx)


class CameraChange14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_off') # Bridge
        self.select_camera(triggerId=16, enable=True)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=210, patrolName='MS2PatrolData_210')
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_211')
        self.move_npc(spawnId=212, patrolName='MS2PatrolData_212')
        self.move_npc(spawnId=213, patrolName='MS2PatrolData_213')
        self.move_npc(spawnId=214, patrolName='MS2PatrolData_214')
        self.move_npc(spawnId=215, patrolName='MS2PatrolData_215')
        self.set_user_value(triggerId=10, key='DefencePhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraChange15(self.ctx)


class CameraChange15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return SetLocalTargetCamera01(self.ctx)


class SetLocalTargetCamera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=False)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, delay=0, scale=2) # GratingDown
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SetLocalTargetCamera02(self.ctx)


class SetLocalTargetCamera01cskip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=10, key='DefencePhase', value=1)
        self.move_user(mapId=52000120, portalId=10, boxId=9900)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=False)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, delay=0, scale=2) # GratingDown
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SetLocalTargetCamera02(self.ctx)


class SetLocalTargetCamera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SetLocalTargetCamera03(self.ctx)


class SetLocalTargetCamera03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(cameraId=10000, enable=True)
        self.set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=True) # LiftUp_Bomb

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetLocalTargetCamera04(self.ctx)


class SetLocalTargetCamera04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.create_monster(spawnIds=[901,902], animationEffect=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BattleOnTheWallGuide01(self.ctx)


class BattleOnTheWallGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[202,210,211,212,213,214,215])
        self.create_monster(spawnIds=[203,220,221,222,223,224,225], animationEffect=False)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__10$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=BattleOnTheWallGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return BattleOnTheWallGuide01Skip(self.ctx)


class BattleOnTheWallGuide01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return BattleOnTheWallGuide02(self.ctx)


class BattleOnTheWallGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_effect(triggerIds=[5000], visible=False) # DarkCloud
        self.set_effect(triggerIds=[5001], visible=False) # DarkCloud
        self.create_monster(spawnIds=[903,904], animationEffect=False) # Battle_Mob
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__11$', duration=4000, align='center', illustId='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=BattleOnTheWallGuide02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return BattleOnTheWallGuide02Skip(self.ctx)


class BattleOnTheWallGuide02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleOnTheWallGuide03(self.ctx)


class BattleOnTheWallGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25101201, textId=25101201) # 가이드 : 자경단의 전투를 지원해주세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return BattleOnTheWallEnd01(self.ctx)


class BattleOnTheWallEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25101201)
        self.set_user_value(triggerId=4, key='NpcDown', value=1)
        self.set_user_value(triggerId=5, key='NpcDown', value=1)
        self.set_user_value(triggerId=6, key='NpcDown', value=1)
        self.set_user_value(triggerId=7, key='NpcDown', value=1)
        self.set_user_value(triggerId=8, key='NpcDown', value=1)
        self.set_user_value(triggerId=9, key='NpcDown', value=1)
        self.create_monster(spawnIds=[905,906], animationEffect=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return BattleOnTheWallEnd02(self.ctx)


class BattleOnTheWallEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[907,908], animationEffect=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return BattleOnTheWallEnd03(self.ctx)


class BattleOnTheWallEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[909,910], animationEffect=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return CallingBackUp01(self.ctx)


class CallingBackUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__12$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        # 씬스킵으로 바로 전투 시작
        self.set_scene_skip(state=PCVolunteer05CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CallingBackUp01Skip(self.ctx)


class CallingBackUp01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCVolunteer01(self.ctx)


class PCVolunteer01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_local_camera(cameraId=10000, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCVolunteer02(self.ctx)


class PCVolunteer02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000120, portalId=20, boxId=9900)
        self.select_camera(triggerId=20, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCVolunteer03(self.ctx)


class PCVolunteer03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCVolunteer04(self.ctx)


class PCVolunteer04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return PCVolunteer05(self.ctx)


class PCVolunteer05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000120_QD__01_HENESYSDEFENSE__13$', duration=4000, align='center', illustId='0')
        # self.set_scene_skip(state=Battle01End01Skip, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCVolunteer05Skip(self.ctx)


class PCVolunteer05Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Battle01Start01(self.ctx)


class PCVolunteer05CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000120, portalId=20, boxId=9900)
        self.set_user_value(triggerId=10, key='DefencePhase', value=2)
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Battle01Start01(self.ctx)


class Battle01Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01Start02(self.ctx)


class Battle01Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], isVisible=False) # LiftUp_Bomb
        self.destroy_monster(spawnIds=[701,702,703,704]) # Cannon
        self.destroy_monster(spawnIds=[710,711,712,713]) # CannonForPC
        self.create_monster(spawnIds=[300,301,302,303,304,305,306,307,308,309,310], animationEffect=False) # Archer_1st
        self.create_monster(spawnIds=[500,503,504,505,506,509,510], animationEffect=False) # Archer_4rd
        self.create_monster(spawnIds=[601,602,603,604], animationEffect=False) # Actor_Artillery
        self.create_monster(spawnIds=[701,702,703,704], animationEffect=False) # Cannon
        self.move_user(mapId=52000120, portalId=30, boxId=9900)
        self.create_monster(spawnIds=[240,241,242,243,244,245], animationEffect=False)
        self.select_camera(triggerId=30, enable=True)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01Start03(self.ctx)


class Battle01Start03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # BridgeBarrier_Invisible
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=False, arg3=500, delay=0, scale=2) # GratingDown
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=True)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01Start04(self.ctx)


class Battle01Start04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_off') # Bridge
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.move_npc(spawnId=240, patrolName='MS2PatrolData_240')
        self.move_npc(spawnId=241, patrolName='MS2PatrolData_241')
        self.move_npc(spawnId=242, patrolName='MS2PatrolData_242')
        self.move_npc(spawnId=243, patrolName='MS2PatrolData_243')
        self.move_npc(spawnId=244, patrolName='MS2PatrolData_244')
        self.move_npc(spawnId=245, patrolName='MS2PatrolData_245')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01Start05(self.ctx)


class Battle01Start05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=31, enable=True)
        self.set_user_value(triggerId=10, key='DefencePhase', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle01Start06(self.ctx)


class Battle01Start06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[4000,4001,4002,4003,4004,4005], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003,4004,4005], visible=False)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105], visible=True, arg3=500, delay=0, scale=2) # GratingDown
        self.set_actor(triggerId=4500, visible=True, initialSequence='Interaction_bridge_A01_on') # Bridge
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # BridgeBarrier_Invisible

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle01Start07(self.ctx)


class Battle01Start07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.change_monster(removeSpawnId=203, addSpawnId=204)
        self.change_monster(removeSpawnId=240, addSpawnId=250)
        self.change_monster(removeSpawnId=241, addSpawnId=251)
        self.change_monster(removeSpawnId=242, addSpawnId=252)
        self.change_monster(removeSpawnId=243, addSpawnId=253)
        self.change_monster(removeSpawnId=244, addSpawnId=254)
        self.change_monster(removeSpawnId=245, addSpawnId=255)
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25101202, textId=25101202) # 가이드 : 남아있는 적군을 소탕하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return Battle01End01(self.ctx)


class Battle01End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25101202)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__14$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=Battle01End01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle01End01Skip(self.ctx)


class Battle01End01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        self.move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        self.move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        self.move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        self.move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        self.move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        self.move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        self.move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        self.move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        self.move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        self.move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        self.move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        self.move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01End02(self.ctx)


class Battle01End02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        # 가이드 : 서둘러 부상당한 자경단원들을 치료해주세요!
        self.show_guide_summary(entityId=25101203, textId=25101203, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle02Start01(self.ctx)


class Battle02Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[911,912], animationEffect=False) # Battle02Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle02Start02(self.ctx)


class Battle02Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        # 가이드 : 자경단원들과 함께 적군을 모두 물리치세요!
        self.show_guide_summary(entityId=25101204, textId=25101204, duration=5000)
        self.create_monster(spawnIds=[913,914], animationEffect=False) # Battle02Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[911,912,913,914]):
            return Battle02End01(self.ctx)


class Battle02End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__15$', duration=5000, align='center', illustId='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=Battle02End01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle02End01Skip(self.ctx)


class Battle02End01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[911,912,913,914]) # Battle02_Mob
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        self.move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        self.move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        self.move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        self.move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        self.move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        self.move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        self.move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        self.move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        self.move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        self.move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        self.move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Battle03Start01(self.ctx)


class Battle03Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[921,922], animationEffect=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle03Start02(self.ctx)


class Battle03Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[923,924], animationEffect=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Battle03Start03(self.ctx)


class Battle03Start03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[925,926], animationEffect=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle03Start04(self.ctx)


class Battle03Start04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[927,928], animationEffect=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[921,922,923,924,925,926,927,928]):
            return Battle03End01(self.ctx)


class Battle03End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[290], animationEffect=False) # Turka
        self.destroy_monster(spawnIds=[921,922,923,924,925,926,927,928]) # Battle03_Mob
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=40, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TurkaWalkIn01(self.ctx)


class TurkaWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=230, patrolName='MS2PatrolData_230')
        self.move_npc(spawnId=231, patrolName='MS2PatrolData_231')
        self.move_npc(spawnId=232, patrolName='MS2PatrolData_232')
        self.move_npc(spawnId=233, patrolName='MS2PatrolData_233')
        self.move_npc(spawnId=234, patrolName='MS2PatrolData_234')
        self.move_npc(spawnId=235, patrolName='MS2PatrolData_235')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=250, patrolName='MS2PatrolData_250')
        self.move_npc(spawnId=251, patrolName='MS2PatrolData_251')
        self.move_npc(spawnId=252, patrolName='MS2PatrolData_252')
        self.move_npc(spawnId=253, patrolName='MS2PatrolData_253')
        self.move_npc(spawnId=254, patrolName='MS2PatrolData_254')
        self.move_npc(spawnId=255, patrolName='MS2PatrolData_255')
        self.set_user_value(triggerId=4, key='BattleEnd', value=1)
        self.set_user_value(triggerId=5, key='BattleEnd', value=1)
        self.set_user_value(triggerId=6, key='BattleEnd', value=1)
        self.set_user_value(triggerId=7, key='BattleEnd', value=1)
        self.set_user_value(triggerId=8, key='BattleEnd', value=1)
        self.set_user_value(triggerId=9, key='BattleEnd', value=1)
        self.move_npc(spawnId=290, patrolName='MS2PatrolData_301')
        self.destroy_monster(spawnIds=[204])
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TurkaWalkIn02(self.ctx)


class TurkaWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TurkaTalk01(self.ctx)


class TurkaTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5000], visible=True) # DarkCloud
        self.set_effect(triggerIds=[5001], visible=True) # DarkCloud
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__16$', duration=5000, align='center', illustId='0')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=ManovichTalk03_CSkip, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TurkaTalk01Skip(self.ctx)


class TurkaTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ChangeView01(self.ctx)


class ChangeView01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ChangeView02(self.ctx)


class ChangeView02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=42, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ChangeView03(self.ctx)


class ChangeView03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return TurkaTalk02(self.ctx)


class TurkaTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__17$', duration=4000, align='center', illustId='Turka_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TurkaTalk02Skip(self.ctx)


class TurkaTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawnId=290, patrolName='MS2PatrolData_302')
        self.destroy_monster(spawnIds=[980,981,982,983,984,985,990,991,992,993,994,995])
        self.create_monster(spawnIds=[960,961,962,963,964,965,970,971,972,973,974,975], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyRetreat01(self.ctx)


class EnemyRetreat01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=43, enable=True) # 퇴각 연출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return EnemyRetreat02(self.ctx)


class EnemyRetreat02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=144, patrolName='MS2PatrolData_2001') # DevilWitch
        # Right Group1
        self.move_npc(spawnId=145, patrolName='MS2PatrolData_2105') # DevilWitch
        self.move_npc(spawnId=146, patrolName='MS2PatrolData_2101') # DevilWitch
        self.move_npc(spawnId=147, patrolName='MS2PatrolData_2003') # DevilWitch
        self.move_npc(spawnId=170, patrolName='MS2PatrolData_2104') # DevilJunior
        self.move_npc(spawnId=172, patrolName='MS2PatrolData_2102') # DevilJunior
        self.move_npc(spawnId=178, patrolName='MS2PatrolData_2002') # DevilJunior
        self.move_npc(spawnId=179, patrolName='MS2PatrolData_2104') # DevilJunior
        self.move_npc(spawnId=180, patrolName='MS2PatrolData_2101') # DevilJunior
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_2103') # DevilHuge
        self.move_npc(spawnId=160, patrolName='MS2PatrolData_2206') # DevilJunior
        # Left Group1
        self.move_npc(spawnId=161, patrolName='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawnId=162, patrolName='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawnId=163, patrolName='MS2PatrolData_2202') # DevilJunior
        self.move_npc(spawnId=164, patrolName='MS2PatrolData_2201') # DevilJunior
        self.move_npc(spawnId=165, patrolName='MS2PatrolData_2205') # DevilJunior
        self.move_npc(spawnId=166, patrolName='MS2PatrolData_2204') # DevilJunior

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return EnemyRetreat03(self.ctx)


class EnemyRetreat03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=171, patrolName='MS2PatrolData_2101') # DevilJunior
        # Right Group2
        self.move_npc(spawnId=174, patrolName='MS2PatrolData_2103') # DevilJunior
        self.move_npc(spawnId=175, patrolName='MS2PatrolData_2101') # DevilJunior
        self.move_npc(spawnId=176, patrolName='MS2PatrolData_2105') # DevilJunior
        self.move_npc(spawnId=177, patrolName='MS2PatrolData_2003') # DevilJunior
        self.move_npc(spawnId=150, patrolName='MS2PatrolData_2104') # DevilHornSpear
        self.move_npc(spawnId=151, patrolName='MS2PatrolData_2101') # DevilHornSpear
        self.move_npc(spawnId=152, patrolName='MS2PatrolData_2103') # DevilHornSpear
        self.move_npc(spawnId=153, patrolName='MS2PatrolData_2104') # DevilHornSpear
        self.move_npc(spawnId=154, patrolName='MS2PatrolData_2102') # DevilHornSpear
        self.move_npc(spawnId=155, patrolName='MS2PatrolData_2105') # DevilHornSpear
        self.move_npc(spawnId=156, patrolName='MS2PatrolData_2101') # DevilHornSpear
        self.move_npc(spawnId=140, patrolName='MS2PatrolData_2206') # DevilWitch
        # Left Group2
        self.move_npc(spawnId=141, patrolName='MS2PatrolData_2203') # DevilWitch
        self.move_npc(spawnId=142, patrolName='MS2PatrolData_2205') # DevilWitch
        self.move_npc(spawnId=143, patrolName='MS2PatrolData_2201') # DevilWitch
        self.move_npc(spawnId=167, patrolName='MS2PatrolData_2202') # DevilJunior
        self.move_npc(spawnId=168, patrolName='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawnId=169, patrolName='MS2PatrolData_2206') # DevilJunior

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return EnemyRetreat04(self.ctx)


class EnemyRetreat04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=191, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        # Right Group3
        self.move_npc(spawnId=192, patrolName='MS2PatrolData_2103') # DevilHornIronMace
        self.move_npc(spawnId=193, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        self.move_npc(spawnId=194, patrolName='MS2PatrolData_2105') # DevilHornIronMace
        self.move_npc(spawnId=195, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawnId=114, patrolName='MS2PatrolData_2204') # DevilHornIronMace
        # Left Group3
        self.move_npc(spawnId=115, patrolName='MS2PatrolData_2205') # DevilHornIronMace
        self.move_npc(spawnId=116, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        self.move_npc(spawnId=117, patrolName='MS2PatrolData_2202') # DevilHornIronMace
        self.move_npc(spawnId=118, patrolName='MS2PatrolData_2206') # DevilHornIronMace
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2203') # DevilHuge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return EnemyRetreat05(self.ctx)


class EnemyRetreat05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2002') # DevilHuge
        # Right Group4
        self.move_npc(spawnId=187, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawnId=188, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawnId=189, patrolName='MS2PatrolData_2101') # DevilHornIronMace
        self.move_npc(spawnId=190, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_2202') # DevilHornSpear
        # Left Group4
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_2201') # DevilHornSpear
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2203') # DevilHornSpear
        self.move_npc(spawnId=123, patrolName='MS2PatrolData_2203') # DevilHornSpear
        self.move_npc(spawnId=124, patrolName='MS2PatrolData_2202') # DevilHornSpear
        self.move_npc(spawnId=125, patrolName='MS2PatrolData_2201') # DevilHornSpear
        self.move_npc(spawnId=126, patrolName='MS2PatrolData_2206') # DevilHornSpear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return EnemyRetreat06(self.ctx)


class EnemyRetreat06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[112,144,145,146,147,170,172,178,179,180]) # Right Group1
        self.destroy_monster(spawnIds=[160,161,162,163,164,165,166]) # Left Group1
        self.move_npc(spawnId=130, patrolName='MS2PatrolData_2101') # DevilHornSpear
        # Right Group5
        self.move_npc(spawnId=131, patrolName='MS2PatrolData_2003') # DevilHornSpear
        self.move_npc(spawnId=132, patrolName='MS2PatrolData_2002') # DevilHornSpear
        self.move_npc(spawnId=133, patrolName='MS2PatrolData_2001') # DevilHornSpear
        self.move_npc(spawnId=134, patrolName='MS2PatrolData_2001') # DevilHornSpear
        self.move_npc(spawnId=135, patrolName='MS2PatrolData_2002') # DevilHornSpear
        self.move_npc(spawnId=136, patrolName='MS2PatrolData_2003') # DevilHornSpear
        self.move_npc(spawnId=184, patrolName='MS2PatrolData_2102') # DevilHornIronMace
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        # Left Group5
        self.move_npc(spawnId=196, patrolName='MS2PatrolData_2201') # DevilHornIronMace
        self.move_npc(spawnId=197, patrolName='MS2PatrolData_2203') # DevilHornIronMace
        self.move_npc(spawnId=198, patrolName='MS2PatrolData_2206') # DevilHornIronMace
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_2205') # DevilHornIronMace

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyRetreat07(self.ctx)


class EnemyRetreat07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[171,174,175,176,177,150,151,152,153,154,155,156]) # Right Group2
        self.destroy_monster(spawnIds=[140,141,142,143,167,168,169]) # Left Group2
        self.move_npc(spawnId=181, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        # Right Group6
        self.move_npc(spawnId=182, patrolName='MS2PatrolData_2002') # DevilHornIronMace
        self.move_npc(spawnId=183, patrolName='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawnId=185, patrolName='MS2PatrolData_2002') # DevilHornIronMace
        self.move_npc(spawnId=186, patrolName='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawnId=960, patrolName='MS2PatrolData_2201') # ShieldBarrierLeft
        # Left Group6
        self.move_npc(spawnId=961, patrolName='MS2PatrolData_2202') # ShieldBarrierLeft
        self.move_npc(spawnId=962, patrolName='MS2PatrolData_2203') # ShieldBarrierLeft
        self.move_npc(spawnId=963, patrolName='MS2PatrolData_2203') # ShieldBarrierLeft
        self.move_npc(spawnId=964, patrolName='MS2PatrolData_2201') # ShieldBarrierLeft
        self.move_npc(spawnId=965, patrolName='MS2PatrolData_2202') # ShieldBarrierLeft
        self.move_npc(spawnId=970, patrolName='MS2PatrolData_2002') # ShieldBarrierRight
        # Right Group7
        self.move_npc(spawnId=971, patrolName='MS2PatrolData_2003') # ShieldBarrierRight
        self.move_npc(spawnId=972, patrolName='MS2PatrolData_2003') # ShieldBarrierRight
        self.move_npc(spawnId=973, patrolName='MS2PatrolData_2002') # ShieldBarrierRight
        self.move_npc(spawnId=974, patrolName='MS2PatrolData_2001') # ShieldBarrierRight
        self.move_npc(spawnId=975, patrolName='MS2PatrolData_2001') # ShieldBarrierRight

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return EnemyRetreat08(self.ctx)


class EnemyRetreat08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[191,192,193,194,195]) # Right Group3
        self.destroy_monster(spawnIds=[114,115,116,117,118,110]) # Left Group3

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return EnemyRetreat09(self.ctx)


class EnemyRetreat09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111,187,188,189,190]) # Right Group4
        self.destroy_monster(spawnIds=[120,121,122,123,124,125,126]) # Left Group4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return EnemyRetreat10(self.ctx)


class EnemyRetreat10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[130,131,132,133,134,135,136,184]) # Right Group5
        self.destroy_monster(spawnIds=[113,196,197,198,199]) # Left Group5

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EnemyRetreat11(self.ctx)


class EnemyRetreat11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[181,182,183,184,185,186]) # Right Group6
        self.destroy_monster(spawnIds=[990,991,992,993,994,995]) # Left Group6
        self.destroy_monster(spawnIds=[980,981,982,983,984,985]) # Right Group7
        self.destroy_monster(spawnIds=[290]) # Turka
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Ending01(self.ctx)


class Ending01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=44, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Ending02(self.ctx)


class Ending02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ManovichTalk03(self.ctx)


class ManovichTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npcId=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__18$', duration=4000, align='center', illustId='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ManovichTalk03Skip(self.ctx)


class ManovichTalk03_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1]) # Turka
        self.select_camera(triggerId=44, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ManovichTalk03Skip(self.ctx)


class ManovichTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_achievement(triggerId=9900, type='trigger', achieve='henesysinvasion')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000072, portalId=1)
        self.set_user_value(triggerId=10, key='DefencePhase', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 스테이트
            return Leave(self.ctx)


class Leave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맵 튕기고 이동 명령 못 받을 상태를 대비한 스테이트
        self.move_user(mapId=2000072, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Leave(self.ctx)


initial_state = Wait
