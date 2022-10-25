""" trigger/63000025_cs/training01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_widget(type='Guide')
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5104], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5105], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5200], visible=False) # 점프 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내
        self.set_effect(triggerIds=[5301], visible=False) # 화살표 안내
        self.set_effect(triggerIds=[5400], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5408], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5409], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5410], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5500], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5501], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5502], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5503], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5504], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001676
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001677
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001678
        self.set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001714
        self.set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001679
        self.set_effect(triggerIds=[6005], visible=False) # Voice_Tinchai_00001680
        self.set_effect(triggerIds=[6006], visible=False) # Voice_Tinchai_00001720
        self.set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001760
        self.set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001761
        self.set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001762
        self.set_effect(triggerIds=[6103], visible=False) # Voice_Junta_00001763
        self.set_effect(triggerIds=[6104], visible=False) # Voice_Junta_00001764
        self.set_effect(triggerIds=[6105], visible=False) # Voice_Junta_00001765
        self.set_effect(triggerIds=[6106], visible=False) # Voice_Junta_00001766
        self.set_effect(triggerIds=[6107], visible=False) # Voice_Junta_00001767
        self.set_effect(triggerIds=[6108], visible=False) # Voice_Junta_00001768
        self.set_effect(triggerIds=[6109], visible=False) # Voice_Junta_00001769
        self.set_effect(triggerIds=[6110], visible=False) # Voice_Junta_00001770
        self.set_effect(triggerIds=[6111], visible=False) # Voice_Junta_00001771
        self.set_effect(triggerIds=[6112], visible=False) # Voice_Junta_00001772
        self.set_interact_object(triggerIds=[10001003], state=0) # Training

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[1]):
            return TimeToLeave02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[3]):
            return ReadyToMove02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[2]):
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[1]):
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[3]):
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[2]):
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000446], questStates=[1]):
            return QuestOnGoing41(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[3]):
            return QuestOnGoing31(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[2]):
            return QuestOnGoing21(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[1]):
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[3]):
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[2]):
            return Enter02(self.ctx)
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


# 스킬 사용 가이드 진행 중인 상태
class QuestOnGoing41(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000025, portalId=10, boxId=9900)
        self.create_monster(spawnIds=[104,204], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return QuestOnGoing42(self.ctx)


class QuestOnGoing42(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return SkillUseGuide02(self.ctx)


# 엄격한 대제자의 지도 퀘스트 완료 상태
class QuestOnGoing31(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000025, portalId=10, boxId=9900)
        self.create_monster(spawnIds=[104,204], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return QuestOnGoing32(self.ctx)


class QuestOnGoing32(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return SkillUseGuide01(self.ctx)


# 엄격한 대제자의 지도 퀘스트 완료 가능 상태
class QuestOnGoing21(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000025, portalId=10, boxId=9900)
        self.create_monster(spawnIds=[104,204], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return QuestOnGoing22(self.ctx)


class QuestOnGoing22(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return SecondQuestEnd01(self.ctx)


# 엄격한 대제자의 지도 퀘스트 수락한 상태
class QuestOnGoing11(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000025, portalId=30, boxId=9900)
        self.create_monster(spawnIds=[102,202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return QuestOnGoing12(self.ctx)


class QuestOnGoing12(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return JumpPointGuide01(self.ctx)


# 가이던스의 대제자 퀘스트 완료 상태
class QuestOnGoing01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000025, portalId=30, boxId=9900)
        self.create_monster(spawnIds=[102,202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return SecondQuestStart01(self.ctx)


# 최초 입장
class Enter02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=Dialogue10, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Enter03(self.ctx)


class Enter03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Enter04(self.ctx)


class Enter04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Enter05(self.ctx)


class Enter05(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Enter06(self.ctx)


class Enter06(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Dialogue01(self.ctx)


class Dialogue01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001760
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__0$', arg4=5) # 준타 00001760

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Dialogue02(self.ctx)


class Dialogue02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue03(self.ctx)


class Dialogue03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001761
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__1$', arg4=7) # 준타 00001761
        self.set_skip(state=Dialogue04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Dialogue04(self.ctx)


class Dialogue04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue05(self.ctx)


class Dialogue05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001676
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__2$', arg4=6) # 틴차이 00001676
        self.set_skip(state=Dialogue06)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return Dialogue06(self.ctx)


class Dialogue06(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue07(self.ctx)


class Dialogue07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001762
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__3$', arg4=6) # 준타 00001762
        self.set_skip(state=Dialogue08)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return Dialogue08(self.ctx)


class Dialogue08(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue09(self.ctx)


class Dialogue09(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001677
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__4$', arg4=4) # 틴차이 00001677

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Dialogue10(self.ctx)


class Dialogue10(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=502, enable=False)
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[3]):
            return SecondQuestStart01(self.ctx)


class SecondQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.hide_guide_summary(entityId=10031010)
        self.show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[1]):
            return JumpPointGuide01(self.ctx)


class JumpPointGuide01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10031020)
        self.show_guide_summary(entityId=10031030, textId=10031030) # 가이드 : 물가로 이동하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5101], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5102], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5103], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5104], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5105], visible=True) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5200], visible=True) # 점프 경로 안내
        self.set_effect(triggerIds=[5203], visible=True) # 점프 경로 안내
        self.set_effect(triggerIds=[5301], visible=True) # 화살표 안내
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[103,203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return JumpPointGuide02(self.ctx)


class JumpPointGuide02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6103], visible=True) # Voice_Junta_00001763
        self.set_conversation(type=1, spawnId=103, script='$63000025_CS__TRAINING01__5$', arg4=3, arg5=0) # 준타 00001763
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_202')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return JumpPointGuide03(self.ctx)


class JumpPointGuide03(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10031030)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031031, textId=10031031) # 가이드 : C키로 점프해 기둥 위로 올라가기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return JumpPointGuide04(self.ctx)


class JumpPointGuide04(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001003], state=1) # Training
        self.hide_guide_summary(entityId=10031031)
        self.show_guide_summary(entityId=10031032, textId=10031032) # 가이드 : 스페이스 키를 눌러 기둥 위에서 수련하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5301], visible=False) # 화살표 안내
        self.set_effect(triggerIds=[5100], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5104], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5105], visible=False) # 웅덩이 경로 안내
        self.set_effect(triggerIds=[5200], visible=False) # 점프 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[2]):
            return SecondQuestEnd01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[103,203])
        self.create_monster(spawnIds=[104,204], animationEffect=False)
        self.hide_guide_summary(entityId=10031032)


class SecondQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031050, textId=10031050) # 가이드 : 준타를 향해 이동하기
        self.set_effect(triggerIds=[5500], visible=True) # NPC 경로 안내
        self.set_effect(triggerIds=[5501], visible=True) # NPC 경로 안내
        self.set_effect(triggerIds=[5502], visible=True) # NPC 경로 안내
        self.set_effect(triggerIds=[5503], visible=True) # NPC 경로 안내
        self.set_effect(triggerIds=[5504], visible=True) # NPC 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9300]):
            return SecondQuestEnd02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10031050)
        self.set_effect(triggerIds=[5500], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5501], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5502], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5503], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5504], visible=False) # NPC 경로 안내
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5203], visible=False) # 점프 경로 안내


class SecondQuestEnd02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000445], questStates=[3]):
            return SkillUseGuide01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10031010)


# 스킬 사용 퀘스트 2개 90000446, 90000447 가이드
class SkillUseGuide01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SkillUseGuide02(self.ctx)


class SkillUseGuide02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000447], questStates=[3]):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToMove01(self.ctx)


class ReadyToMove01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ReadyToMove02(self.ctx)


class ReadyToMove02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)
        self.destroy_monster(spawnIds=[104,204]) # Talk
        self.create_monster(spawnIds=[105,205], animationEffect=False) # Actor
        self.move_user(mapId=63000025, portalId=10, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PatrolWalk01(self.ctx)


class PatrolWalk01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_203')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolWalk02(self.ctx)


class PatrolWalk02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FeelStrange01(self.ctx)


class FeelStrange01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6104], visible=True) # Voice_Junta_00001764
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__6$', arg4=5) # 준타 00001764
        self.set_scene_skip(state=FeelStrange18, action='nextState')
        self.set_skip(state=FeelStrange02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FeelStrange02(self.ctx)


class FeelStrange02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange03(self.ctx)


class FeelStrange03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6105], visible=True) # Voice_Junta_00001765
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__7$', arg4=3) # 준타 00001765
        self.set_skip(state=FeelStrange04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FeelStrange04(self.ctx)


class FeelStrange04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange05(self.ctx)


class FeelStrange05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001678
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__8$', arg4=4) # 틴차이 00001678
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange06)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FeelStrange06(self.ctx)


class FeelStrange06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange07(self.ctx)


class FeelStrange07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6106], visible=True) # Voice_Junta_00001766
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__9$', arg4=4) # 준타 00001766
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange08)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FeelStrange08(self.ctx)


class FeelStrange08(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange09(self.ctx)


class FeelStrange09(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001714
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__10$', arg4=4) # 틴차이 00001714
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FeelStrange10(self.ctx)


class FeelStrange10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange11(self.ctx)


class FeelStrange11(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6107], visible=True) # Voice_Junta_00001767
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__11$', arg4=6) # 준타 00001767
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange12)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return FeelStrange12(self.ctx)


class FeelStrange12(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange13(self.ctx)


class FeelStrange13(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001679
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__12$', arg4=4) # 틴차이 00001679
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange14)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FeelStrange14(self.ctx)


class FeelStrange14(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange15(self.ctx)


class FeelStrange15(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6108], visible=True) # Voice_Junta_00001768
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__13$', arg4=5) # 준타 00001768
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        self.set_skip(state=FeelStrange16)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FeelStrange16(self.ctx)


class FeelStrange16(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FeelStrange17(self.ctx)


class FeelStrange17(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6005], visible=True) # Voice_Tinchai_00001680
        self.set_conversation(type=2, spawnId=11001708, script='$63000025_CS__TRAINING01__14$', arg4=3) # 틴차이 00001680

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FeelStrange18(self.ctx)


class FeelStrange18(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[105,205]) # Actor
        self.create_monster(spawnIds=[106,206], animationEffect=False) # Talk

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LastQuestStart01(self.ctx)


class LastQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[1]):
            return Delay02(self.ctx)


class Delay02(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10031020)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return MinimapGuide01(self.ctx)


class MinimapGuide01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[6109], visible=True) # Voice_Junta_00001769
        self.set_conversation(type=2, spawnId=11001557, script='$63000025_CS__TRAINING01__19$', arg4=7) # 준타 00001769
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Talk_A')
        self.set_skip(state=MinimapGuide02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return MinimapGuide02(self.ctx)


class MinimapGuide02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return MinimapGuide03(self.ctx)


# 미니맵 가이드 : 트리거 To 가이드
class MinimapGuide03(common.Trigger):
    def on_enter(self):
        self.guide_event(eventId=10031080) # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='10031083'):
            return Delay03(self.ctx)


class Delay03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False)
        self.move_user(mapId=63000025, portalId=20, boxId=9900)
        self.destroy_monster(spawnIds=[106,206]) # Talk
        self.create_monster(spawnIds=[107,207], animationEffect=False) # Actor
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=NpcLeave_CSkip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Monologue01(self.ctx)


class Monologue01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6110], visible=True) # Voice_Junta_00001770
        self.set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__15$', arg4=2, arg5=0) # 준타 00001770

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return Monologue02(self.ctx)


class Monologue02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=701, enable=True)
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_104')
        self.move_npc(spawnId=207, patrolName='MS2PatrolData_204')
        self.set_effect(triggerIds=[6111], visible=True) # Voice_Junta_00001771
        self.set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__16$', arg4=3, arg5=0) # 준타 00001771

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Monologue03(self.ctx)


class Monologue03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6006], visible=True) # Voice_Tinchai_00001720
        self.set_conversation(type=1, spawnId=207, script='$63000025_CS__TRAINING01__17$', arg4=3, arg5=0) # 틴차이 00001720

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Monologue04(self.ctx)


class Monologue04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=702, enable=True)
        self.set_effect(triggerIds=[6112], visible=True) # Voice_Junta_00001772
        self.set_conversation(type=1, spawnId=107, script='$63000025_CS__TRAINING01__18$', arg4=2, arg5=0) # 준타 00001772

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2200):
            return NpcLeave01(self.ctx)


class NpcLeave01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.destroy_monster(spawnIds=[107])
        self.move_user(mapId=63000025, portalId=40, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return NpcLeave02(self.ctx)


class NpcLeave02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[207])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GuideNextMap01(self.ctx)


class NpcLeave_CSkip(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[107])
        self.destroy_monster(spawnIds=[207])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=702, enable=False)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10020012, textId=10020012) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5400], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5401], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5402], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5403], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5404], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5405], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5406], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5407], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5408], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5409], visible=True) # 포털 경로 안내
        self.set_effect(triggerIds=[5410], visible=True) # 포털 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10020012)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.hide_guide_summary(entityId=1060)
        self.set_effect(triggerIds=[5400], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5408], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5409], visible=False) # 포털 경로 안내
        self.set_effect(triggerIds=[5410], visible=False) # 포털 경로 안내


initial_state = Wait
