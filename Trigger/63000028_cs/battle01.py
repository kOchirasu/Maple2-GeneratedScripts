""" trigger/63000028_cs/battle01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001684
        set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001685
        set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001686
        set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001717
        set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001687
        set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001773
        set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001774
        set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001775
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        set_agent(triggerIds=[8105], visible=False)
        set_agent(triggerIds=[8106], visible=False)
        set_agent(triggerIds=[8107], visible=False)
        set_agent(triggerIds=[8108], visible=False)
        set_agent(triggerIds=[8109], visible=False)
        set_agent(triggerIds=[8110], visible=False)
        set_agent(triggerIds=[8111], visible=False)
        set_agent(triggerIds=[8112], visible=False)
        set_agent(triggerIds=[8113], visible=False)
        set_agent(triggerIds=[8114], visible=False)
        set_agent(triggerIds=[8115], visible=False)
        set_skill(triggerIds=[7000], isEnable=False) # 올킬

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[1]):
            return QuestOnGoing21()
        if quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[3]):
            return QuestOnGoing11()
        if quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[2]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[1]):
            return PCWakeUp01()


#  별, 수정, 그리고 퀘스트 완료 가능 상태 
class QuestOnGoing01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FirstQuestEnd01()


#  별, 수정, 그리고 퀘스트 완료 상태  
class QuestOnGoing11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SecondQuestStart01()


#  그림자의 파도 퀘스트 수락한 상태  
class QuestOnGoing21(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGoing22()


class QuestOnGoing22(state.State):
    def on_enter(self):
        move_user(mapId=63000028, portalId=11, boxId=9900)
        create_monster(spawnIds=[104,203], arg2=False)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGoing23()


class QuestOnGoing23(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return ShadowWaveAgain02()


#  최초 입장 
class PCWakeUp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCWakeUp02()


class PCWakeUp02(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=TinChaiTalk02_CSkip, arg2='nextState')
        create_monster(spawnIds=[101,900,901,902], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCWakeUp03()


class PCWakeUp03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCWakeUp04()


class PCWakeUp04(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Bore_C'])
        set_conversation(type=1, spawnId=0, script='$63000028_CS__BATTLE01__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return PCWakeUp05()


class PCWakeUp05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$63000028_CS__BATTLE01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleING01()


class BattleING01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleING02()


class BattleING02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TinChaiTalk01()


class TinChaiTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001684
        set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__2$', arg4=5) # 틴차이 00001684
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TinChaiTalk02()


class TinChaiTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ReadyToBattle01()


class TinChaiTalk02_CSkip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return ReadyToBattle01()


class ReadyToBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        select_camera(triggerId=501, enable=False)

    def on_tick(self) -> state.State:
        if true():
            return ReadyToBattle02()


#  HP 가이드 
class ReadyToBattle02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BattleStart01()


class BattleStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10035010, textId=10035010) # 가이드 : 틴차이를 도와 검은 그림자 처치하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleStart02()


class BattleStart02(state.State):
    def on_enter(self):
        guide_event(eventId=10035020) # 트리거 To가이드 : HP가 0이 되면 비석에 깔리니 조심

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900,901,902]):
            return BattleEnd01()

    def on_exit(self):
        hide_guide_summary(entityId=10035010)


class BattleEnd01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[900,901,902])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleEnd02()


class BattleEnd02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleEnd03()


class BattleEnd03(state.State):
    def on_enter(self):
        move_user(mapId=63000028, portalId=10, boxId=9900)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleEnd04()


class BattleEnd04(state.State):
    def on_enter(self):
        set_scene_skip(state=MeetJunta05_Cskip, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleEnd05()


class BattleEnd05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$63000028_CS__BATTLE01__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShadowWave01()


class ShadowWave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        set_agent(triggerIds=[8102], visible=True)
        set_agent(triggerIds=[8103], visible=True)
        set_agent(triggerIds=[8104], visible=True)
        set_agent(triggerIds=[8105], visible=True)
        set_agent(triggerIds=[8106], visible=True)
        set_agent(triggerIds=[8107], visible=True)
        set_agent(triggerIds=[8108], visible=True)
        set_agent(triggerIds=[8109], visible=True)
        set_agent(triggerIds=[8110], visible=True)
        set_agent(triggerIds=[8111], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowWave02()


class ShadowWave02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        set_effect(triggerIds=[5100], visible=True) # Sound_ShadowApp_Loop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWave03()


#  정면 1차 스폰 후 다리 패트롤 바로 시작 
class ShadowWave03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910,911,912,913])
        move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        move_npc(spawnId=913, patrolName='MS2PatrolData_913')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowWave04()


#  정면 2차 스폰 후 다리 패트롤 바로 시작 
class ShadowWave04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[920,921,922,923,924])
        move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        move_npc(spawnId=924, patrolName='MS2PatrolData_924')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWave05()


#  카메라 워크  
class ShadowWave05(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowWave06()


class ShadowWave06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[930,931,932,933,950,951,952,953])
        move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        move_npc(spawnId=932, patrolName='MS2PatrolData_932')
        move_npc(spawnId=933, patrolName='MS2PatrolData_933')
        move_npc(spawnId=950, patrolName='MS2PatrolData_950')
        move_npc(spawnId=951, patrolName='MS2PatrolData_951')
        move_npc(spawnId=952, patrolName='MS2PatrolData_952')
        move_npc(spawnId=953, patrolName='MS2PatrolData_953')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWave07()


#  양측 2차 스폰 
class ShadowWave07(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$63000028_CS__BATTLE01__4$', arg4=3, arg5=0) # 틴차이
        create_monster(spawnIds=[940,941,942,943,944,945,960,961,962,963,964,965])
        move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        move_npc(spawnId=943, patrolName='MS2PatrolData_943')
        move_npc(spawnId=944, patrolName='MS2PatrolData_944')
        move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        move_npc(spawnId=960, patrolName='MS2PatrolData_960')
        move_npc(spawnId=961, patrolName='MS2PatrolData_961')
        move_npc(spawnId=962, patrolName='MS2PatrolData_962')
        move_npc(spawnId=963, patrolName='MS2PatrolData_963')
        move_npc(spawnId=964, patrolName='MS2PatrolData_964')
        move_npc(spawnId=965, patrolName='MS2PatrolData_965')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TinChaiDesperate01()


class TinChaiDesperate01(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)
        set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=12000)
        set_pc_emotion_loop(sequenceName='Orb_Attack_Idle_A', duration=12000)
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001685
        set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__5$', arg4=5) # 틴차이 00001685
        set_skip(state=TinChaiDesperate02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TinChaiDesperate02()


class TinChaiDesperate02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaApp01()


class JuntaApp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JuntaApp02()


class JuntaApp02(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=True)
        destroy_monster(spawnIds=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        create_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JuntaApp03()


class JuntaApp03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        set_agent(triggerIds=[8105], visible=False)
        set_agent(triggerIds=[8106], visible=False)
        set_agent(triggerIds=[8107], visible=False)
        set_agent(triggerIds=[8108], visible=False)
        set_agent(triggerIds=[8109], visible=False)
        set_agent(triggerIds=[8110], visible=False)
        set_agent(triggerIds=[8111], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JuntaApp04()


class JuntaApp04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False) # 11001742_M_Junta 준타 Regen_A

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return JuntaTalk01()

    def on_exit(self):
        set_skill(triggerIds=[7000], isEnable=True) # 올킬


class JuntaTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001773
        set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__6$', arg4=4) # 준타 00001773

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MeetJunta01()


class MeetJunta01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        move_user_path(patrolName='MS2PatrolData_1003')
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MeetJunta02()

    def on_exit(self):
        remove_cinematic_talk()


class MeetJunta02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001686
        set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__7$', arg4=5) # 틴차이 00001686

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return MeetJunta03()


class MeetJunta03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return MeetJunta04()


class MeetJunta04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001774
        set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__8$', arg4=7) # 준타 00001774

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return MeetJunta05()


class MeetJunta05_Cskip(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        destroy_monster(spawnIds=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MeetJunta05_Cskip2()


class MeetJunta05_Cskip2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        destroy_monster(spawnIds=[102,201])
        create_monster(spawnIds=[103,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetJunta06()

    def on_exit(self):
        remove_cinematic_talk()


class MeetJunta05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        destroy_monster(spawnIds=[102,201])
        create_monster(spawnIds=[103,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MeetJunta06()


class MeetJunta06(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9900, type='trigger', achieve='complete_airstrikeofjunta')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[2]):
            return FirstQuestEnd01()


class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[3]):
            return SecondQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10031010)


class SecondQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000452], questStates=[1]):
            return Delay01()

    def on_exit(self):
        hide_guide_summary(entityId=10031020)


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Delay02()


class Delay02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowWaveAgain01()


class ShadowWaveAgain01(state.State):
    def on_enter(self):
        move_user(mapId=63000028, portalId=12, boxId=9900)
        destroy_monster(spawnIds=[103,202])
        create_monster(spawnIds=[104,203], arg2=False)
        select_camera(triggerId=600, enable=True)
        set_scene_skip(state=TimeToLeave05, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowWaveAgain02()


#  정면 1차 스폰 후 다리 패트롤 바로 시작 
class ShadowWaveAgain02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        set_agent(triggerIds=[8102], visible=True)
        set_agent(triggerIds=[8103], visible=True)
        set_agent(triggerIds=[8106], visible=True)
        set_agent(triggerIds=[8107], visible=True)
        set_agent(triggerIds=[8108], visible=True)
        set_agent(triggerIds=[8109], visible=True)
        set_agent(triggerIds=[8110], visible=True)
        set_agent(triggerIds=[8111], visible=True)
        set_agent(triggerIds=[8112], visible=True)
        set_agent(triggerIds=[8113], visible=True)
        set_agent(triggerIds=[8114], visible=True)
        set_agent(triggerIds=[8115], visible=True)
        create_monster(spawnIds=[910,911,912,913])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWaveAgain03()


#  정면 2차 스폰 후 다리 패트롤 바로 시작 
class ShadowWaveAgain03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        set_effect(triggerIds=[5100], visible=True) # Sound_ShadowApp_Loop
        set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001717
        set_conversation(type=1, spawnId=104, script='$63000028_CS__BATTLE01__9$', arg4=3, arg5=1) # 틴차이 00001717
        move_npc(spawnId=104, patrolName='MS2PatrolData_103')
        move_user_path(patrolName='MS2PatrolData_1004')
        create_monster(spawnIds=[920,921,922,923,924])
        move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        move_npc(spawnId=913, patrolName='MS2PatrolData_913')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWaveAgain04()


#  카메라 워크  
class ShadowWaveAgain04(state.State):
    def on_enter(self):
        move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        move_npc(spawnId=924, patrolName='MS2PatrolData_924')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShadowWaveAgain05()


class ShadowWaveAgain05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001775
        set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__10$', arg4=4) # 준타 00001775
        create_monster(spawnIds=[930,931,932,933,950,951,952,953])
        move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        move_npc(spawnId=932, patrolName='MS2PatrolData_932')
        move_npc(spawnId=933, patrolName='MS2PatrolData_933')
        move_npc(spawnId=950, patrolName='MS2PatrolData_950')
        move_npc(spawnId=951, patrolName='MS2PatrolData_951')
        move_npc(spawnId=952, patrolName='MS2PatrolData_952')
        move_npc(spawnId=953, patrolName='MS2PatrolData_953')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowWaveAgain06()


#  양측 2차 스폰 
class ShadowWaveAgain06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[940,941,942,943,944,945,960,961,962,963,964,965])
        move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        move_npc(spawnId=943, patrolName='MS2PatrolData_943')
        move_npc(spawnId=944, patrolName='MS2PatrolData_944')
        move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        move_npc(spawnId=960, patrolName='MS2PatrolData_960')
        move_npc(spawnId=961, patrolName='MS2PatrolData_961')
        move_npc(spawnId=962, patrolName='MS2PatrolData_962')
        move_npc(spawnId=963, patrolName='MS2PatrolData_963')
        move_npc(spawnId=964, patrolName='MS2PatrolData_964')
        move_npc(spawnId=965, patrolName='MS2PatrolData_965')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TimeToLeave01()


class TimeToLeave01(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)
        set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001687
        set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__11$', arg4=4) # 틴차이 00001687
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TimeToLeave02()


class TimeToLeave02(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return TimeToLeave03()


class TimeToLeave03(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_104')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave04()


class TimeToLeave04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1005')
        select_camera(triggerId=602, enable=False)
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return TimeToLeave05()


class TimeToLeave05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104,203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=63000029, portalId=1, boxId=9900)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    pass


