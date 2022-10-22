""" trigger/52000047_qd/action01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 미션 성공 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # DoorOpen
        set_effect(triggerIds=[5101], visible=False) # DoorClose
        set_effect(triggerIds=[5200], visible=False) # Dust
        set_effect(triggerIds=[5201], visible=False) # Dust
        set_effect(triggerIds=[5202], visible=False) # Dust
        set_effect(triggerIds=[5203], visible=False) # Dust
        set_effect(triggerIds=[5204], visible=False) # Dust
        set_effect(triggerIds=[5205], visible=False) # Dust
        set_effect(triggerIds=[5206], visible=False) # Dust
        set_effect(triggerIds=[5207], visible=False) # Dust
        set_effect(triggerIds=[5208], visible=False) # Dust
        set_effect(triggerIds=[5209], visible=False) # Dust
        set_effect(triggerIds=[5210], visible=False) # Dust
        set_effect(triggerIds=[5220], visible=False) # SandFlow
        set_effect(triggerIds=[5221], visible=False) # SandFlow
        set_effect(triggerIds=[5300], visible=False) # RockFall
        set_skill(triggerIds=[7000], isEnable=False) # PCKnockBack
        set_skill(triggerIds=[7001], isEnable=False) # PCKnockBack
        set_skill(triggerIds=[7002], isEnable=False) # CubeBreak
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021], visible=False, arg3=0, arg4=0, arg5=0) # BrokenCube  Visible OFF
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0) # Barrier Visible OFF
        set_user_value(key='VasaraTired', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[2]):
            return Quit()
        if quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[1]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[3]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[2]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9900], questIds=[10003043], questStates=[1]):
            return LoadingDelay02()
        if wait_tick(waitTick=5000):
            return Quit()


#  첫 번째 퀘스트 완료 가능, 완료 상태 
class QuestOnGoing01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201,530,531,532,533,534,535,536,537,538,539], arg2=False)
        move_user(mapId=52000047, portalId=3, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestOnGoing02()


class QuestOnGoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NextQuestStart01()


#  최초 입장 
class LoadingDelay02(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        create_monster(spawnIds=[500,501,502,503,504,505,506,507,508,509], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCWalkIn01()


class PCWalkIn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=501, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCWalkIn02()


class PCWalkIn02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=500, sequenceName='Talk_A', duration=6000)
        set_npc_emotion_sequence(spawnId=507, sequenceName='Bore_A')
        set_npc_emotion_sequence(spawnId=501, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCWalkIn03()


class PCWalkIn03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=502, sequenceName='Talk_A', duration=6000)
        set_npc_emotion_loop(spawnId=509, sequenceName='Talk_A', duration=6000)
        set_npc_emotion_sequence(spawnId=503, sequenceName='Bore_A')
        select_camera(triggerId=502, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice01()


class NPCNotice01(state.State):
    def on_enter(self):
        move_npc(spawnId=509, patrolName='MS2PatrolData_509')
        set_conversation(type=1, spawnId=509, script='$52000047_QD__ACTION01__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice02()


class NPCNotice02(state.State):
    def on_enter(self):
        move_npc(spawnId=500, patrolName='MS2PatrolData_500')
        move_npc(spawnId=507, patrolName='MS2PatrolData_507')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice03()


class NPCNotice03(state.State):
    def on_enter(self):
        move_npc(spawnId=504, patrolName='MS2PatrolData_504')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice04()


class NPCNotice04(state.State):
    def on_enter(self):
        move_npc(spawnId=508, patrolName='MS2PatrolData_508')
        set_conversation(type=1, spawnId=504, script='$52000047_QD__ACTION01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPCNotice05()


class NPCNotice05(state.State):
    def on_enter(self):
        move_npc(spawnId=501, patrolName='MS2PatrolData_501')
        move_npc(spawnId=506, patrolName='MS2PatrolData_506')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice06()


class NPCNotice06(state.State):
    def on_enter(self):
        move_npc(spawnId=502, patrolName='MS2PatrolData_502')
        move_npc(spawnId=505, patrolName='MS2PatrolData_505')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPCNotice07()


class NPCNotice07(state.State):
    def on_enter(self):
        move_npc(spawnId=503, patrolName='MS2PatrolData_503')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MafiaReadyToFight01()


class MafiaReadyToFight01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=505, script='$52000047_QD__ACTION01__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MafiaReadyToFight02()


class MafiaReadyToFight02(state.State):
    def on_enter(self):
        select_camera(triggerId=503, enable=True)
        set_pc_emotion_sequence(sequenceNames=['Striker_Bore_A'])
        set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__3$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MafiaReadyToFight03()


class MafiaReadyToFight03(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=True)
        change_monster(removeSpawnId=500, addSpawnId=900)
        change_monster(removeSpawnId=501, addSpawnId=901)
        change_monster(removeSpawnId=502, addSpawnId=902)
        change_monster(removeSpawnId=503, addSpawnId=903)
        change_monster(removeSpawnId=504, addSpawnId=904)
        change_monster(removeSpawnId=505, addSpawnId=905)
        change_monster(removeSpawnId=506, addSpawnId=906)
        change_monster(removeSpawnId=507, addSpawnId=907)
        change_monster(removeSpawnId=508, addSpawnId=908)
        change_monster(removeSpawnId=509, addSpawnId=909)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return MafiaReadyToFight04()


class MafiaReadyToFight04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=504, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MafiaFightStart01()


class MafiaFightStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=25200471, textId=25200471) # 가이드 : 흑성회 조직원들 모두 쓰러트리기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900,901,902,903,904,905,906,907,908,909]):
            return MafiaFightEnd01()


class MafiaFightEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # 미션 성공 사운드 이펙트
        hide_guide_summary(entityId=25200471)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeihongWalkIn01()


#  웨이홍 바사라첸 입장 
class WeihongWalkIn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5100], visible=True) # DoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeihongWalkIn02()


class WeihongWalkIn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100], arg2=False) # 웨이 홍
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeihongWalkIn03()


class WeihongWalkIn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 바사라 첸
        move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        set_effect(triggerIds=[5101], visible=True) # DoorClose
        move_user(mapId=52000047, portalId=2, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeihongTalk01()


class WeihongTalk01(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__4$', arg4=4) # 웨이 홍
        set_skip(state=WeihongTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return WeihongTalk01Skip()


class WeihongTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_user_value(triggerId=500, key='NpcRemove', value=1)
        set_user_value(triggerId=501, key='NpcRemove', value=1)
        set_user_value(triggerId=502, key='NpcRemove', value=1)
        set_user_value(triggerId=503, key='NpcRemove', value=1)
        set_user_value(triggerId=504, key='NpcRemove', value=1)
        set_user_value(triggerId=505, key='NpcRemove', value=1)
        set_user_value(triggerId=506, key='NpcRemove', value=1)
        set_user_value(triggerId=507, key='NpcRemove', value=1)
        set_user_value(triggerId=508, key='NpcRemove', value=1)
        set_user_value(triggerId=509, key='NpcRemove', value=1)
        create_monster(spawnIds=[520,521,522,523,524,525,526,527,528,529], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeihongTalk02()


class WeihongTalk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__5$', arg4=4) # 웨이 홍
        set_skip(state=WeihongTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return WeihongTalk02Skip()


class WeihongTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetAgainWeihong01()


class MeetAgainWeihong01(state.State):
    def on_enter(self):
        move_npc(spawnId=520, patrolName='MS2PatrolData_520')
        move_npc(spawnId=521, patrolName='MS2PatrolData_521')
        move_npc(spawnId=522, patrolName='MS2PatrolData_522')
        move_npc(spawnId=523, patrolName='MS2PatrolData_523')
        move_npc(spawnId=524, patrolName='MS2PatrolData_524')
        move_npc(spawnId=525, patrolName='MS2PatrolData_525')
        move_npc(spawnId=526, patrolName='MS2PatrolData_526')
        move_npc(spawnId=527, patrolName='MS2PatrolData_527')
        move_npc(spawnId=528, patrolName='MS2PatrolData_528')
        move_npc(spawnId=529, patrolName='MS2PatrolData_529')
        set_conversation(type=1, spawnId=520, script='$52000047_QD__ACTION01__6$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetAgainWeihong02()


class MeetAgainWeihong02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=527, script='$52000047_QD__ACTION01__7$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=529, script='$52000047_QD__ACTION01__8$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MeetAgainWeihong03()


class MeetAgainWeihong03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__9$', arg4=4, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MeetAgainWeihong04()


class MeetAgainWeihong04(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='MS2PatrolData_101')
        move_npc(spawnId=200, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MeetAgainWeihong05()


class MeetAgainWeihong05(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetAgainWeihong06()

    def on_exit(self):
        destroy_monster(spawnIds=[100,200,520,521,522,523,524,525,526,527,528,529])
        create_monster(spawnIds=[101,201,530,531,532,533,534,535,536,537,538,539], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class MeetAgainWeihong06(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='MeetAgainWeihong')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NextQuestStart01()


#  다음 퀘스트 시작 
class NextQuestStart01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[10003044], questStates=[1]):
            return PositionArrange01()


class PositionArrange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PositionArrange02()


class PositionArrange02(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=True)
        move_user(mapId=52000047, portalId=3, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PositionArrange03()


class PositionArrange03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeihongStepBack01()


class WeihongStepBack01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000047_QD__ACTION01__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return WeihongStepBack02()


class WeihongStepBack02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        set_conversation(type=1, spawnId=101, script='$52000047_QD__ACTION01__11$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCTryToAttackWeihong01()


class PCTryToAttackWeihong01(state.State):
    def on_enter(self):
        select_camera(triggerId=710, enable=True)
        set_pc_emotion_loop(sequenceName='Knuckle_Attack_Idle_A', duration=1734)
        set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__12$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCTryToAttackWeihong02()


class PCTryToAttackWeihong02(state.State):
    def on_enter(self):
        select_camera(triggerId=711, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return PCTryToAttackWeihong03()


class PCTryToAttackWeihong03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return VasaraPush01()


class VasaraPush01(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=201, script='$52000047_QD__ACTION01__20$', arg4=1, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraPush02()


class VasaraPush02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_H')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraPush03()


class VasaraPush03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True) # PCKnockBack

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return VasaraPush04()


class VasaraPush04(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Push_A', duration=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SceneChange01()


class SceneChange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SceneChange02()


class SceneChange02(state.State):
    def on_enter(self):
        select_camera(triggerId=720, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SceneChange03()


class SceneChange03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VasaraTalk01()


class VasaraTalk01(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__13$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return VasaraTalk02()


class VasaraTalk02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000047_QD__ACTION01__14$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return VasaraTalk03()


class VasaraTalk03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000047_QD__ACTION01__15$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return VasaraBattle01()


class VasaraBattle01(state.State):
    def on_enter(self):
        select_camera(triggerId=720, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VasaraBattle02()


class VasaraBattle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=25200472, textId=25200472) # 가이드 : 바사라 첸 쓰러트리기

    def on_tick(self) -> state.State:
        if user_value(key='VasaraTired', value=1):
            return VasaraBattle03()


class VasaraBattle03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # 미션 성공 사운드 이펙트
        hide_guide_summary(entityId=25200472)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VasaraTired01()


class VasaraTired01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraTired02()


class VasaraTired02(state.State):
    def on_enter(self):
        select_camera(triggerId=720, enable=True)
        move_user(mapId=52000047, portalId=4, boxId=9900)
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraTired03()


class VasaraTired03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=203, sequenceName='Down_Idle_A', duration=9000)
        set_pc_emotion_loop(sequenceName='Knuckle_Attack_Idle_A', duration=9537)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraTired04()


class VasaraTired04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=600):
            return VasaraTired05()


class VasaraTired05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=203, script='$52000047_QD__ACTION01__21$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return WeihongOrder01()


class WeihongOrder01(state.State):
    def on_enter(self):
        select_camera(triggerId=730, enable=True)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeihongOrder02()


class WeihongOrder02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$52000047_QD__ACTION01__16$', arg4=5) # 웨이 홍
        set_skip(state=WeihongOrder02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WeihongOrder02Skip()


class WeihongOrder02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MafiaMove01()


class MafiaMove01(state.State):
    def on_enter(self):
        select_camera(triggerId=731, enable=True)
        move_npc(spawnId=530, patrolName='MS2PatrolData_530')
        move_npc(spawnId=535, patrolName='MS2PatrolData_535')
        move_npc(spawnId=534, patrolName='MS2PatrolData_534')
        move_npc(spawnId=537, patrolName='MS2PatrolData_537')
        move_npc(spawnId=532, patrolName='MS2PatrolData_532')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return MafiaMove02()


class MafiaMove02(state.State):
    def on_enter(self):
        move_npc(spawnId=531, patrolName='MS2PatrolData_531')
        move_npc(spawnId=533, patrolName='MS2PatrolData_533')
        move_npc(spawnId=536, patrolName='MS2PatrolData_536')
        move_npc(spawnId=538, patrolName='MS2PatrolData_538')
        move_npc(spawnId=539, patrolName='MS2PatrolData_539')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraTalk10()


class VasaraTalk10(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_204')
        set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__17$', arg4=5) # 바사라 첸
        set_skip(state=VasaraTalk10Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return VasaraTalk10Skip()


class VasaraTalk10Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return VasaraPushAgain01()


class VasaraPushAgain01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraPushAgain02()


class VasaraPushAgain02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_02_G,Attack_03_G')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return VasaraPushAgain03()


class VasaraPushAgain03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=True) # PCKnockBack

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VasaraPushAgain04()


class VasaraPushAgain04(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Push_A', duration=6000)
        set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_I,Attack_Idle_A,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return VasaraLastAttack01()


class VasaraLastAttack01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7002], isEnable=True) # CubeBreak
        set_effect(triggerIds=[5300], visible=True) # RockFall

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return VasaraLastAttack02()


class VasaraLastAttack02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5220], visible=True) # SandFlow
        set_random_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021], visible=True, meshCount=22, arg4=50, delay=80) # Rock Visible  ON
        set_effect(triggerIds=[5200], visible=True) # Dust
        set_effect(triggerIds=[5201], visible=True) # Dust
        set_effect(triggerIds=[5202], visible=True) # Dust
        set_effect(triggerIds=[5203], visible=True) # Dust
        set_effect(triggerIds=[5204], visible=True) # Dust
        set_effect(triggerIds=[5205], visible=True) # Dust
        set_effect(triggerIds=[5206], visible=True) # Dust
        set_effect(triggerIds=[5207], visible=True) # Dust
        set_effect(triggerIds=[5208], visible=True) # Dust
        set_effect(triggerIds=[5209], visible=True) # Dust
        set_effect(triggerIds=[5210], visible=True) # Dust

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VasaraLastAttack03()


class VasaraLastAttack03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5221], visible=True) # SandFlow
        select_camera(triggerId=731, enable=True)
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Barrier Visible OFF

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return VasaraTalk20()

    def on_exit(self):
        set_effect(triggerIds=[5220], visible=True) # SandFlow


class VasaraTalk20(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__18$', arg4=5) # 바사라 첸
        set_skip(state=VasaraTalk20Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return VasaraTalk20Skip()


class VasaraTalk20Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return VasaraTalk21()


class VasaraTalk21(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$52000047_QD__ACTION01__19$', arg4=5) # 바사라 첸
        set_skip(state=VasaraTalk21Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return VasaraTalk21Skip()


class VasaraTalk21Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=731, enable=False)
        set_effect(triggerIds=[5221], visible=True) # SandFlow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FriendOfVasara01()


class FriendOfVasara01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5220], visible=True) # SandFlow
        set_achievement(triggerId=9900, type='trigger', achieve='FriendOfVasara')
        move_npc(spawnId=203, patrolName='MS2PatrolData_205')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5221], visible=True) # SandFlow
        move_user(mapId=2000138, portalId=105, boxId=9900)


