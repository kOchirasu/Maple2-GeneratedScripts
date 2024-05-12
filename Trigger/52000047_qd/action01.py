""" trigger/52000047_qd/action01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 미션 성공 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # DoorOpen
        self.set_effect(triggerIds=[5101], visible=False) # DoorClose
        self.set_effect(triggerIds=[5200], visible=False) # Dust
        self.set_effect(triggerIds=[5201], visible=False) # Dust
        self.set_effect(triggerIds=[5202], visible=False) # Dust
        self.set_effect(triggerIds=[5203], visible=False) # Dust
        self.set_effect(triggerIds=[5204], visible=False) # Dust
        self.set_effect(triggerIds=[5205], visible=False) # Dust
        self.set_effect(triggerIds=[5206], visible=False) # Dust
        self.set_effect(triggerIds=[5207], visible=False) # Dust
        self.set_effect(triggerIds=[5208], visible=False) # Dust
        self.set_effect(triggerIds=[5209], visible=False) # Dust
        self.set_effect(triggerIds=[5210], visible=False) # Dust
        self.set_effect(triggerIds=[5220], visible=False) # SandFlow
        self.set_effect(triggerIds=[5221], visible=False) # SandFlow
        self.set_effect(triggerIds=[5300], visible=False) # RockFall
        self.set_skill(triggerIds=[7000], enable=False) # PCKnockBack
        self.set_skill(triggerIds=[7001], enable=False) # PCKnockBack
        self.set_skill(triggerIds=[7002], enable=False) # CubeBreak
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021], visible=False, arg3=0, delay=0, scale=0) # BrokenCube  Visible OFF
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # Barrier Visible OFF
        self.set_user_value(key='VasaraTired', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[2]):
            # 인내의 한계 퀘스트 수락한 상태
            return Quit(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[1]):
            # 인내의 한계 퀘스트 수락한 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[3]):
            # 꺾을 수 없는 의지 퀘스트 완료 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[2]):
            # 꺾을 수 없는 의지 퀘스트 완료 가능 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[1]):
            # 꺾을 수 없는 의지 퀘스트 수락한 상태
            return LoadingDelay02(self.ctx)
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


# 첫 번째 퀘스트 완료 가능, 완료 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,201,530,531,532,533,534,535,536,537,538,539], animationEffect=False)
        self.move_user(mapId=52000047, portalId=3, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NextQuestStart01(self.ctx)


# 최초 입장
class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=500, enable=True)
        self.create_monster(spawnIds=[500,501,502,503,504,505,506,507,508,509], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCWalkIn01(self.ctx)


class PCWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=501, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCWalkIn02(self.ctx)


class PCWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=500, sequenceName='Talk_A', duration=6000)
        self.set_npc_emotion_sequence(spawnId=507, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCWalkIn03(self.ctx)


class PCWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=502, sequenceName='Talk_A', duration=6000)
        self.set_npc_emotion_loop(spawnId=509, sequenceName='Talk_A', duration=6000)
        self.set_npc_emotion_sequence(spawnId=503, sequenceName='Bore_A')
        self.select_camera(triggerId=502, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice01(self.ctx)


class NPCNotice01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=509, patrolName='MS2PatrolData_509')
        self.set_conversation(type=1, spawnId=509, script='$52000047_QD__ACTION01__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice02(self.ctx)


class NPCNotice02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_500')
        self.move_npc(spawnId=507, patrolName='MS2PatrolData_507')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice03(self.ctx)


class NPCNotice03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=504, patrolName='MS2PatrolData_504')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice04(self.ctx)


class NPCNotice04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=508, patrolName='MS2PatrolData_508')
        self.set_conversation(type=1, spawnId=504, script='$52000047_QD__ACTION01__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPCNotice05(self.ctx)


class NPCNotice05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_501')
        self.move_npc(spawnId=506, patrolName='MS2PatrolData_506')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice06(self.ctx)


class NPCNotice06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=502, patrolName='MS2PatrolData_502')
        self.move_npc(spawnId=505, patrolName='MS2PatrolData_505')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NPCNotice07(self.ctx)


class NPCNotice07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=503, patrolName='MS2PatrolData_503')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MafiaReadyToFight01(self.ctx)


class MafiaReadyToFight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=505, script='$52000047_QD__ACTION01__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MafiaReadyToFight02(self.ctx)


class MafiaReadyToFight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=503, enable=True)
        self.set_pc_emotion_sequence(sequenceNames=['Striker_Bore_A'])
        self.set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__3$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MafiaReadyToFight03(self.ctx)


class MafiaReadyToFight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=504, enable=True)
        self.change_monster(removeSpawnId=500, addSpawnId=900)
        self.change_monster(removeSpawnId=501, addSpawnId=901)
        self.change_monster(removeSpawnId=502, addSpawnId=902)
        self.change_monster(removeSpawnId=503, addSpawnId=903)
        self.change_monster(removeSpawnId=504, addSpawnId=904)
        self.change_monster(removeSpawnId=505, addSpawnId=905)
        self.change_monster(removeSpawnId=506, addSpawnId=906)
        self.change_monster(removeSpawnId=507, addSpawnId=907)
        self.change_monster(removeSpawnId=508, addSpawnId=908)
        self.change_monster(removeSpawnId=509, addSpawnId=909)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return MafiaReadyToFight04(self.ctx)


class MafiaReadyToFight04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=504, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MafiaFightStart01(self.ctx)


class MafiaFightStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=25200471, textId=25200471) # 가이드 : 흑성회 조직원들 모두 쓰러트리기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900,901,902,903,904,905,906,907,908,909]):
            return MafiaFightEnd01(self.ctx)


class MafiaFightEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True) # 미션 성공 사운드 이펙트
        self.hide_guide_summary(entityId=25200471)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeihongWalkIn01(self.ctx)


# 웨이홍 바사라첸 입장
class WeihongWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5100], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeihongWalkIn02(self.ctx)


class WeihongWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[100], animationEffect=False) # 웨이 홍
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeihongWalkIn03(self.ctx)


class WeihongWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[200], animationEffect=False) # 바사라 첸
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        self.set_effect(triggerIds=[5101], visible=True) # DoorClose
        self.move_user(mapId=52000047, portalId=2, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeihongTalk01(self.ctx)


class WeihongTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)
        self.set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__4$', arg4=4) # 웨이 홍
        self.set_skip(state=WeihongTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return WeihongTalk01Skip(self.ctx)


class WeihongTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_user_value(triggerId=500, key='NpcRemove', value=1)
        self.set_user_value(triggerId=501, key='NpcRemove', value=1)
        self.set_user_value(triggerId=502, key='NpcRemove', value=1)
        self.set_user_value(triggerId=503, key='NpcRemove', value=1)
        self.set_user_value(triggerId=504, key='NpcRemove', value=1)
        self.set_user_value(triggerId=505, key='NpcRemove', value=1)
        self.set_user_value(triggerId=506, key='NpcRemove', value=1)
        self.set_user_value(triggerId=507, key='NpcRemove', value=1)
        self.set_user_value(triggerId=508, key='NpcRemove', value=1)
        self.set_user_value(triggerId=509, key='NpcRemove', value=1)
        self.create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeihongTalk02(self.ctx)


class WeihongTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__5$', arg4=4) # 웨이 홍
        self.set_skip(state=WeihongTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return WeihongTalk02Skip(self.ctx)


class WeihongTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetAgainWeihong01(self.ctx)


class MeetAgainWeihong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=520, patrolName='MS2PatrolData_520')
        self.move_npc(spawnId=521, patrolName='MS2PatrolData_521')
        self.move_npc(spawnId=522, patrolName='MS2PatrolData_522')
        self.move_npc(spawnId=523, patrolName='MS2PatrolData_523')
        self.move_npc(spawnId=524, patrolName='MS2PatrolData_524')
        self.move_npc(spawnId=525, patrolName='MS2PatrolData_525')
        self.move_npc(spawnId=526, patrolName='MS2PatrolData_526')
        self.move_npc(spawnId=527, patrolName='MS2PatrolData_527')
        self.move_npc(spawnId=528, patrolName='MS2PatrolData_528')
        self.move_npc(spawnId=529, patrolName='MS2PatrolData_529')
        self.set_conversation(type=1, spawnId=520, script='$52000047_QD__ACTION01__6$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetAgainWeihong02(self.ctx)


class MeetAgainWeihong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=527, script='$52000047_QD__ACTION01__7$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=529, script='$52000047_QD__ACTION01__8$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MeetAgainWeihong03(self.ctx)


class MeetAgainWeihong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__9$', arg4=4, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MeetAgainWeihong04(self.ctx)


class MeetAgainWeihong04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return MeetAgainWeihong05(self.ctx)


class MeetAgainWeihong05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=602, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetAgainWeihong06(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[100,200,520,521,522,523,524,525,526,527,528,529])
        self.create_monster(spawnIds=[101,201,530,531,532,533,534,535,536,537,538,539], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class MeetAgainWeihong06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9900, type='trigger', achieve='MeetAgainWeihong')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NextQuestStart01(self.ctx)


# 다음 퀘스트 시작
class NextQuestStart01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[1]):
            # 인내의 한계 퀘스트 수락한 상태
            return PositionArrange01(self.ctx)


class PositionArrange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PositionArrange02(self.ctx)


class PositionArrange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=700, enable=True)
        self.move_user(mapId=52000047, portalId=3, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PositionArrange03(self.ctx)


class PositionArrange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeihongStepBack01(self.ctx)


class WeihongStepBack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=101, script='$52000047_QD__ACTION01__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return WeihongStepBack02(self.ctx)


class WeihongStepBack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.set_conversation(type=1, spawnId=101, script='$52000047_QD__ACTION01__11$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PCTryToAttackWeihong01(self.ctx)


class PCTryToAttackWeihong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=710, enable=True)
        self.set_pc_emotion_loop(sequenceName='Knuckle_Attack_Idle_A', duration=1734)
        self.set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__12$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCTryToAttackWeihong02(self.ctx)


class PCTryToAttackWeihong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=711, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return PCTryToAttackWeihong03(self.ctx)


class PCTryToAttackWeihong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return VasaraPush01(self.ctx)


class VasaraPush01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=201, script='$52000047_QD__ACTION01__20$', arg4=1, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraPush02(self.ctx)


class VasaraPush02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_H')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraPush03(self.ctx)


class VasaraPush03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[7000], enable=True) # PCKnockBack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return VasaraPush04(self.ctx)


class VasaraPush04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SceneChange01(self.ctx)


class SceneChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SceneChange02(self.ctx)


class SceneChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=720, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SceneChange03(self.ctx)


class SceneChange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return VasaraTalk01(self.ctx)


class VasaraTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__13$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return VasaraTalk02(self.ctx)


class VasaraTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=201, script='$52000047_QD__ACTION01__14$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return VasaraTalk03(self.ctx)


class VasaraTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__15$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return VasaraBattle01(self.ctx)


class VasaraBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=720, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return VasaraBattle02(self.ctx)


class VasaraBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=25200472, textId=25200472) # 가이드 : 바사라 첸 쓰러트리기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='VasaraTired', value=1):
            return VasaraBattle03(self.ctx)


class VasaraBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True) # 미션 성공 사운드 이펙트
        self.hide_guide_summary(entityId=25200472)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return VasaraTired01(self.ctx)


class VasaraTired01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraTired02(self.ctx)


class VasaraTired02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=720, enable=True)
        self.move_user(mapId=52000047, portalId=4, boxId=9900)
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraTired03(self.ctx)


class VasaraTired03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Down_Idle_A', duration=9000)
        self.set_pc_emotion_loop(sequenceName='Knuckle_Attack_Idle_A', duration=9537)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraTired04(self.ctx)


class VasaraTired04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=600):
            return VasaraTired05(self.ctx)


class VasaraTired05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=203, script='$52000047_QD__ACTION01__21$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return WeihongOrder01(self.ctx)


class WeihongOrder01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=730, enable=True)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeihongOrder02(self.ctx)


class WeihongOrder02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__16$', arg4=5) # 웨이 홍
        self.set_skip(state=WeihongOrder02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return WeihongOrder02Skip(self.ctx)


class WeihongOrder02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MafiaMove01(self.ctx)


class MafiaMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=731, enable=True)
        self.move_npc(spawnId=530, patrolName='MS2PatrolData_530')
        self.move_npc(spawnId=535, patrolName='MS2PatrolData_535')
        self.move_npc(spawnId=534, patrolName='MS2PatrolData_534')
        self.move_npc(spawnId=537, patrolName='MS2PatrolData_537')
        self.move_npc(spawnId=532, patrolName='MS2PatrolData_532')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return MafiaMove02(self.ctx)


class MafiaMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=531, patrolName='MS2PatrolData_531')
        self.move_npc(spawnId=533, patrolName='MS2PatrolData_533')
        self.move_npc(spawnId=536, patrolName='MS2PatrolData_536')
        self.move_npc(spawnId=538, patrolName='MS2PatrolData_538')
        self.move_npc(spawnId=539, patrolName='MS2PatrolData_539')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraTalk10(self.ctx)


class VasaraTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_204')
        self.set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__17$', arg4=5) # 바사라 첸
        self.set_skip(state=VasaraTalk10Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return VasaraTalk10Skip(self.ctx)


class VasaraTalk10Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return VasaraPushAgain01(self.ctx)


class VasaraPushAgain01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraPushAgain02(self.ctx)


class VasaraPushAgain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_02_G,Attack_03_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return VasaraPushAgain03(self.ctx)


class VasaraPushAgain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[7001], enable=True) # PCKnockBack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return VasaraPushAgain04(self.ctx)


class VasaraPushAgain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=6000)
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_I,Attack_Idle_A,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return VasaraLastAttack01(self.ctx)


class VasaraLastAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[7002], enable=True) # CubeBreak
        self.set_effect(triggerIds=[5300], visible=True) # RockFall

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return VasaraLastAttack02(self.ctx)


class VasaraLastAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5220], visible=True) # SandFlow
        self.set_random_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021], visible=True, meshCount=22, arg4=50, delay=80) # Rock Visible  ON
        self.set_effect(triggerIds=[5200], visible=True) # Dust
        self.set_effect(triggerIds=[5201], visible=True) # Dust
        self.set_effect(triggerIds=[5202], visible=True) # Dust
        self.set_effect(triggerIds=[5203], visible=True) # Dust
        self.set_effect(triggerIds=[5204], visible=True) # Dust
        self.set_effect(triggerIds=[5205], visible=True) # Dust
        self.set_effect(triggerIds=[5206], visible=True) # Dust
        self.set_effect(triggerIds=[5207], visible=True) # Dust
        self.set_effect(triggerIds=[5208], visible=True) # Dust
        self.set_effect(triggerIds=[5209], visible=True) # Dust
        self.set_effect(triggerIds=[5210], visible=True) # Dust

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return VasaraLastAttack03(self.ctx)


class VasaraLastAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5221], visible=True) # SandFlow
        self.select_camera(triggerId=731, enable=True)
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Barrier Visible OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return VasaraTalk20(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(triggerIds=[5220], visible=True)
        # SandFlow


class VasaraTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__18$', arg4=5) # 바사라 첸
        self.set_skip(state=VasaraTalk20Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return VasaraTalk20Skip(self.ctx)


class VasaraTalk20Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return VasaraTalk21(self.ctx)


class VasaraTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__19$', arg4=5) # 바사라 첸
        self.set_skip(state=VasaraTalk21Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return VasaraTalk21Skip(self.ctx)


class VasaraTalk21Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=731, enable=False)
        self.set_effect(triggerIds=[5221], visible=True) # SandFlow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FriendOfVasara01(self.ctx)


class FriendOfVasara01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5220], visible=True) # SandFlow
        self.set_achievement(triggerId=9900, type='trigger', achieve='FriendOfVasara')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5221], visible=True) # SandFlow
        self.move_user(mapId=2000138, portalId=105, boxId=9900)


initial_state = Wait
