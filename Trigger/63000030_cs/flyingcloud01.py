""" trigger/63000030_cs/flyingcloud01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # DownArrow
        self.set_effect(triggerIds=[5200], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5300], visible=False) # FlyingCloud
        self.set_effect(triggerIds=[5400], visible=False) # ShadowApp
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001689
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001690
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001691
        self.set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001692
        self.set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001694
        self.set_effect(triggerIds=[6005], visible=False) # Voice_Tinchai_00001695
        self.set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001820
        self.set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001780
        self.set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001781
        self.set_effect(triggerIds=[6103], visible=False) # Voice_Junta_00001782
        self.set_effect(triggerIds=[6104], visible=False) # Voice_Junta_00001783
        self.set_effect(triggerIds=[6105], visible=False) # Voice_Junta_00001792
        self.set_effect(triggerIds=[6106], visible=False) # Voice_Junta_00001798
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
        self.set_interact_object(triggerIds=[10001010], state=0) # FlyingCloud
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0) # Invisible_Bounding

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[1]):
            return QuestOnGiong21(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000454], questStates=[3]):
            return QuestOnGiong11(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000454], questStates=[2]):
            return QuestOnGiong01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000453], questStates=[3]):
            return Delay01(self.ctx)
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


# 하산 퀘스트 수락한 상태
class QuestOnGiong21(common.Trigger):
    def on_enter(self):
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
        self.create_monster(spawnIds=[104,204], animationEffect=False)
        self.move_user(mapId=63000030, portalId=11, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestOnGiong22(self.ctx)


class QuestOnGiong22(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PatrolWhileTalking03(self.ctx)


# 여정의 명분 퀘스트 완료 상태
class QuestOnGiong11(common.Trigger):
    def on_enter(self):
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
        self.create_monster(spawnIds=[103,203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestOnGiong12(self.ctx)


class QuestOnGiong12(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return SecondQuestStart01(self.ctx)


# 여정의 명분 퀘스트 완료 가능 상태
class QuestOnGiong01(common.Trigger):
    def on_enter(self):
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
        self.create_monster(spawnIds=[103,203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestOnGiong02(self.ctx)


class QuestOnGiong02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return FirstQuestStart01(self.ctx)


# 최초 진입
class Delay01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[920,921,922,923,924,925,926,927,928,929,930,931], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround01(self.ctx)


class LookAround01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LookAround02(self.ctx)


class LookAround02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,201], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LookAround03(self.ctx)


class LookAround03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=LookAround07_CSkip, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround04(self.ctx)


class LookAround04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$63000030_CS__FLYINGCLOUD01__0$', arg4=2, arg5=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround05(self.ctx)


class LookAround05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001820
        self.set_conversation(type=1, spawnId=201, script='$63000030_CS__FLYINGCLOUD01__1$', arg4=2, arg5=0) # 준타 00001820
        self.move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        self.move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        self.move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        self.move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        self.move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_931')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround06(self.ctx)


class LookAround06(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        self.move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        self.move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        self.move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround07(self.ctx)


class LookAround07_CSkip(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        self.move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        self.move_npc(spawnId=925, patrolName='MS2PatrolData_925')
        self.move_npc(spawnId=927, patrolName='MS2PatrolData_927')
        self.move_npc(spawnId=928, patrolName='MS2PatrolData_928')
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        self.move_npc(spawnId=924, patrolName='MS2PatrolData_924')
        self.move_npc(spawnId=926, patrolName='MS2PatrolData_926')
        self.move_npc(spawnId=929, patrolName='MS2PatrolData_929')
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_930')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround07(self.ctx)


class LookAround07(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False)
        self.select_camera(triggerId=500, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
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

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleStart01(self.ctx)


class BattleStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10037010, textId=10037010) # 가이드 : 검은 그림자 무리 처치하기

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[920,921,922,923,924,925,926,927,928,929,930,931]):
            return BattleEnd01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10037010)


class BattleEnd01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleEnd02(self.ctx)


class BattleEnd02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000030, portalId=10, boxId=9900)
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[103,203], animationEffect=False)
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleEnd03(self.ctx)


class BattleEnd03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=DialogueSkip10, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Dialogue01(self.ctx)


# 시네마틱 대화 연출
class Dialogue01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001780
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__2$', arg4=7) # 준타 00001780

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return DialogueSkip01(self.ctx)


class DialogueSkip01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue02(self.ctx)


class Dialogue02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001689
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__3$', arg4=6) # 틴차이 00001689

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return DialogueSkip02(self.ctx)


class DialogueSkip02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue03(self.ctx)


class Dialogue03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001690
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__4$', arg4=6) # 틴차이 00001690

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return DialogueSkip03(self.ctx)


class DialogueSkip03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue04(self.ctx)


class Dialogue04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001781
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__5$', arg4=6) # 준타 00001781

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return DialogueSkip04(self.ctx)


class DialogueSkip04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue05(self.ctx)


class Dialogue05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001691
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__6$', arg4=6) # 틴차이 00001691

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return DialogueSkip05(self.ctx)


class DialogueSkip05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue06(self.ctx)


class Dialogue06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001692
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__7$', arg4=6) # 틴차이 00001692

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return DialogueSkip06(self.ctx)


class DialogueSkip06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue07(self.ctx)


class Dialogue07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6103], visible=True) # Voice_Junta_00001782
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__8$', arg4=5) # 준타 00001782

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DialogueSkip07(self.ctx)


class DialogueSkip07(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue08(self.ctx)


class Dialogue08(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__9$', arg4=4) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return DialogueSkip08(self.ctx)


class DialogueSkip08(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Dialogue09(self.ctx)


class Dialogue09(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6104], visible=True) # Voice_Junta_00001783
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__10$', arg4=8) # 준타 00001783

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return DialogueSkip09(self.ctx)


class DialogueSkip09(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue10(self.ctx)


class Dialogue10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001694
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__11$', arg4=5) # 틴차이 00001694
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DialogueSkip10(self.ctx)


class DialogueSkip10(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Idle_A')
        self.select_camera(triggerId=501, enable=False)
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return FirstQuestStart01(self.ctx)


class FirstQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10030160, textId=10030160) # 가이드 : [[icon:questaccept]] 틴차이와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000454], questStates=[2]):
            return FirstQuestEnd01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10030160)


class FirstQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031010, textId=10031010) # 가이드 : [[icon:questcomplete]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000454], questStates=[3]):
            return SecondQuestStart01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10031010)


class SecondQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10031020, textId=10031020) # 가이드 : [[icon:questaccept]] 준타와 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000455], questStates=[1]):
            return PatrolWhileTalking01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10031020)


class PatrolWhileTalking01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PatrolWhileTalking02(self.ctx)


class PatrolWhileTalking02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103,203])
        self.create_monster(spawnIds=[104,204], animationEffect=False)
        self.move_user(mapId=63000030, portalId=11, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PatrolWhileTalking03(self.ctx)


class PatrolWhileTalking03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=FightBack01, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_203')
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolWhileTalking04(self.ctx)


class PatrolWhileTalking04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__12$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__13$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return PatrolWhileTalking05(self.ctx)


class PatrolWhileTalking05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__14$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__15$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__16$', arg4=2, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return ShadowApp01(self.ctx)


class ShadowApp01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=True) # ShadowApp
        self.create_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949], animationEffect=False)
        self.select_camera(triggerId=600, enable=True)
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowApp02(self.ctx)


class ShadowApp02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104')
        self.set_effect(triggerIds=[6105], visible=True) # Voice_Junta_00001792
        self.set_conversation(type=1, spawnId=204, script='$63000030_CS__FLYINGCLOUD01__17$', arg4=2, arg5=0) # 준타 00001792

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return ShadowApp03(self.ctx)


class ShadowApp03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowApp04(self.ctx)


class ShadowApp04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$63000030_CS__FLYINGCLOUD01__18$', arg4=2, arg5=0)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ShadowApp05(self.ctx)


class ShadowApp05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FightBack01(self.ctx)


class FightBack01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_205')
        self.set_effect(triggerIds=[6106], visible=True) # Voice_Junta_00001798
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__FLYINGCLOUD01__19$', arg4=4) # 준타 00001798

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FightBack02(self.ctx)


class FightBack02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FightBack03(self.ctx)


class FightBack03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_105')
        self.set_effect(triggerIds=[6005], visible=True) # Voice_Tinchai_00001695
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__FLYINGCLOUD01__20$', arg4=5) # 틴차이 00001695

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FightBack04(self.ctx)


class FightBack04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[5400], visible=False) # ShadowApp

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return FightBack05(self.ctx)


class FightBack05(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000030, portalId=20, boxId=9900)
        self.destroy_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949])
        self.create_monster(spawnIds=[910,911,912,913,914,915,916,917,918,919], animationEffect=False)
        self.destroy_monster(spawnIds=[104,204])
        self.create_monster(spawnIds=[105,205], animationEffect=False)
        self.select_camera(triggerId=602, enable=True)
        self.set_user_value(triggerId=3, key='SafetyStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return FightBack06(self.ctx)


class FightBack06(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_user_value(triggerId=2, key='PushStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return GotoTria01(self.ctx)


# 암벽등반 가이드 ClimbingGuide01
class GotoTria01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=602, enable=False)
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5201], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5202], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5203], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5204], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5205], visible=True) # 구름터 경로 안내
        self.set_effect(triggerIds=[5100], visible=True) # DownArrow
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10037020, textId=10037020) # 가이드 : 트라이아행 구름에 가까이 가기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return GotoTria02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10037020)


class GotoTria02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10037030, textId=10037030) # 가이드 : 트라이아행 구름에 타기
        self.set_interact_object(triggerIds=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001010], stateValue=0):
            return TakeOffFlyingCloud01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10037030)
        self.set_effect(triggerIds=[5100], visible=False) # DownArrow
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 구름터 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 구름터 경로 안내


class TakeOffFlyingCloud01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_visible_breakable_object(triggerIds=[4000], visible=True)
        self.set_breakable(triggerIds=[4000], enable=True)
        self.set_interact_object(triggerIds=[10001010], state=2) # FlyingCloud 숨기기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TakeOffFlyingCloud02(self.ctx)


class TakeOffFlyingCloud02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # FlyingCloud
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_Bounding
        self.move_user(mapId=63000030, portalId=30, boxId=9900)
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TakeOffFlyingCloud03(self.ctx)


class TakeOffFlyingCloud03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return TakeOffFlyingCloud04(self.ctx)


class TakeOffFlyingCloud04(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000036, portalId=1)
        self.select_camera(triggerId=701, enable=False)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
