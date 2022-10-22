""" trigger/63000030_cs/flyingcloud01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # DownArrow
        set_effect(triggerIds=[5200], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5300], visible=False) # FlyingCloud
        set_effect(triggerIds=[5400], visible=False) # ShadowApp
        set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001689
        set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001690
        set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001691
        set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001692
        set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001694
        set_effect(triggerIds=[6005], visible=False) # Voice_Tinchai_00001695
        set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001820
        set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001780
        set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001781
        set_effect(triggerIds=[6103], visible=False) # Voice_Junta_00001782
        set_effect(triggerIds=[6104], visible=False) # Voice_Junta_00001783
        set_effect(triggerIds=[6105], visible=False) # Voice_Junta_00001792
        set_effect(triggerIds=[6106], visible=False) # Voice_Junta_00001798
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_interact_object(triggerIds=[10001010], state=0) # FlyingCloud
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Bounding

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[1]):
            return QuestOnGiong21()
        if quest_user_detected(boxIds=[9000], questIds=[90000454], questStates=[3]):
            return QuestOnGiong11()
        if quest_user_detected(boxIds=[9000], questIds=[90000454], questStates=[2]):
            return QuestOnGiong01()
        if quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[3]):
            return Delay01()
        if wait_tick(waitTick=3000):
            return Quit()


#  하산 퀘스트 수락한 상태 
class QuestOnGiong21(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        create_monster(spawnIds=[104,204], arg2=False)
        move_user(mapId=63000030, portalId=11, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestOnGiong22()


class QuestOnGiong22(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PatrolWhileTalking03()


#  여정의 명분 퀘스트 완료 상태 
class QuestOnGiong11(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        create_monster(spawnIds=[103,203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestOnGiong12()


class QuestOnGiong12(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SecondQuestStart01()


#  여정의 명분 퀘스트 완료 가능 상태 
class QuestOnGiong01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        create_monster(spawnIds=[103,203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestOnGiong02()


class QuestOnGiong02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FirstQuestStart01()


#  최초 진입 
class Delay01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[920,921,922,923,924,925,926,927,928,929,930,931], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LookAround03()


class LookAround03(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=LookAround07_CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround04()


class LookAround04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000030_CS__FLYINGCLOUD01__0$', arg4=2, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround05()


class LookAround05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001820
        set_conversation(type=1, spawnId=201, script='$63000030_CS__FLYINGCLOUD01__1$', arg4=2, arg5=0) # 준타 00001820
        move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        move_npc(spawnId=931, patrolName='MS2PatrolData_931')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround06()


class LookAround06(state.State):
    def on_enter(self):
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround07()


class LookAround07_CSkip(state.State):
    def on_enter(self):
        move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        move_npc(spawnId=930, patrolName='MS2PatrolData_930')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LookAround07()


class LookAround07(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202], arg2=False)
        select_camera(triggerId=500, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleStart01()


class BattleStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10037010, textId=10037010) # 가이드 : 검은 그림자 무리 처치하기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[920,921,922,923,924,925,926,927,928,929,930,931]):
            return BattleEnd01()

    def on_exit(self):
        hide_guide_summary(entityId=10037010)


class BattleEnd01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleEnd02()


class BattleEnd02(state.State):
    def on_enter(self):
        move_user(mapId=63000030, portalId=10, boxId=9900)
        destroy_monster(spawnIds=[102,202])
        create_monster(spawnIds=[103,203], arg2=False)
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleEnd03()


class BattleEnd03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=DialogueSkip10, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Dialogue01()


#  시네마틱 대화 연출 
class Dialogue01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001780
        set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__2$', arg4=7) # 준타 00001780

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return DialogueSkip01()


class DialogueSkip01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001689
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__3$', arg4=6) # 틴차이 00001689

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DialogueSkip02()


class DialogueSkip02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001690
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__4$', arg4=6) # 틴차이 00001690

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DialogueSkip03()


class DialogueSkip03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue04()


class Dialogue04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001781
        set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__5$', arg4=6) # 준타 00001781

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DialogueSkip04()


class DialogueSkip04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue05()


class Dialogue05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001691
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__6$', arg4=6) # 틴차이 00001691

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return DialogueSkip05()


class DialogueSkip05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue06()


class Dialogue06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001692
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__7$', arg4=6) # 틴차이 00001692

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DialogueSkip06()


class DialogueSkip06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue07()


class Dialogue07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6103], visible=True) # Voice_Junta_00001782
        set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__8$', arg4=5) # 준타 00001782

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DialogueSkip07()


class DialogueSkip07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue08()


class Dialogue08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__9$', arg4=4) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return DialogueSkip08()


class DialogueSkip08(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue09()


class Dialogue09(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6104], visible=True) # Voice_Junta_00001783
        set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__10$', arg4=8) # 준타 00001783

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return DialogueSkip09()


class DialogueSkip09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue10()


class Dialogue10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001694
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__11$', arg4=5) # 틴차이 00001694
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DialogueSkip10()


class DialogueSkip10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        select_camera(triggerId=501, enable=False)
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FirstQuestStart01()


class FirstQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10030160, textId=10030160) # 가이드 : [[icon:questaccept]] 틴차이와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000454], questStates=[2]):
            return FirstQuestEnd01()

    def on_exit(self):
        hide_guide_summary(entityId=10030160)


class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000454], questStates=[3]):
            return SecondQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10031010)


class SecondQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000455], questStates=[1]):
            return PatrolWhileTalking01()

    def on_exit(self):
        hide_guide_summary(entityId=10031020)


class PatrolWhileTalking01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PatrolWhileTalking02()


class PatrolWhileTalking02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103,203])
        create_monster(spawnIds=[104,204], arg2=False)
        move_user(mapId=63000030, portalId=11, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PatrolWhileTalking03()


class PatrolWhileTalking03(state.State):
    def on_enter(self):
        set_scene_skip(state=FightBack01, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=104, patrolName='MS2PatrolData_103')
        move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolWhileTalking04()


class PatrolWhileTalking04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__12$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__13$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PatrolWhileTalking05()


class PatrolWhileTalking05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__14$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__15$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__16$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return ShadowApp01()


class ShadowApp01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=True) # ShadowApp
        create_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949], arg2=False)
        select_camera(triggerId=600, enable=True)
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowApp02()


class ShadowApp02(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_104')
        set_effect(triggerIds=[6105], visible=True) # Voice_Junta_00001792
        set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__17$', arg4=2, arg5=0) # 준타 00001792

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return ShadowApp03()


class ShadowApp03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowApp04()


class ShadowApp04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__18$', arg4=2, arg5=0)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShadowApp05()


class ShadowApp05(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FightBack01()


class FightBack01(state.State):
    def on_enter(self):
        move_npc(spawnId=204, patrolName='MS2PatrolData_205')
        set_effect(triggerIds=[6106], visible=True) # Voice_Junta_00001798
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__19$', arg4=4) # 준타 00001798

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FightBack02()


class FightBack02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FightBack03()


class FightBack03(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_105')
        set_effect(triggerIds=[6005], visible=True) # Voice_Tinchai_00001695
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__20$', arg4=5) # 틴차이 00001695

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FightBack04()


class FightBack04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[5400], visible=False) # ShadowApp

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FightBack05()


class FightBack05(state.State):
    def on_enter(self):
        move_user(mapId=63000030, portalId=20, boxId=9900)
        destroy_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949])
        create_monster(spawnIds=[910,911,912,913,914,915,916,917,918,919], arg2=False)
        destroy_monster(spawnIds=[104,204])
        create_monster(spawnIds=[105,205], arg2=False)
        select_camera(triggerId=602, enable=True)
        set_user_value(triggerId=3, key='SafetyStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return FightBack06()


class FightBack06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_user_value(triggerId=2, key='PushStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GotoTria01()


#  암벽등반 가이드 ClimbingGuide01 
class GotoTria01(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=False)
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5201], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5202], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5204], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5205], visible=True) # 구름터 경로 안내
        set_effect(triggerIds=[5100], visible=True) # DownArrow
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10037020, textId=10037020) # 가이드 : 트라이아행 구름에 가까이 가기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return GotoTria02()

    def on_exit(self):
        hide_guide_summary(entityId=10037020)


class GotoTria02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10037030, textId=10037030) # 가이드 : 트라이아행 구름에 타기
        set_interact_object(triggerIds=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001010], arg2=0):
            return TakeOffFlyingCloud01()

    def on_exit(self):
        hide_guide_summary(entityId=10037030)
        set_effect(triggerIds=[5100], visible=False) # DownArrow
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 구름터 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 구름터 경로 안내


class TakeOffFlyingCloud01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_visible_breakable_object(triggerIds=[4000], arg2=True)
        set_breakable(triggerIds=[4000], enabled=True)
        set_interact_object(triggerIds=[10001010], state=2) # FlyingCloud 숨기기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TakeOffFlyingCloud02()


class TakeOffFlyingCloud02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # FlyingCloud
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Bounding
        move_user(mapId=63000030, portalId=30, boxId=9900)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TakeOffFlyingCloud03()


class TakeOffFlyingCloud03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TakeOffFlyingCloud04()


class TakeOffFlyingCloud04(state.State):
    def on_enter(self):
        move_user(mapId=63000036, portalId=1)
        select_camera(triggerId=701, enable=False)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


