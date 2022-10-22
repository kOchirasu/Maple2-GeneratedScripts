""" trigger/63000025_cs/training01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5105], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5200], visible=False) # 점프 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내
        set_effect(triggerIds=[5301], visible=False) # 화살표 안내
        set_effect(triggerIds=[5400], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5401], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5402], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5403], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5404], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5405], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5406], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5407], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5408], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5409], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5410], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5500], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5501], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5502], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5503], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5504], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001676
        set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001677
        set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001678
        set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001714
        set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001679
        set_effect(triggerIds=[6005], visible=False) # Voice_Tinchai_00001680
        set_effect(triggerIds=[6006], visible=False) # Voice_Tinchai_00001720
        set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001760
        set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001761
        set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001762
        set_effect(triggerIds=[6103], visible=False) # Voice_Junta_00001763
        set_effect(triggerIds=[6104], visible=False) # Voice_Junta_00001764
        set_effect(triggerIds=[6105], visible=False) # Voice_Junta_00001765
        set_effect(triggerIds=[6106], visible=False) # Voice_Junta_00001766
        set_effect(triggerIds=[6107], visible=False) # Voice_Junta_00001767
        set_effect(triggerIds=[6108], visible=False) # Voice_Junta_00001768
        set_effect(triggerIds=[6109], visible=False) # Voice_Junta_00001769
        set_effect(triggerIds=[6110], visible=False) # Voice_Junta_00001770
        set_effect(triggerIds=[6111], visible=False) # Voice_Junta_00001771
        set_effect(triggerIds=[6112], visible=False) # Voice_Junta_00001772
        set_interact_object(triggerIds=[10001003], state=0) # Training

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[1]):
            return TimeToLeave02()
        if quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[3]):
            return ReadyToMove02()
        if quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[2]):
            return QuestOnGoing41()
        if quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[1]):
            return QuestOnGoing41()
        if quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[3]):
            return QuestOnGoing41()
        if quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[2]):
            return QuestOnGoing41()
        if quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[1]):
            return QuestOnGoing41()
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[3]):
            return QuestOnGoing31()
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[2]):
            return QuestOnGoing21()
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[1]):
            return QuestOnGoing11()
        if quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[3]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[2]):
            return Enter02()
        if wait_tick(waitTick=5000):
            return Quit()


#  스킬 사용 가이드 진행 중인 상태 
class QuestOnGoing41(state.State):
    def on_enter(self):
        move_user(mapId=63000025, portalId=10, boxId=9900)
        create_monster(spawnIds=[104,204], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return QuestOnGoing42()


class QuestOnGoing42(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SkillUseGuide02()


#  엄격한 대제자의 지도 퀘스트 완료 상태 
class QuestOnGoing31(state.State):
    def on_enter(self):
        move_user(mapId=63000025, portalId=10, boxId=9900)
        create_monster(spawnIds=[104,204], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return QuestOnGoing32()


class QuestOnGoing32(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SkillUseGuide01()


#  엄격한 대제자의 지도 퀘스트 완료 가능 상태 
class QuestOnGoing21(state.State):
    def on_enter(self):
        move_user(mapId=63000025, portalId=10, boxId=9900)
        create_monster(spawnIds=[104,204], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return QuestOnGoing22()


class QuestOnGoing22(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SecondQuestEnd01()


#  엄격한 대제자의 지도 퀘스트 수락한 상태 
class QuestOnGoing11(state.State):
    def on_enter(self):
        move_user(mapId=63000025, portalId=30, boxId=9900)
        create_monster(spawnIds=[102,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return QuestOnGoing12()


class QuestOnGoing12(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JumpPointGuide01()


#  가이던스의 대제자 퀘스트 완료 상태 
class QuestOnGoing01(state.State):
    def on_enter(self):
        move_user(mapId=63000025, portalId=30, boxId=9900)
        create_monster(spawnIds=[102,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return QuestOnGoing02()


class QuestOnGoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SecondQuestStart01()


#  최초 입장 
class Enter02(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=Dialogue10, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Enter03()


class Enter03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Enter04()


class Enter04(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Enter05()


class Enter05(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Enter06()


class Enter06(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001760
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__0$', arg4=5) # 준타 00001760

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001761
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__1$', arg4=7) # 준타 00001761
        set_skip(state=Dialogue04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Dialogue04()


class Dialogue04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue05()


class Dialogue05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001676
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__2$', arg4=6) # 틴차이 00001676
        set_skip(state=Dialogue06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return Dialogue06()


class Dialogue06(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue07()


class Dialogue07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001762
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__3$', arg4=6) # 준타 00001762
        set_skip(state=Dialogue08)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Dialogue08()


class Dialogue08(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue09()


class Dialogue09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001677
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__4$', arg4=4) # 틴차이 00001677

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue10()


class Dialogue10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=502, enable=False)
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstQuestEnd01()


class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[3]):
            return SecondQuestStart01()


class SecondQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        hide_guide_summary(entityId=10031010)
        show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[1]):
            return JumpPointGuide01()


class JumpPointGuide01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10031020)
        show_guide_summary(entityId=10031030, textId=10031030) # 가이드 : 물가로 이동하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5100], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5101], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5102], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5103], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5104], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5105], visible=True) # 웅덩이 경로 안내
        set_effect(triggerIds=[5200], visible=True) # 점프 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 점프 경로 안내
        set_effect(triggerIds=[5301], visible=True) # 화살표 안내
        destroy_monster(spawnIds=[102,202])
        create_monster(spawnIds=[103,203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JumpPointGuide02()


class JumpPointGuide02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6103], visible=True) # Voice_Junta_00001763
        set_conversation(type=1, spawnId=103, script='$63000025_CS__TRAINING01__5$', arg4=3, arg5=0) # 준타 00001763
        move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        move_npc(spawnId=203, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return JumpPointGuide03()


class JumpPointGuide03(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10031030)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031031, textId=10031031) # 가이드 : C키로 점프해 기둥 위로 올라가기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return JumpPointGuide04()


class JumpPointGuide04(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001003], state=1) # Training
        hide_guide_summary(entityId=10031031)
        show_guide_summary(entityId=10031032, textId=10031032) # 가이드 : 스페이스 키를 눌러 기둥 위에서 수련하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5301], visible=False) # 화살표 안내
        set_effect(triggerIds=[5100], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5105], visible=False) # 웅덩이 경로 안내
        set_effect(triggerIds=[5200], visible=False) # 점프 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[2]):
            return SecondQuestEnd01()

    def on_exit(self):
        destroy_monster(spawnIds=[103,203])
        create_monster(spawnIds=[104,204], arg2=False)
        hide_guide_summary(entityId=10031032)


class SecondQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031050, textId=10031050) # 가이드 : 준타를 향해 이동하기
        set_effect(triggerIds=[5500], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5501], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5502], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5503], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5504], visible=True) # NPC 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return SecondQuestEnd02()

    def on_exit(self):
        hide_guide_summary(entityId=10031050)
        set_effect(triggerIds=[5500], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5501], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5502], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5503], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5504], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내


class SecondQuestEnd02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[3]):
            return SkillUseGuide01()

    def on_exit(self):
        hide_guide_summary(entityId=10031010)


#  스킬 사용 퀘스트 2개 90000446, 90000447 가이드 
class SkillUseGuide01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SkillUseGuide02()


class SkillUseGuide02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[3]):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToMove01()


class ReadyToMove01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ReadyToMove02()


class ReadyToMove02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        destroy_monster(spawnIds=[104,204]) # Talk
        create_monster(spawnIds=[105,205], arg2=False) # Actor
        move_user(mapId=63000025, portalId=10, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PatrolWalk01()


class PatrolWalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=105, patrolName='MS2PatrolData_103')
        move_npc(spawnId=205, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolWalk02()


class PatrolWalk02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FeelStrange01()


class FeelStrange01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6104], visible=True) # Voice_Junta_00001764
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__6$', arg4=5) # 준타 00001764
        set_scene_skip(state=FeelStrange18, arg2='nextState')
        set_skip(state=FeelStrange02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FeelStrange02()


class FeelStrange02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange03()


class FeelStrange03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6105], visible=True) # Voice_Junta_00001765
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__7$', arg4=3) # 준타 00001765
        set_skip(state=FeelStrange04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FeelStrange04()


class FeelStrange04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange05()


class FeelStrange05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001678
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__8$', arg4=4) # 틴차이 00001678
        set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        set_skip(state=FeelStrange06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FeelStrange06()


class FeelStrange06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange07()


class FeelStrange07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6106], visible=True) # Voice_Junta_00001766
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__9$', arg4=4) # 준타 00001766
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        set_skip(state=FeelStrange08)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FeelStrange08()


class FeelStrange08(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange09()


class FeelStrange09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001714
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__10$', arg4=4) # 틴차이 00001714
        set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        set_skip(state=FeelStrange10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FeelStrange10()


class FeelStrange10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange11()


class FeelStrange11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6107], visible=True) # Voice_Junta_00001767
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__11$', arg4=6) # 준타 00001767
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        set_skip(state=FeelStrange12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return FeelStrange12()


class FeelStrange12(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange13()


class FeelStrange13(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001679
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__12$', arg4=4) # 틴차이 00001679
        set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        set_skip(state=FeelStrange14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FeelStrange14()


class FeelStrange14(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange15()


class FeelStrange15(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6108], visible=True) # Voice_Junta_00001768
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__13$', arg4=5) # 준타 00001768
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        set_skip(state=FeelStrange16)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FeelStrange16()


class FeelStrange16(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return FeelStrange17()


class FeelStrange17(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6005], visible=True) # Voice_Tinchai_00001680
        set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__14$', arg4=3) # 틴차이 00001680

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FeelStrange18()


class FeelStrange18(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[105,205]) # Actor
        create_monster(spawnIds=[106,206], arg2=False) # Talk

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LastQuestStart01()


class LastQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[1]):
            return Delay02()


class Delay02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10031020)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MinimapGuide01()


class MinimapGuide01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[6109], visible=True) # Voice_Junta_00001769
        set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__19$', arg4=7) # 준타 00001769
        set_npc_emotion_sequence(spawnId=106, sequenceName='Talk_A')
        set_skip(state=MinimapGuide02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return MinimapGuide02()


class MinimapGuide02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return MinimapGuide03()


#  미니맵 가이드 : 트리거 To 가이드 
class MinimapGuide03(state.State):
    def on_enter(self):
        guide_event(eventId=10031080) # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10031083'):
            return Delay03()


class Delay03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave01()


class TimeToLeave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave02()


class TimeToLeave02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False)
        move_user(mapId=63000025, portalId=20, boxId=9900)
        destroy_monster(spawnIds=[106,206]) # Talk
        create_monster(spawnIds=[107,207], arg2=False) # Actor
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave03()


class TimeToLeave03(state.State):
    def on_enter(self):
        set_scene_skip(state=NpcLeave_CSkip, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Monologue01()


class Monologue01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6110], visible=True) # Voice_Junta_00001770
        set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__15$', arg4=2, arg5=0) # 준타 00001770

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return Monologue02()


class Monologue02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        move_npc(spawnId=107, patrolName='MS2PatrolData_104')
        move_npc(spawnId=207, patrolName='MS2PatrolData_204')
        set_effect(triggerIds=[6111], visible=True) # Voice_Junta_00001771
        set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__16$', arg4=3, arg5=0) # 준타 00001771

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Monologue03()


class Monologue03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6006], visible=True) # Voice_Tinchai_00001720
        set_conversation(type=1, spawnId=207, script='$63000025_CS__TRAINING01__17$', arg4=3, arg5=0) # 틴차이 00001720

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Monologue04()


class Monologue04(state.State):
    def on_enter(self):
        select_camera(triggerId=702, enable=True)
        set_effect(triggerIds=[6112], visible=True) # Voice_Junta_00001772
        set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__18$', arg4=2, arg5=0) # 준타 00001772

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2200):
            return NpcLeave01()


class NpcLeave01(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[107])
        move_user(mapId=63000025, portalId=40, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return NpcLeave02()


class NpcLeave02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[207])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GuideNextMap01()


class NpcLeave_CSkip(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[107])
        destroy_monster(spawnIds=[207])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GuideNextMap01()


class GuideNextMap01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=702, enable=False)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10020012, textId=10020012) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5400], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5401], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5402], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5403], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5404], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5405], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5406], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5407], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5408], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5409], visible=True) # 포털 경로 안내
        set_effect(triggerIds=[5410], visible=True) # 포털 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return GuideNextMap02()


class GuideNextMap02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10020012)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        hide_guide_summary(entityId=1060)
        set_effect(triggerIds=[5400], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5401], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5402], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5403], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5404], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5405], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5406], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5407], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5408], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5409], visible=False) # 포털 경로 안내
        set_effect(triggerIds=[5410], visible=False) # 포털 경로 안내


