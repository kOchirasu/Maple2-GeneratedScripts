""" trigger/63000029_cs/cave01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5003], visible=False) # BlockApp 사운드 이펙트
        self.set_effect(triggerIds=[5004], visible=False) # EnteranceExplosion Vibrate 사운드 이펙트
        self.set_effect(triggerIds=[5005], visible=False) # GroundSplit Vibrate 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # LiftableTargetBox
        self.set_effect(triggerIds=[5200], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5201], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5202], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5203], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5300], visible=False) # DownArrow
        self.set_effect(triggerIds=[5400], visible=False) # RockDeris_Enterance
        self.set_effect(triggerIds=[5500], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5501], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5502], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5503], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5504], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5505], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5506], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5507], visible=False) # Dust_Enterance
        self.set_effect(triggerIds=[5700], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5701], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5702], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5703], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5704], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5705], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5706], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5707], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5708], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5709], visible=False) # Dust_Split
        self.set_effect(triggerIds=[5600], visible=False) # SandStormSmall_GroundCollapse
        self.set_effect(triggerIds=[5800], visible=False) # Rumble
        self.set_effect(triggerIds=[5801], visible=False) # Earthquake
        self.set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        self.set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion
        self.set_effect(triggerIds=[5900], visible=False) # StoneGate
        self.set_effect(triggerIds=[5901], visible=False) # ShadowApp
        self.set_effect(triggerIds=[5920], visible=False) # Sound_LaozExplosionRumble
        self.set_effect(triggerIds=[5921], visible=False) # Voice_LaozBattle_Attack_00001875
        self.set_effect(triggerIds=[5922], visible=False) # Voice_LaozBattle_Attack_00001874
        self.set_effect(triggerIds=[5930], visible=False) # Sound_LaozVsKandura_FightBlending
        self.set_effect(triggerIds=[5931], visible=False) # Sound_LaozVsKandura_FightExplosion
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Laoz_00001847
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Laoz_00001822
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Laoz_00001823
        self.set_effect(triggerIds=[6003], visible=False) # Voice_Laoz_00001824
        self.set_effect(triggerIds=[6004], visible=False) # Voice_Laoz_00001825
        self.set_effect(triggerIds=[6005], visible=False) # Voice_Laoz_00001826
        self.set_effect(triggerIds=[6006], visible=False) # Voice_Laoz_00001827
        self.set_effect(triggerIds=[6007], visible=False) # Voice_Laoz_00001828
        self.set_effect(triggerIds=[6008], visible=False) # Voice_Laoz_00001829
        self.set_effect(triggerIds=[6009], visible=False) # Voice_Laoz_00001831
        self.set_effect(triggerIds=[6010], visible=False) # Voice_Laoz_00001834
        self.set_effect(triggerIds=[6100], visible=False) # Voice_Kandura_00001855
        self.set_effect(triggerIds=[6101], visible=False) # Voice_Kandura_00001856
        self.set_effect(triggerIds=[6102], visible=False) # Voice_Kandura_00001857
        self.set_effect(triggerIds=[6103], visible=False) # Voice_Kandura_00001858
        self.set_effect(triggerIds=[6104], visible=False) # Voice_Kandura_00001859
        self.set_effect(triggerIds=[6105], visible=False) # Voice_Kandura_00001860
        self.set_effect(triggerIds=[6106], visible=False) # Voice_Kandura_00001861
        self.set_effect(triggerIds=[6107], visible=False) # Voice_Kandura_00001862
        self.set_effect(triggerIds=[6200], visible=False) # Voice_Junta_00001779
        self.set_effect(triggerIds=[6201], visible=False) # Voice_Junta_00001770
        self.set_effect(triggerIds=[6300], visible=False) # Voice_Tinchai_00001688
        self.set_effect(triggerIds=[6301], visible=False) # Voice_Tinchai_00001717
        self.set_effect(triggerIds=[6400], visible=False) # Voice_JuntaNTinchai_00001873
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_EnteranceBlock
        self.set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=0, delay=0, scale=0) # Invisible_SplitBlock
        self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0) # Invisible_StoneGate
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=False, arg3=0, delay=0, scale=0) # MeshGroup01_Block
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], visible=True, arg3=0, delay=0, scale=0) # MeshGroup03_SplitTop
        self.set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, delay=0, scale=0) # MeshGroup04_SplitSide
        self.set_actor(triggerId=4500, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509], visible=False, arg3=0, delay=0, scale=0) # CollapseStart
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_agent(triggerIds=[8014], visible=False)
        self.set_agent(triggerIds=[8015], visible=False)
        self.set_agent(triggerIds=[8016], visible=False)
        self.set_agent(triggerIds=[8017], visible=False)
        self.set_agent(triggerIds=[8018], visible=False)
        self.set_agent(triggerIds=[8019], visible=False)
        self.set_agent(triggerIds=[8020], visible=False)
        self.set_agent(triggerIds=[8021], visible=False)
        self.set_agent(triggerIds=[8022], visible=False)
        self.set_agent(triggerIds=[8023], visible=False)
        self.set_agent(triggerIds=[8024], visible=False)
        self.set_agent(triggerIds=[8025], visible=False)
        self.set_agent(triggerIds=[8026], visible=False)
        self.set_agent(triggerIds=[8027], visible=False)
        self.create_monster(spawnIds=[101,201], animationEffect=False)
        self.set_skill(triggerIds=[7000], enable=False) # 바닥 큐브 부수기 스킬
        self.set_skill(triggerIds=[7001], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[7002], enable=False) # 그림자 소멸 스킬
        self.set_skill(triggerIds=[7003], enable=False) # 천장 부수기 스킬
        self.set_skill(triggerIds=[7100], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7101], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7102], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7103], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7104], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7105], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7106], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7107], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7108], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_skill(triggerIds=[7109], enable=False) # 천장 큐브 한개씩 떨어트리기 스킬
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_breakable(triggerIds=[4001], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.set_visible_breakable_object(triggerIds=[4001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[3]):
            return QuestOnGiong11(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[2]):
            return QuestOnGiong01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[1]):
            return LiftRock01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[3]):
            return SecondQuestStart01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[2]):
            return FirstQuestEnd01(self.ctx)


# 무나크라의 계시 퀘스트 완료 상태
class QuestOnGiong11(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGiong12(self.ctx)


class QuestOnGiong12(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=30, boxId=9900)
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[110,210,302], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0) # Invisible_EnteranceBlock
        self.set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=0, delay=0) # MeshGroup01_Block

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGiong13(self.ctx)


class QuestOnGiong13(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Delay01(self.ctx)


# 무나크라의 계시 퀘스트 완료 가능 상태
class QuestOnGiong01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGiong02(self.ctx)


class QuestOnGiong02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=20, boxId=9900)
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0) # Invisible_EnteranceBlock
        self.set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=0, delay=0) # MeshGroup01_Block

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGiong03(self.ctx)


class QuestOnGiong03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__0$', arg4=3, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return QuestOnGiong04(self.ctx)


class QuestOnGiong04(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LaozApp01(self.ctx)


# 최초 입장
class FirstQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10030100, textId=10030100) # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000452], questStates=[3]):
            return SecondQuestStart01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10030100)


class SecondQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000453], questStates=[1]):
            return LiftRock01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10031020)


# 바위로 동굴 입구 막기
class LiftRock01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10036010, textId=10036010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기
        self.set_effect(triggerIds=[5300], visible=True) # DownArrow
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트

    def on_tick(self) -> common.Trigger:
        if not self.detect_liftable_object(boxIds=[9001], itemId=30000441):
            return LiftRock02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10036010)


class LiftRock02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=False) # DownArrow
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10036011, textId=10036011) # 가이드 : 스페이스 키로 방위덩이 내려놔 동굴 입구 막기
        self.set_effect(triggerIds=[5100], visible=True) # LiftableTargetBox
        self.set_effect(triggerIds=[5200], visible=True) # LiftableTargetGuide
        self.set_effect(triggerIds=[5201], visible=True) # LiftableTargetGuide
        self.set_effect(triggerIds=[5202], visible=True) # LiftableTargetGuide
        self.set_effect(triggerIds=[5203], visible=True) # LiftableTargetGuide

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9002], itemId=30000441):
            return LiftRock03(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10036011)


class LiftRock03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # LiftableTargetBox
        self.set_effect(triggerIds=[5200], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5201], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5202], visible=False) # LiftableTargetGuide
        self.set_effect(triggerIds=[5203], visible=False) # LiftableTargetGuide

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return EnteranceBlock01(self.ctx)


class EnteranceBlock01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return EnteranceBlock02(self.ctx)


class EnteranceBlock02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=10, boxId=9900)
        self.select_camera(triggerId=500, enable=True)
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return EnteranceBlock03(self.ctx)


class EnteranceBlock03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=LaozApp05_CSkip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5003], visible=True) # BlockApp 사운드 이펙트
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0) # Invisible_EnteranceBlock
        self.set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=True, meshCount=9, arg4=100, delay=100) # MeshGroup01_Block

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return TimeToMoveIn01(self.ctx)


class TimeToMoveIn01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TimeToMoveIn02(self.ctx)


class TimeToMoveIn02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__1$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return TimeToMoveIn03(self.ctx)


class TimeToMoveIn03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__2$', arg4=2, arg5=0)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LaozApp01(self.ctx)


class LaozApp01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        self.set_effect(triggerIds=[6400], visible=True) # Voice_JuntaNTinchai_00001873
        self.set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__3$', arg4=2, arg5=0) # Voice 둘이 함께 00001873
        self.set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__4$', arg4=2, arg5=0)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LaozApp02(self.ctx)


class LaozApp02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return LaozApp03(self.ctx)


class LaozApp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return LaozApp04(self.ctx)


class LaozApp04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=202, script='$63000029_CS__CAVE01__5$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=102, script='$63000029_CS__CAVE01__6$', arg4=3, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozApp05(self.ctx)


class LaozApp05_CSkip(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=10, boxId=9900)
        self.destroy_monster(spawnIds=[101,201])
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_201')
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LaozTalk01(self.ctx)


class LaozApp05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LaozTalk01(self.ctx)


class LaozTalk01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Laoz_00001847
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__7$', arg4=5) # 라오즈 00001847
        self.set_skip(state=LaozTalk04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LaozTalk02(self.ctx)


class LaozTalk02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozTalk03(self.ctx)


class LaozTalk03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__8$', arg4=4) # 라오즈

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozTalk04(self.ctx)


class LaozTalk04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[301])
        self.create_monster(spawnIds=[302], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=601, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetLaoz01(self.ctx)


class MeetLaoz01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10036020, textId=10036020) # 가이드 : 라오즈에게 가까이 가기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9003]):
            return SecondQuestEnd01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10036020)


class SecondQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10036030, textId=10036030) # 가이드 : [[icon:questcomplete]] 라오즈와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000453], questStates=[3]):
            return Delay01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10036030)


class Delay01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='SafetyStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Delay02(self.ctx)


class Delay02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5004], visible=True) # EnteranceExplosion 사운드 이펙트

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return EnteranceBlockExplosion01(self.ctx)


class EnteranceBlockExplosion01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=LaozNKahnTalk18_CSkip, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return EnteranceBlockExplosion02(self.ctx)


class EnteranceBlockExplosion02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=11, boxId=9900)
        self.select_camera(triggerId=610, enable=True)
        self.destroy_monster(spawnIds=[102,202,302,110,210])
        self.create_monster(spawnIds=[103,203,303], animationEffect=False)
        self.set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108], visible=False, meshCount=9, arg4=100, delay=100) # MeshGroup01_Block

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return EnteranceBlockExplosion03(self.ctx)


class EnteranceBlockExplosion03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5400], visible=True) # RockDeris_Enterance
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_EnteranceBlock
        self.set_skill(triggerIds=[7001], enable=True) # 입구 큐브 부수기 스킬
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_401')
        self.set_effect(triggerIds=[5500], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5501], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5502], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5503], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5504], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5505], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5506], visible=True) # Dust_Enterance
        self.set_effect(triggerIds=[5507], visible=True) # Dust_Enterance

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KahnWalkIn01(self.ctx)


class KahnWalkIn01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5901], visible=True) # ShadowApp
        self.set_effect(triggerIds=[6100], visible=True) # Voice_Kandura_00001855
        self.set_conversation(type=1, spawnId=401, script='$63000029_CS__CAVE01__9$', arg4=3, arg5=0) # 칸두라 00001855
        self.create_monster(spawnIds=[900,901,902,903], animationEffect=False)
        self.move_npc(spawnId=900, patrolName='MS2PatrolData_900')
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_903')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return KahnWalkIn02(self.ctx)


class KahnWalkIn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[904,905,906], animationEffect=False)
        self.move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        self.move_npc(spawnId=905, patrolName='MS2PatrolData_905')
        self.move_npc(spawnId=906, patrolName='MS2PatrolData_906')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return KahnWalkIn03(self.ctx)


class KahnWalkIn03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[907,908,909], animationEffect=False)
        self.move_npc(spawnId=907, patrolName='MS2PatrolData_907')
        self.move_npc(spawnId=908, patrolName='MS2PatrolData_908')
        self.move_npc(spawnId=909, patrolName='MS2PatrolData_909')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return KahnWalkIn04(self.ctx)


class KahnWalkIn04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[940,941,942,943], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KahnWalkIn05(self.ctx)


class KahnWalkIn05(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[920,921,922,923,924,925,926,927,928,929,930,931], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KahnWalkIn06(self.ctx)


class KahnWalkIn06(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=611, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KahnWalkIn07(self.ctx)


class KahnWalkIn07(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_302')
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Laoz_00001822
        self.set_conversation(type=1, spawnId=303, script='$63000029_CS__CAVE01__10$', arg4=3, arg5=0) # 라오즈 00001822

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToFight01(self.ctx)


class ReadyToFight01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=203, script='$63000029_CS__CAVE01__11$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ReadyToFight02(self.ctx)


class ReadyToFight02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.set_conversation(type=1, spawnId=103, script='$63000029_CS__CAVE01__12$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ReadyToFight03(self.ctx)


class ReadyToFight03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=90000)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=90000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return MeetKahn01(self.ctx)


class MeetKahn01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6101], visible=True) # Voice_Kandura_00001856
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__13$', arg4=9) # 칸두라 00001856
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return MeetKahn02(self.ctx)


class MeetKahn02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return MeetKahn03(self.ctx)


class MeetKahn03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Laoz_00001823
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__14$', arg4=4) # 라오즈 00001823
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return MeetKahn04(self.ctx)


class MeetKahn04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=620, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozTalkToJuntaNTinChai01(self.ctx)


class LaozTalkToJuntaNTinChai01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Voice_Laoz_00001824
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__15$', arg4=8) # 라오즈 00001824
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return LaozTalkToJuntaNTinChai02(self.ctx)


class LaozTalkToJuntaNTinChai02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozTalkToJuntaNTinChai03(self.ctx)


class LaozTalkToJuntaNTinChai03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$63000029_CS__CAVE01__16$', arg4=4) # 준타
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai04(self.ctx)


class LaozTalkToJuntaNTinChai04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozTalkToJuntaNTinChai05(self.ctx)


class LaozTalkToJuntaNTinChai05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$63000029_CS__CAVE01__17$', arg4=4) # 틴차이
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai06(self.ctx)


class LaozTalkToJuntaNTinChai06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozTalkToJuntaNTinChai07(self.ctx)


class LaozTalkToJuntaNTinChai07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Laoz_00001847
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__18$', arg4=4) # 라오즈 00001847
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozTalkToJuntaNTinChai08(self.ctx)


class LaozTalkToJuntaNTinChai08(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=611, enable=True)
        self.create_monster(spawnIds=[945,946], animationEffect=False)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_402')
        self.move_npc(spawnId=900, patrolName='MS2PatrolData_910')
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_911')
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_912')
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_913')
        self.move_npc(spawnId=904, patrolName='MS2PatrolData_914')
        self.move_npc(spawnId=905, patrolName='MS2PatrolData_915')
        self.move_npc(spawnId=906, patrolName='MS2PatrolData_916')
        self.move_npc(spawnId=907, patrolName='MS2PatrolData_917')
        self.move_npc(spawnId=908, patrolName='MS2PatrolData_918')
        self.move_npc(spawnId=909, patrolName='MS2PatrolData_919')
        self.move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        self.move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        self.move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        self.move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        self.move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        self.move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        self.move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        self.move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        self.move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        self.move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        self.move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        self.move_npc(spawnId=943, patrolName='MS2PatrolData_943')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LaozNKahnTalk01(self.ctx)


class LaozNKahnTalk01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[947,948,949], animationEffect=False)
        self.move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        self.move_npc(spawnId=946, patrolName='MS2PatrolData_946')
        self.create_monster(spawnIds=[950,951,952,953,954,955,956,957,958,959], animationEffect=False)
        self.move_npc(spawnId=950, patrolName='MS2PatrolData_900')
        self.move_npc(spawnId=951, patrolName='MS2PatrolData_901')
        self.move_npc(spawnId=952, patrolName='MS2PatrolData_902')
        self.move_npc(spawnId=953, patrolName='MS2PatrolData_903')
        self.move_npc(spawnId=954, patrolName='MS2PatrolData_904')
        self.move_npc(spawnId=955, patrolName='MS2PatrolData_905')
        self.move_npc(spawnId=956, patrolName='MS2PatrolData_906')
        self.move_npc(spawnId=957, patrolName='MS2PatrolData_907')
        self.move_npc(spawnId=958, patrolName='MS2PatrolData_908')
        self.move_npc(spawnId=959, patrolName='MS2PatrolData_909')
        self.set_effect(triggerIds=[6004], visible=True) # Voice_Laoz_00001825
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__19$', arg4=9) # 라오즈 00001825
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.select_camera(triggerId=612, enable=True)
        self.set_skip(state=LaozNKahnTalk02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return LaozNKahnTalk02(self.ctx)


class LaozNKahnTalk02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozNKahnTalk03(self.ctx)


class LaozNKahnTalk03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        self.set_effect(triggerIds=[6102], visible=True) # Voice_Kandura_00001857
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__20$', arg4=9) # 칸두라 00001857

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return LaozNKahnTalk04(self.ctx)


class LaozNKahnTalk04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozNKahnTalk05(self.ctx)


class LaozNKahnTalk05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        self.set_effect(triggerIds=[6103], visible=True) # Voice_Kandura_00001858
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__21$', arg4=6) # 칸두라 00001858
        self.set_skip(state=LaozNKahnTalk06)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LaozNKahnTalk06(self.ctx)


class LaozNKahnTalk06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozNKahnTalk07(self.ctx)


class LaozNKahnTalk07(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6005], visible=True) # Voice_Laoz_00001826
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__22$', arg4=7) # 라오즈 00001826

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LaozNKahnTalk08(self.ctx)


class LaozNKahnTalk08(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozNKahnTalk09(self.ctx)


class LaozNKahnTalk09(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6006], visible=True) # Voice_Laoz_00001827
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__23$', arg4=7) # 라오즈 00001827

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LaozNKahnTalk10(self.ctx)


class LaozNKahnTalk10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozNKahnTalk11(self.ctx)


class LaozNKahnTalk11(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        self.set_effect(triggerIds=[6104], visible=True) # Voice_Kandura_00001859
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__24$', arg4=7) # 칸두라 00001859

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LaozNKahnTalk12(self.ctx)


class LaozNKahnTalk12(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozNKahnTalk13(self.ctx)


class LaozNKahnTalk13(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6007], visible=True) # Voice_Laoz_00001828
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__25$', arg4=8) # 라오즈 00001828

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return LaozNKahnTalk14(self.ctx)


class LaozNKahnTalk14(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozNKahnTalk15(self.ctx)


class LaozNKahnTalk15(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6105], visible=True) # Voice_Kandura_00001860
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__26$', arg4=7) # 칸두라 00001860
        self.select_camera(triggerId=621, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return LaozNKahnTalk16(self.ctx)


class LaozNKahnTalk16(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozNKahnTalk17(self.ctx)


class LaozNKahnTalk17(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6106], visible=True) # Voice_Kandura_00001861
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__27$', arg4=4) # 칸두라 00001861
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LaozNKahnTalk18(self.ctx)


class LaozNKahnTalk18_CSkip(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102,202,302,110,210])
        self.create_monster(spawnIds=[103,203,303], animationEffect=False)
        self.move_user(mapId=63000029, portalId=12, boxId=9900)
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleReady01(self.ctx)


class LaozNKahnTalk18(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return BattleReady01(self.ctx)


class BattleReady01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=630, enable=True)
        self.move_user(mapId=63000029, portalId=12, boxId=9900)
        self.destroy_monster(spawnIds=[103,203,303,401])
        self.create_monster(spawnIds=[105,205,305,403], animationEffect=False)
        self.destroy_monster(spawnIds=[900,901,902,903,904,905,906,907,908,909,920,921,922,923,924,925,926,927,928,929,930,931,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959])
        self.create_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleReady02(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=205, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=305, sequenceName='Attack_Idle_A', duration=15000)
        self.set_npc_emotion_loop(spawnId=403, sequenceName='Attack_Idle_A', duration=15000)


class BattleReady02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=631, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return LaozKillAll01(self.ctx)


class LaozKillAll01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_303')
        self.set_conversation(type=1, spawnId=305, script='$63000029_CS__CAVE01__28$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LaozKillAll02(self.ctx)


class LaozKillAll02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5921], visible=True) # Voice_LaozBattle_Attack_00001875
        self.set_npc_emotion_sequence(spawnId=305, sequenceName='Attack_01_D') # 임시
        self.select_camera(triggerId=632, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return LaozKillAll03(self.ctx)


class LaozKillAll03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=True) # GroundSplit Vibrate 사운드 이펙트
        self.set_skill(triggerIds=[7002], enable=True) # 그림자 소멸 스킬
        self.set_effect(triggerIds=[5920], visible=True) # Sound_LaozExplosionRumble

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return LaozSplitGround01(self.ctx)


class LaozSplitGround01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=305, sequenceName='Attack_01_B') # 임시

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LaozSplitGround02(self.ctx)


class LaozSplitGround02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5922], visible=True) # Voice_LaozBattle_Attack_00001874

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LaozSplitGround03(self.ctx)


class LaozSplitGround03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5901], visible=False) # ShadowApp
        self.set_effect(triggerIds=[5005], visible=True) # GroundSplit Vibrate 사운드 이펙트
        self.set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, delay=0, scale=0) # Invisible_SplitBlock
        self.set_random_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335], visible=False, meshCount=36, arg4=0, delay=25) # MeshGroup03_SplitTop
        self.set_random_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=False, meshCount=17, arg4=0, delay=25) # MeshGroup04_SplitSide

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LaozSplitGround04(self.ctx)


class LaozSplitGround04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5700], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5701], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5702], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5703], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5704], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5705], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5706], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5707], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5708], visible=True) # Dust_Split
        self.set_effect(triggerIds=[5709], visible=True) # Dust_Split

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return LeftBehind00(self.ctx)


class LeftBehind00(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=633, enable=True)
        self.set_scene_skip(state=Earthquake_CSkip, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LeftBehind01(self.ctx)


class LeftBehind01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6008], visible=True) # Voice_Laoz_00001829
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__29$', arg4=8) # 라오즈 00001829
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)
        self.set_agent(triggerIds=[8012], visible=True)
        self.set_agent(triggerIds=[8013], visible=True)
        self.set_agent(triggerIds=[8014], visible=True)
        self.set_agent(triggerIds=[8015], visible=True)
        self.set_agent(triggerIds=[8016], visible=True)
        self.set_agent(triggerIds=[8017], visible=True)
        self.set_agent(triggerIds=[8018], visible=True)
        self.set_agent(triggerIds=[8019], visible=True)
        self.set_agent(triggerIds=[8020], visible=True)
        self.set_agent(triggerIds=[8021], visible=True)
        self.set_agent(triggerIds=[8022], visible=True)
        self.set_agent(triggerIds=[8023], visible=True)
        self.set_agent(triggerIds=[8024], visible=True)
        self.set_agent(triggerIds=[8025], visible=True)
        self.set_agent(triggerIds=[8026], visible=True)
        self.set_agent(triggerIds=[8027], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return LeftBehind02(self.ctx)


class LeftBehind02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LeftBehind03(self.ctx)


class LeftBehind03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6200], visible=True) # Voice_Junta_00001779
        self.set_conversation(type=2, spawnId=11001557, script='$63000029_CS__CAVE01__30$', arg4=6) # 준타 00001779

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return LeftBehind04(self.ctx)


class LeftBehind04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LeftBehind05(self.ctx)


class LeftBehind05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6009], visible=True) # Voice_Laoz_00001831
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__31$', arg4=7) # 라오즈 00001831

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return LeftBehind06(self.ctx)


class LeftBehind06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=303, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LeftBehind07(self.ctx)


class LeftBehind07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_conversation(type=2, spawnId=11001708, script='$63000029_CS__CAVE01__32$', arg4=4) # 틴차이 00001688

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LeftBehind08(self.ctx)


class LeftBehind08(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LeftBehind09(self.ctx)


class LeftBehind09(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=634, enable=True)
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Event_A')
        self.set_effect(triggerIds=[6107], visible=True) # Voice_Kandura_00001862
        self.set_conversation(type=2, spawnId=11001559, script='$63000029_CS__CAVE01__33$', arg4=6) # 칸두라 00001862

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return LeftBehind10(self.ctx)


class LeftBehind10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LeftBehind11(self.ctx)


class LeftBehind11(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=635, enable=True)
        self.set_effect(triggerIds=[6010], visible=True) # Voice_Laoz_00001834
        self.set_conversation(type=2, spawnId=11001556, script='$63000029_CS__CAVE01__34$', arg4=5) # 라오즈 00001834

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LeftBehind12(self.ctx)


class LeftBehind12(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LaozVersusKahnAttack01(self.ctx)


# 전투 연출 교전
class LaozVersusKahnAttack01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_304')
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_403')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return LaozVersusKahnAttack02(self.ctx)


# 전투 연출 대치
class LaozVersusKahnAttack02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozVersusKahnAttack03(self.ctx)


class LaozVersusKahnAttack03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=651, enable=True) # zoomin
        self.set_effect(triggerIds=[5820], visible=True) # LaozVsKandura_FightBlending
        self.set_npc_emotion_loop(spawnId=305, sequenceName='Bore_B', duration=15000) # 라오즈
        self.set_npc_emotion_loop(spawnId=403, sequenceName='Attack_02_F', duration=15000) # 칸두라
        self.set_effect(triggerIds=[5930], visible=True) # Sound_LaozVsKandura_FightBlending

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return LaozVersusKahnCrash01(self.ctx)


class LaozVersusKahnCrash01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[5600], visible=True) # SandStormSmall_GroundCollapse

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LaozVersusKahnCrash02(self.ctx)


class LaozVersusKahnCrash02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=650, enable=True) # zoomout
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509], visible=True, arg3=0, delay=0, scale=0) # CollapseStart

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapaseStart01(self.ctx)


# 전투 연출 격돌
class CollapaseStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5800], visible=True) # Rumble
        self.set_mesh(triggerIds=[3505], visible=False, arg3=0, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3509], visible=False, arg3=100, delay=0, scale=0) # CollapseStart

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapaseStart02(self.ctx)


class CollapaseStart02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3504], visible=False, arg3=0, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3501], visible=False, arg3=50, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3507], visible=False, arg3=100, delay=0, scale=0) # CollapseStart
        self.set_effect(triggerIds=[5931], visible=True) # Sound_LaozVsKandura_FightExplosion

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapaseStart03(self.ctx)


class CollapaseStart03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5821], visible=True) # LaozVsKandura_FightExplosion
        self.set_mesh(triggerIds=[3502], visible=False, arg3=0, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3508], visible=False, arg3=50, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3506], visible=False, arg3=100, delay=0, scale=0) # CollapseStart

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapaseStart04(self.ctx)


class CollapaseStart04(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3503], visible=False, arg3=0, delay=0, scale=0) # CollapseStart
        self.set_mesh(triggerIds=[3500], visible=False, arg3=100, delay=0, scale=0) # CollapseStart

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapaseAbove01(self.ctx)


class CollapaseAbove01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7003], enable=True) # 천장 부수기 스킬
        self.set_effect(triggerIds=[5801], visible=True) # Earthquake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CollapaseGround01(self.ctx)


class CollapaseGround01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[305,403])
        self.set_breakable(triggerIds=[4000], enable=True)
        self.set_breakable(triggerIds=[4001], enable=True)
        self.set_visible_breakable_object(triggerIds=[4000], visible=True)
        self.set_visible_breakable_object(triggerIds=[4001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return CollapaseGround02(self.ctx)


class CollapaseGround02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        self.set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion
        self.set_skill(triggerIds=[7000], enable=True) # 바닥 큐브 부수기 스킬
        self.set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__35$', arg4=3, arg5=0) # 틴차이 00001688

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return CollapaseGround03(self.ctx)


class CollapaseGround03(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_breakable(triggerIds=[4001], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.set_visible_breakable_object(triggerIds=[4001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Earthquake01(self.ctx)


# 동굴이 무너질 것 같은 연출
class Earthquake_CSkip(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7003], enable=True) # 천장 부수기 스킬
        self.set_effect(triggerIds=[5801], visible=True) # Earthquake
        self.set_breakable(triggerIds=[4000], enable=True)
        self.set_breakable(triggerIds=[4001], enable=True)
        self.set_effect(triggerIds=[5820], visible=False) # LaozVsKandura_FightBlending
        self.set_effect(triggerIds=[5821], visible=False) # LaozVsKandura_FightExplosion

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Earthquake_CSkip2(self.ctx)


class Earthquake_CSkip2(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=True) # 바닥 큐브 부수기 스킬
        self.set_effect(triggerIds=[6300], visible=True) # Voice_Tinchai_00001688
        self.set_visible_breakable_object(triggerIds=[4000], visible=True)
        self.set_visible_breakable_object(triggerIds=[4001], visible=True)
        self.set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__35$', arg4=3, arg5=0) # 틴차이 00001688
        self.destroy_monster(spawnIds=[305,403])
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_breakable(triggerIds=[4001], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.set_visible_breakable_object(triggerIds=[4001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Earthquake01(self.ctx)


class Earthquake01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=660, enable=True) # zoomout
        self.set_user_value(triggerId=2, key='EarthquakeStart', value=1)
        self.set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__39$', arg4=4, arg5=2) # 틴차이
        self.set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__40$', arg4=3, arg5=4) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Earthquake02(self.ctx)


class Earthquake02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=640, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Earthquake03(self.ctx)


class Earthquake03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_105')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Earthquake04(self.ctx)


class Earthquake04(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.set_effect(triggerIds=[6301], visible=True) # Voice_Tinchai_00001717
        self.set_conversation(type=1, spawnId=105, script='$63000029_CS__CAVE01__36$', arg4=3, arg5=0) # 틴차이 00001717
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Earthquake05(self.ctx)


class Earthquake05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Idle_A')
        self.set_effect(triggerIds=[6201], visible=True) # Voice_Junta_00001770
        self.set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__37$', arg4=4, arg5=0) # 준타 00001770
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return TimeToLeave01(self.ctx)

    def on_exit(self):
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Idle_A')


class TimeToLeave01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=641, enable=True)
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_203')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_103')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=641, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10036040, textId=10036040) # 가이드 : 준타, 틴차이를 따라 동굴에서 빠져나가기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9004]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5900], visible=True) # StoneGate
        self.set_conversation(type=1, spawnId=205, script='$63000029_CS__CAVE01__38$', arg4=3)
        self.hide_guide_summary(entityId=10036040)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return OpenTheStoneGate01(self.ctx)


class OpenTheStoneGate01(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4500, visible=True, initialSequence='or_fi_struc_stonegate_A01_on') # StoneGate

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return OpenTheStoneGate02(self.ctx)


class OpenTheStoneGate02(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return MoveToNextMap01(self.ctx)


class MoveToNextMap01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_204')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return MoveToNextMap02(self.ctx)


class MoveToNextMap02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_104')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return MoveToNextMap03(self.ctx)


class MoveToNextMap03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[105])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return MoveToNextMap04(self.ctx)


class MoveToNextMap04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[205])

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=1060)


initial_state = Wait
