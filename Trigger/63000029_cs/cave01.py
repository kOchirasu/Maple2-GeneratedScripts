""" trigger/63000029_cs/cave01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5003], visible=False) # BlockApp 사운드 이펙트
        set_effect(triggerIds=[5004], visible=False) # EnteranceExplosion Vibrate 사운드 이펙트
        set_effect(triggerIds=[5005], visible=False) # GroundSplit Vibrate 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # LiftableTargetBox
        set_effect(triggerIds=[5200], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5201], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5202], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5203], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5300], visible=False) # DownArrow
        set_effect(triggerIds=[5400], visible=False) # RockDeris_Enterance
        set_effect(triggerIds=[5500], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5501], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5502], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5503], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5504], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5505], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5506], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5507], visible=False) # Dust_Enterance
        set_effect(triggerIds=[5700], visible=False) # Dust_Split
        set_effect(triggerIds=[5701], visible=False) # Dust_Split
        set_effect(triggerIds=[5702], visible=False) # Dust_Split
        set_effect(triggerIds=[5703], visible=False) # Dust_Split
        set_effect(triggerIds=[5704], visible=False) # Dust_Split
        set_effect(triggerIds=[5705], visible=False) # Dust_Split
        set_effect(triggerIds=[5706], visible=False) # Dust_Split
        set_effect(triggerIds=[5707], visible=False) # Dust_Split
        set_effect(triggerIds=[5708], visible=False) # Dust_Split
        set_effect(triggerIds=[5709], visible=False) # Dust_Split
        set_effect(triggerIds=[5600], visible=False) # SandStormSmall_GroundCollapse
        set_effect(triggerIds=[5800], visible=False) # Rumble
        set_effect(triggerIds=[5801], visible=False) # Earthquake
        set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion
        set_effect(triggerIds=[5900], visible=False) # StoneGate
        set_effect(triggerIds=[5901], visible=False) # ShadowApp
        set_effect(triggerIds=[5920], visible=False) # Sound_LaozExplosionRumble
        set_effect(triggerIds=[5921], visible=False) # Voice_LaozBattle_Attack_00001875
        set_effect(triggerIds=[5922], visible=False) # Voice_LaozBattle_Attack_00001874
        set_effect(triggerIds=[5930], visible=False) # Sound_LaozVsKandura_FightBlending
        set_effect(triggerIds=[5931], visible=False) # Sound_LaozVsKandura_FightExplosion
        set_effect(triggerIds=[6000], visible=False) # Voice_Laoz_00001847
        set_effect(triggerIds=[6001], visible=False) # Voice_Laoz_00001822
        set_effect(triggerIds=[6002], visible=False) # Voice_Laoz_00001823
        set_effect(triggerIds=[6003], visible=False) # Voice_Laoz_00001824
        set_effect(triggerIds=[6004], visible=False) # Voice_Laoz_00001825
        set_effect(triggerIds=[6005], visible=False) # Voice_Laoz_00001826
        set_effect(triggerIds=[6006], visible=False) # Voice_Laoz_00001827
        set_effect(triggerIds=[6007], visible=False) # Voice_Laoz_00001828
        set_effect(triggerIds=[6008], visible=False) # Voice_Laoz_00001829
        set_effect(triggerIds=[6009], visible=False) # Voice_Laoz_00001831
        set_effect(triggerIds=[6010], visible=False) # Voice_Laoz_00001834
        set_effect(triggerIds=[6100], visible=False) # Voice_Kandura_00001855
        set_effect(triggerIds=[6101], visible=False) # Voice_Kandura_00001856
        set_effect(triggerIds=[6102], visible=False) # Voice_Kandura_00001857
        set_effect(triggerIds=[6103], visible=False) # Voice_Kandura_00001858
        set_effect(triggerIds=[6104], visible=False) # Voice_Kandura_00001859
        set_effect(triggerIds=[6105], visible=False) # Voice_Kandura_00001860
        set_effect(triggerIds=[6106], visible=False) # Voice_Kandura_00001861
        set_effect(triggerIds=[6107], visible=False) # Voice_Kandura_00001862
        set_effect(triggerIds=[6200], visible=False) # Voice_Junta_00001779
        set_effect(triggerIds=[6201], visible=False) # Voice_Junta_00001770
        set_effect(triggerIds=[6300], visible=False) # Voice_Tinchai_00001688
        set_effect(triggerIds=[6301], visible=False) # Voice_Tinchai_00001717
        set_effect(triggerIds=[6400], visible=False) # Voice_JuntaNTinchai_00001873
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_EnteranceBlock
        set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_SplitBlock
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_StoneGate
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=False, arg3=0, arg4=0, arg5=0) # MeshGroup01_Block
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], visible=True, arg3=0, arg4=0, arg5=0) # MeshGroup03_SplitTop
        set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0) # MeshGroup04_SplitSide
        set_actor(triggerId=4500, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509], visible=False, arg3=0, arg4=0, arg5=0) # CollapseStart
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
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        set_agent(triggerIds=[8016], visible=False)
        set_agent(triggerIds=[8017], visible=False)
        set_agent(triggerIds=[8018], visible=False)
        set_agent(triggerIds=[8019], visible=False)
        set_agent(triggerIds=[8020], visible=False)
        set_agent(triggerIds=[8021], visible=False)
        set_agent(triggerIds=[8022], visible=False)
        set_agent(triggerIds=[8023], visible=False)
        set_agent(triggerIds=[8024], visible=False)
        set_agent(triggerIds=[8025], visible=False)
        set_agent(triggerIds=[8026], visible=False)
        set_agent(triggerIds=[8027], visible=False)
        create_monster(spawnIds=[101,201], arg2=False)
        set_skill(triggerIds=[7000], isEnable=False) # 바닥 큐브 부수기 스킬
        set_skill(triggerIds=[7001], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[7002], isEnable=False) # 그림자 소멸 스킬
        set_skill(triggerIds=[7003], isEnable=False) # 천장 부수기 스킬
        set_skill(triggerIds=[7100], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7101], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7102], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7103], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7104], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7105], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7106], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7107], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7108], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_skill(triggerIds=[7109], isEnable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        set_breakable(triggerIds=[4000], enabled=False)
        set_breakable(triggerIds=[4001], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        set_visible_breakable_object(triggerIds=[4001], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[3]):
            return QuestOnGiong11()
        if quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[2]):
            return QuestOnGiong01()
        if quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[1]):
            return LiftRock01()
        if quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[3]):
            return SecondQuestStart01()
        if quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[2]):
            return FirstQuestEnd01()


#  무나크라의 계시 퀘스트 완료 상태  
class QuestOnGiong11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGiong12()


class QuestOnGiong12(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=30, boxId=9900)
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[110,210,302], arg2=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_EnteranceBlock
        set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=0, delay=0) # MeshGroup01_Block

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGiong13()


class QuestOnGiong13(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Delay01()


#  무나크라의 계시 퀘스트 완료 가능 상태  
class QuestOnGiong01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGiong02()


class QuestOnGiong02(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=20, boxId=9900)
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202], arg2=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_EnteranceBlock
        set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=0, delay=0) # MeshGroup01_Block

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return QuestOnGiong03()


class QuestOnGiong03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__0$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOnGiong04()


class QuestOnGiong04(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        move_npc(spawnId=202, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LaozApp01()


#  최초 입장 
class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10030100, textId=10030100) # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000452], questStates=[3]):
            return SecondQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10030100)


class SecondQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000453], questStates=[1]):
            return LiftRock01()

    def on_exit(self):
        hide_guide_summary(entityId=10031020)


#  바위로 동굴 입구 막기 
class LiftRock01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10036010, textId=10036010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기
        set_effect(triggerIds=[5300], visible=True) # DownArrow
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트

    def on_tick(self) -> state.State:
        if not detect_liftable_object(boxIds=[9001], itemId=30000441):
            return LiftRock02()

    def on_exit(self):
        hide_guide_summary(entityId=10036010)


class LiftRock02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=False) # DownArrow
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10036011, textId=10036011) # 가이드 : 스페이스 키로 방위덩이 내려놔 동굴 입구 막기
        set_effect(triggerIds=[5100], visible=True) # LiftableTargetBox
        set_effect(triggerIds=[5200], visible=True) # LiftableTargetGuide
        set_effect(triggerIds=[5201], visible=True) # LiftableTargetGuide
        set_effect(triggerIds=[5202], visible=True) # LiftableTargetGuide
        set_effect(triggerIds=[5203], visible=True) # LiftableTargetGuide

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9002], itemId=30000441):
            return LiftRock03()

    def on_exit(self):
        hide_guide_summary(entityId=10036011)


class LiftRock03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # LiftableTargetBox
        set_effect(triggerIds=[5200], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5201], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5202], visible=False) # LiftableTargetGuide
        set_effect(triggerIds=[5203], visible=False) # LiftableTargetGuide

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return EnteranceBlock01()


class EnteranceBlock01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return EnteranceBlock02()


class EnteranceBlock02(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=10, boxId=9900)
        select_camera(triggerId=500, enable=True)
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return EnteranceBlock03()


class EnteranceBlock03(state.State):
    def on_enter(self):
        set_scene_skip(state=LaozApp05_CSkip, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5003], visible=True) # BlockApp 사운드 이펙트
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_EnteranceBlock
        set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=100, delay=100) # MeshGroup01_Block

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TimeToMoveIn01()


class TimeToMoveIn01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TimeToMoveIn02()


class TimeToMoveIn02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TimeToMoveIn03()


class TimeToMoveIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__2$', arg4=2, arg5=0)
        move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        move_npc(spawnId=202, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LaozApp01()


class LaozApp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[301], arg2=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        set_effect(triggerIds=[6400], visible=True) # Voice_JuntaNTinchai_00001873
        set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__3$', arg4=2, arg5=0) # Voice 둘이 함께 00001873
        set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__4$', arg4=2, arg5=0)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LaozApp02()


class LaozApp02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return LaozApp03()


class LaozApp03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return LaozApp04()


class LaozApp04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__5$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__6$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozApp05()


class LaozApp05_CSkip(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=10, boxId=9900)
        destroy_monster(spawnIds=[101,201])
        move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        move_npc(spawnId=202, patrolName='MS2PatrolData_201')
        create_monster(spawnIds=[301], arg2=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LaozTalk01()


class LaozApp05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LaozTalk01()


class LaozTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Laoz_00001847
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__7$', arg4=5) # 라오즈 00001847
        set_skip(state=LaozTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LaozTalk02()


class LaozTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozTalk03()


class LaozTalk03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__8$', arg4=4) # 라오즈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozTalk04()


class LaozTalk04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        destroy_monster(spawnIds=[301])
        create_monster(spawnIds=[302], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=601, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetLaoz01()


class MeetLaoz01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10036020, textId=10036020) # 가이드 : 라오즈에게 가까이 가기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return SecondQuestEnd01()

    def on_exit(self):
        hide_guide_summary(entityId=10036020)


class SecondQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10036030, textId=10036030) # 가이드 : [[icon:questcomplete]] 라오즈와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000453], questStates=[3]):
            return Delay01()

    def on_exit(self):
        hide_guide_summary(entityId=10036030)


class Delay01(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='SafetyStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Delay02()


class Delay02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # EnteranceExplosion 사운드 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return EnteranceBlockExplosion01()


class EnteranceBlockExplosion01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_scene_skip(state=LaozNKahnTalk18_CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return EnteranceBlockExplosion02()


class EnteranceBlockExplosion02(state.State):
    def on_enter(self):
        move_user(mapId=63000029, portalId=11, boxId=9900)
        select_camera(triggerId=610, enable=True)
        destroy_monster(spawnIds=[102,202,302,110,210])
        create_monster(spawnIds=[103,203,303], arg2=False)
        set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=False, meshCount=9, arg4=100, delay=100) # MeshGroup01_Block

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return EnteranceBlockExplosion03()


class EnteranceBlockExplosion03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5400], visible=True) # RockDeris_Enterance
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_EnteranceBlock
        set_skill(triggerIds=[7001], isEnable=True) # 입구 큐브 부수기 스킬
        create_monster(spawnIds=[401], arg2=False)
        move_npc(spawnId=401, patrolName='MS2PatrolData_401')
        set_effect(triggerIds=[5500], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5501], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5502], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5503], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5504], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5505], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5506], visible=True) # Dust_Enterance
        set_effect(triggerIds=[5507], visible=True) # Dust_Enterance

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KahnWalkIn01()


class KahnWalkIn01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5901], visible=True) # ShadowApp
        set_effect(triggerIds=[6100], visible=True) # Voice_Kandura_00001855
        set_conversation(type=1, spawnId=401, script='$63000029_CS__CAVE01__9$', arg4=3, arg5=0) # 칸두라 00001855
        create_monster(spawnIds=[900,901,902,903], arg2=False)
        move_npc(spawnId=900, patrolName='MS2PatrolData_900')
        move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        move_npc(spawnId=903, patrolName='MS2PatrolData_903')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return KahnWalkIn02()


class KahnWalkIn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[904,905,906], arg2=False)
        move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        move_npc(spawnId=905, patrolName='MS2PatrolData_905')
        move_npc(spawnId=906, patrolName='MS2PatrolData_906')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return KahnWalkIn03()


class KahnWalkIn03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[907,908,909], arg2=False)
        move_npc(spawnId=907, patrolName='MS2PatrolData_907')
        move_npc(spawnId=908, patrolName='MS2PatrolData_908')
        move_npc(spawnId=909, patrolName='MS2PatrolData_909')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return KahnWalkIn04()


class KahnWalkIn04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[940,941,942,943], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KahnWalkIn05()


class KahnWalkIn05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[920,921,922,923,924,925,926,927,928,929,930,931], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KahnWalkIn06()


class KahnWalkIn06(state.State):
    def on_enter(self):
        select_camera(triggerId=611, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KahnWalkIn07()


class KahnWalkIn07(state.State):
    def on_enter(self):
        move_npc(spawnId=303, patrolName='MS2PatrolData_302')
        set_effect(triggerIds=[6001], visible=True) # Voice_Laoz_00001822
        set_conversation(type=1, spawnId=303, script='$63000029_CS__CAVE01__10$', arg4=3, arg5=0) # 라오즈 00001822

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToFight01()


class ReadyToFight01(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=203, script='$63000029_CS__CAVE01__11$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ReadyToFight02()


class ReadyToFight02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        set_conversation(type=1, spawnId=103, script='$63000029_CS__CAVE01__12$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ReadyToFight03()


class ReadyToFight03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=90000)
        set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=90000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MeetKahn01()


class MeetKahn01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6101], visible=True) # Voice_Kandura_00001856
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__13$', arg4=9) # 칸두라 00001856
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return MeetKahn02()


class MeetKahn02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return MeetKahn03()


class MeetKahn03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Voice_Laoz_00001823
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__14$', arg4=4) # 라오즈 00001823
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MeetKahn04()


class MeetKahn04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=620, enable=True)

    def on_tick(self) -> state.State:
        if true():
            return LaozTalkToJuntaNTinChai01()


class LaozTalkToJuntaNTinChai01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Voice_Laoz_00001824
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__15$', arg4=8) # 라오즈 00001824
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return LaozTalkToJuntaNTinChai02()


class LaozTalkToJuntaNTinChai02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozTalkToJuntaNTinChai03()


class LaozTalkToJuntaNTinChai03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$63000029_CS__CAVE01__16$', arg4=4) # 준타
        set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai04()


class LaozTalkToJuntaNTinChai04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozTalkToJuntaNTinChai05()


class LaozTalkToJuntaNTinChai05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$63000029_CS__CAVE01__17$', arg4=4) # 틴차이
        set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai06()


class LaozTalkToJuntaNTinChai06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozTalkToJuntaNTinChai07()


class LaozTalkToJuntaNTinChai07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Laoz_00001847
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__18$', arg4=4) # 라오즈 00001847
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai08()


class LaozTalkToJuntaNTinChai08(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=611, enable=True)
        create_monster(spawnIds=[945,946], arg2=False)
        move_npc(spawnId=401, patrolName='MS2PatrolData_402')
        move_npc(spawnId=900, patrolName='MS2PatrolData_910')
        move_npc(spawnId=901, patrolName='MS2PatrolData_911')
        move_npc(spawnId=902, patrolName='MS2PatrolData_912')
        move_npc(spawnId=903, patrolName='MS2PatrolData_913')
        move_npc(spawnId=904, patrolName='MS2PatrolData_914')
        move_npc(spawnId=905, patrolName='MS2PatrolData_915')
        move_npc(spawnId=906, patrolName='MS2PatrolData_916')
        move_npc(spawnId=907, patrolName='MS2PatrolData_917')
        move_npc(spawnId=908, patrolName='MS2PatrolData_918')
        move_npc(spawnId=909, patrolName='MS2PatrolData_919')
        move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        move_npc(spawnId=943, patrolName='MS2PatrolData_943')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LaozNKahnTalk01()


class LaozNKahnTalk01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[947,948,949], arg2=False)
        move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        move_npc(spawnId=946, patrolName='MS2PatrolData_946')
        create_monster(spawnIds=[950,951,952,953,954,955,956,957,958,959], arg2=False)
        move_npc(spawnId=950, patrolName='MS2PatrolData_900')
        move_npc(spawnId=951, patrolName='MS2PatrolData_901')
        move_npc(spawnId=952, patrolName='MS2PatrolData_902')
        move_npc(spawnId=953, patrolName='MS2PatrolData_903')
        move_npc(spawnId=954, patrolName='MS2PatrolData_904')
        move_npc(spawnId=955, patrolName='MS2PatrolData_905')
        move_npc(spawnId=956, patrolName='MS2PatrolData_906')
        move_npc(spawnId=957, patrolName='MS2PatrolData_907')
        move_npc(spawnId=958, patrolName='MS2PatrolData_908')
        move_npc(spawnId=959, patrolName='MS2PatrolData_909')
        set_effect(triggerIds=[6004], visible=True) # Voice_Laoz_00001825
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__19$', arg4=9) # 라오즈 00001825
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        select_camera(triggerId=612, enable=True)
        set_skip(state=LaozNKahnTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return LaozNKahnTalk02()


class LaozNKahnTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return LaozNKahnTalk03()


class LaozNKahnTalk03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        set_effect(triggerIds=[6102], visible=True) # Voice_Kandura_00001857
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__20$', arg4=9) # 칸두라 00001857

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return LaozNKahnTalk04()


class LaozNKahnTalk04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozNKahnTalk05()


class LaozNKahnTalk05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        set_effect(triggerIds=[6103], visible=True) # Voice_Kandura_00001858
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__21$', arg4=6) # 칸두라 00001858
        set_skip(state=LaozNKahnTalk06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LaozNKahnTalk06()


class LaozNKahnTalk06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozNKahnTalk07()


class LaozNKahnTalk07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        set_effect(triggerIds=[6005], visible=True) # Voice_Laoz_00001826
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__22$', arg4=7) # 라오즈 00001826

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LaozNKahnTalk08()


class LaozNKahnTalk08(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozNKahnTalk09()


class LaozNKahnTalk09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        set_effect(triggerIds=[6006], visible=True) # Voice_Laoz_00001827
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__23$', arg4=7) # 라오즈 00001827

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LaozNKahnTalk10()


class LaozNKahnTalk10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozNKahnTalk11()


class LaozNKahnTalk11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        set_effect(triggerIds=[6104], visible=True) # Voice_Kandura_00001859
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__24$', arg4=7) # 칸두라 00001859

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LaozNKahnTalk12()


class LaozNKahnTalk12(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozNKahnTalk13()


class LaozNKahnTalk13(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        set_effect(triggerIds=[6007], visible=True) # Voice_Laoz_00001828
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__25$', arg4=8) # 라오즈 00001828

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return LaozNKahnTalk14()


class LaozNKahnTalk14(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozNKahnTalk15()


class LaozNKahnTalk15(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6105], visible=True) # Voice_Kandura_00001860
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__26$', arg4=7) # 칸두라 00001860
        select_camera(triggerId=621, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return LaozNKahnTalk16()


class LaozNKahnTalk16(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return LaozNKahnTalk17()


class LaozNKahnTalk17(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6106], visible=True) # Voice_Kandura_00001861
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__27$', arg4=4) # 칸두라 00001861
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LaozNKahnTalk18()


class LaozNKahnTalk18_CSkip(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,202,302,110,210])
        create_monster(spawnIds=[103,203,303], arg2=False)
        move_user(mapId=63000029, portalId=12, boxId=9900)
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleReady01()


class LaozNKahnTalk18(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return BattleReady01()


class BattleReady01(state.State):
    def on_enter(self):
        select_camera(triggerId=630, enable=True)
        move_user(mapId=63000029, portalId=12, boxId=9900)
        destroy_monster(spawnIds=[103,203,303,401])
        create_monster(spawnIds=[105,205,305,403], arg2=False)
        destroy_monster(spawnIds=[900,901,902,903,904,905,906,907,908,909,920,921,922,923,924,925,926,927,928,929,930,931,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959])
        create_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleReady02()

    def on_exit(self):
        set_npc_emotion_loop(spawnId=105, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=205, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=305, sequenceName='Attack_Idle_A', duration=15000)
        set_npc_emotion_loop(spawnId=403, sequenceName='Attack_Idle_A', duration=15000)


class BattleReady02(state.State):
    def on_enter(self):
        select_camera(triggerId=631, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LaozKillAll01()


class LaozKillAll01(state.State):
    def on_enter(self):
        move_npc(spawnId=305, patrolName='MS2PatrolData_303')
        set_conversation(type=1, spawnId=305, script='$63000029_CS__CAVE01__28$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LaozKillAll02()


class LaozKillAll02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5921], visible=True) # Voice_LaozBattle_Attack_00001875
        set_npc_emotion_sequence(spawnId=305, sequenceName='Attack_01_D') # 임시
        select_camera(triggerId=632, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return LaozKillAll03()


class LaozKillAll03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True) # GroundSplit Vibrate 사운드 이펙트
        set_skill(triggerIds=[7002], isEnable=True) # 그림자 소멸 스킬
        set_effect(triggerIds=[5920], visible=True) # Sound_LaozExplosionRumble

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return LaozSplitGround01()


class LaozSplitGround01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=305, sequenceName='Attack_01_B') # 임시

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LaozSplitGround02()


class LaozSplitGround02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5922], visible=True) # Voice_LaozBattle_Attack_00001874

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LaozSplitGround03()


class LaozSplitGround03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5901], visible=False) # ShadowApp
        set_effect(triggerIds=[5005], visible=True) # GroundSplit Vibrate 사운드 이펙트
        set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_SplitBlock
        set_random_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], visible=False, meshCount=36, arg4=0, delay=25) # MeshGroup03_SplitTop
        set_random_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=False, meshCount=17, arg4=0, delay=25) # MeshGroup04_SplitSide

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LaozSplitGround04()


class LaozSplitGround04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5700], visible=True) # Dust_Split
        set_effect(triggerIds=[5701], visible=True) # Dust_Split
        set_effect(triggerIds=[5702], visible=True) # Dust_Split
        set_effect(triggerIds=[5703], visible=True) # Dust_Split
        set_effect(triggerIds=[5704], visible=True) # Dust_Split
        set_effect(triggerIds=[5705], visible=True) # Dust_Split
        set_effect(triggerIds=[5706], visible=True) # Dust_Split
        set_effect(triggerIds=[5707], visible=True) # Dust_Split
        set_effect(triggerIds=[5708], visible=True) # Dust_Split
        set_effect(triggerIds=[5709], visible=True) # Dust_Split

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LeftBehind00()


class LeftBehind00(state.State):
    def on_enter(self):
        select_camera(triggerId=633, enable=True)
        set_scene_skip(state=Earthquake_CSkip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LeftBehind01()


class LeftBehind01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        set_effect(triggerIds=[6008], visible=True) # Voice_Laoz_00001829
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__29$', arg4=8) # 라오즈 00001829
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
        set_agent(triggerIds=[8013], visible=True)
        set_agent(triggerIds=[8014], visible=True)
        set_agent(triggerIds=[8015], visible=True)
        set_agent(triggerIds=[8016], visible=True)
        set_agent(triggerIds=[8017], visible=True)
        set_agent(triggerIds=[8018], visible=True)
        set_agent(triggerIds=[8019], visible=True)
        set_agent(triggerIds=[8020], visible=True)
        set_agent(triggerIds=[8021], visible=True)
        set_agent(triggerIds=[8022], visible=True)
        set_agent(triggerIds=[8023], visible=True)
        set_agent(triggerIds=[8024], visible=True)
        set_agent(triggerIds=[8025], visible=True)
        set_agent(triggerIds=[8026], visible=True)
        set_agent(triggerIds=[8027], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return LeftBehind02()


class LeftBehind02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LeftBehind03()


class LeftBehind03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        set_effect(triggerIds=[6200], visible=True) # Voice_Junta_00001779
        set_conversation(type=2, spawnId=11001557, script='$63000029_CS__CAVE01__30$', arg4=6) # 준타 00001779

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LeftBehind04()


class LeftBehind04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LeftBehind05()


class LeftBehind05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        set_effect(triggerIds=[6009], visible=True) # Voice_Laoz_00001831
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__31$', arg4=7) # 라오즈 00001831

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LeftBehind06()


class LeftBehind06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LeftBehind07()


class LeftBehind07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        set_conversation(type=2, spawnId=11001708, script='$63000029_CS__CAVE01__32$', arg4=4) # 틴차이 00001688

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LeftBehind08()


class LeftBehind08(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LeftBehind09()


class LeftBehind09(state.State):
    def on_enter(self):
        select_camera(triggerId=634, enable=True)
        set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        set_effect(triggerIds=[6107], visible=True) # Voice_Kandura_00001862
        set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__33$', arg4=6) # 칸두라 00001862

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LeftBehind10()


class LeftBehind10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LeftBehind11()


class LeftBehind11(state.State):
    def on_enter(self):
        select_camera(triggerId=635, enable=True)
        set_effect(triggerIds=[6010], visible=True) # Voice_Laoz_00001834
        set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__34$', arg4=5) # 라오즈 00001834

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LeftBehind12()


class LeftBehind12(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return LaozVersusKahnAttack01()


#  전투 연출 교전 
class LaozVersusKahnAttack01(state.State):
    def on_enter(self):
        move_npc(spawnId=305, patrolName='MS2PatrolData_304')
        move_npc(spawnId=403, patrolName='MS2PatrolData_403')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return LaozVersusKahnAttack02()


#  전투 연출 대치 
class LaozVersusKahnAttack02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozVersusKahnAttack03()


class LaozVersusKahnAttack03(state.State):
    def on_enter(self):
        select_camera(triggerId=651, enable=True) # zoomin
        set_effect(triggerIds=[5820], visible=True) # LaozVsKandura_FightBlending
        set_npc_emotion_loop(spawnId=305, sequenceName='Bore_B', duration=15000) # 라오즈
        set_npc_emotion_loop(spawnId=403, sequenceName='Attack_02_F', duration=15000) # 칸두라
        set_effect(triggerIds=[5930], visible=True) # Sound_LaozVsKandura_FightBlending

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return LaozVersusKahnCrash01()


class LaozVersusKahnCrash01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5600], visible=True) # SandStormSmall_GroundCollapse

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LaozVersusKahnCrash02()


class LaozVersusKahnCrash02(state.State):
    def on_enter(self):
        select_camera(triggerId=650, enable=True) # zoomout
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509], visible=True, arg3=0, arg4=0, arg5=0) # CollapseStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapaseStart01()


#  전투 연출 격돌 
class CollapaseStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5800], visible=True) # Rumble
        set_mesh(triggerIds=[3505], visible=False, arg3=0, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3509], visible=False, arg3=100, arg4=0, arg5=0) # CollapseStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapaseStart02()


class CollapaseStart02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3504], visible=False, arg3=0, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3501], visible=False, arg3=50, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3507], visible=False, arg3=100, arg4=0, arg5=0) # CollapseStart
        set_effect(triggerIds=[5931], visible=True) # Sound_LaozVsKandura_FightExplosion

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapaseStart03()


class CollapaseStart03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5821], visible=True) # LaozVsKandura_FightExplosion
        set_mesh(triggerIds=[3502], visible=False, arg3=0, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3508], visible=False, arg3=50, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3506], visible=False, arg3=100, arg4=0, arg5=0) # CollapseStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapaseStart04()


class CollapaseStart04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3503], visible=False, arg3=0, arg4=0, arg5=0) # CollapseStart
        set_mesh(triggerIds=[3500], visible=False, arg3=100, arg4=0, arg5=0) # CollapseStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapaseAbove01()


class CollapaseAbove01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7003], isEnable=True) # 천장 부수기 스킬
        set_effect(triggerIds=[5801], visible=True) # Earthquake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CollapaseGround01()


class CollapaseGround01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[305,403])
        set_breakable(triggerIds=[4000], enabled=True)
        set_breakable(triggerIds=[4001], enabled=True)
        set_visible_breakable_object(triggerIds=[4000], arg2=True)
        set_visible_breakable_object(triggerIds=[4001], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return CollapaseGround02()


class CollapaseGround02(state.State):
    def on_enter(self):
        set_scene_skip()
        set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion
        set_skill(triggerIds=[7000], isEnable=True) # 바닥 큐브 부수기 스킬
        set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__35$', arg4=3, arg5=0) # 틴차이 00001688

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return CollapaseGround03()


class CollapaseGround03(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False)
        set_breakable(triggerIds=[4001], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        set_visible_breakable_object(triggerIds=[4001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Earthquake01()


#  동굴이 무너질 것 같은 연출 
class Earthquake_CSkip(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7003], isEnable=True) # 천장 부수기 스킬
        set_effect(triggerIds=[5801], visible=True) # Earthquake
        set_breakable(triggerIds=[4000], enabled=True)
        set_breakable(triggerIds=[4001], enabled=True)
        set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Earthquake_CSkip2()


class Earthquake_CSkip2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True) # 바닥 큐브 부수기 스킬
        set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        set_visible_breakable_object(triggerIds=[4000], arg2=True)
        set_visible_breakable_object(triggerIds=[4001], arg2=True)
        set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__35$', arg4=3, arg5=0) # 틴차이 00001688
        destroy_monster(spawnIds=[305,403])
        set_breakable(triggerIds=[4000], enabled=False)
        set_breakable(triggerIds=[4001], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        set_visible_breakable_object(triggerIds=[4001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Earthquake01()


class Earthquake01(state.State):
    def on_enter(self):
        select_camera(triggerId=660, enable=True) # zoomout
        set_user_value(triggerId=2, key='EarthquakeStart', value=1)
        set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__39$', arg4=4, arg5=2) # 틴차이
        set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__40$', arg4=3, arg5=4) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Earthquake02()


class Earthquake02(state.State):
    def on_enter(self):
        select_camera(triggerId=640, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Earthquake03()


class Earthquake03(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_105')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Earthquake04()


class Earthquake04(state.State):
    def on_enter(self):
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        set_effect(triggerIds=[6301], visible=True) # Voice_Tinchai_00001717
        set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__36$', arg4=3, arg5=0) # 틴차이 00001717
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Earthquake05()


class Earthquake05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        set_effect(triggerIds=[6201], visible=True) # Voice_Junta_00001770
        set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__37$', arg4=4, arg5=0) # 준타 00001770
        set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TimeToLeave01()

    def on_exit(self):
        set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')


class TimeToLeave01(state.State):
    def on_enter(self):
        select_camera(triggerId=641, enable=True)
        move_npc(spawnId=205, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TimeToLeave02()


class TimeToLeave02(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TimeToLeave03()


class TimeToLeave03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=641, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideNextMap01()


class GuideNextMap01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10036040, textId=10036040) # 가이드 : 준타, 틴차이를 따라 동굴에서 빠져나가기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9004]):
            return GuideNextMap02()


class GuideNextMap02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5900], visible=True) # StoneGate
        set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__38$', arg4=3)
        hide_guide_summary(entityId=10036040)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return OpenTheStoneGate01()


class OpenTheStoneGate01(state.State):
    def on_enter(self):
        set_actor(triggerId=4500, visible=True, initialSequence='or_fi_struc_stonegate_A01_on') # StoneGate

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return OpenTheStoneGate02()


class OpenTheStoneGate02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MoveToNextMap01()


class MoveToNextMap01(state.State):
    def on_enter(self):
        move_npc(spawnId=205, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MoveToNextMap02()


class MoveToNextMap02(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_104')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return MoveToNextMap03()


class MoveToNextMap03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return MoveToNextMap04()


class MoveToNextMap04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[205])

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=1060)


