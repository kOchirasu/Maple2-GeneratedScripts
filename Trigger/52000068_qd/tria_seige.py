""" trigger/52000068_qd/tria_seige.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 퀘스트분기(self.ctx)


class 퀘스트분기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11010, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=16000, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=16001, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=16002, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16003, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16004, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16005, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16006, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16007, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=16008, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16009, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16010, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16011, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=16012, visible=False, initialSequence='Stun_A')
        self.set_interact_object(triggerIds=[10001074], state=2)
        self.set_interact_object(triggerIds=[10001075], state=2)
        self.set_interact_object(triggerIds=[10001076], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_breakable(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[20002264], questStates=[3]):
            return 재접속유저케어(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[20002263], questStates=[3]):
            return 조디사망연출(self.ctx)
        if not self.quest_user_detected(boxIds=[199], questIds=[20002263], questStates=[3]):
            return 침공이벤트시작(self.ctx)


class 재접속유저케어(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023], animationEffect=False)
        self.create_monster(spawnIds=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], animationEffect=False)
        self.set_visible_breakable_object(triggerIds=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012], visible=False)
        self.set_sound(triggerId=90000, enable=True) # TriaAttack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 트리거멈춤(self.ctx)


class 트리거멈춤(trigger_api.Trigger):
    pass


# 여기서부터 NPC조디 사망연출
class 조디사망연출(trigger_api.Trigger):
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
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_agent(triggerIds=[8014], visible=False)
        self.set_agent(triggerIds=[8015], visible=False)
        self.set_agent(triggerIds=[8016], visible=False)
        self.set_agent(triggerIds=[8017], visible=False)
        self.set_agent(triggerIds=[8018], visible=False)
        self.set_agent(triggerIds=[8019], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출트리거로고고(self.ctx)


class 연출트리거로고고(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99999201, key='tria_seige', value=1)


# 여기서부터 군단 침공 이벤트
class 침공이벤트시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[701], enable=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
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
        self.create_monster(spawnIds=[1001,2001,2002], animationEffect=False)
        self.create_monster(spawnIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026], animationEffect=False)
        self.create_monster(spawnIds=[4100,4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124], animationEffect=False)
        self.set_breakable(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동2(self.ctx)


class 카메라이동2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 데블린동작(self.ctx)


class 데블린동작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        self.set_npc_emotion_sequence(spawnId=2001, sequenceName='AttackReady_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마드리아카메라(self.ctx)


class 마드리아카메라(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=311, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마드리아백샷(self.ctx)


class 마드리아백샷(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2002, script='$52000068_QD__TRIA_SEIGE__0$', arg4=3, arg5=0)
        self.set_onetime_effect(id=1990, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_01_00001990.xml')
        self.select_camera(triggerId=303, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 레논대사01(self.ctx)


class 레논대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__1$', arg4=4)
        self.select_camera(triggerId=304, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레논대사02(self.ctx)


class 레논대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__2$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레논대사03(self.ctx)


class 레논대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__3$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 레논대사03_1(self.ctx)


class 레논대사03_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[199], skillId=70000109, level=1, isPlayer=False, isSkillSet=False) # 초생회
        self.select_camera(triggerId=304, enable=False)
        # action name="카메라리셋" interpolationTime="0.0"/
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_conversation(type=1, spawnId=1001, script='$52000068_QD__TRIA_SEIGE__4$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 임무01(self.ctx)
        if self.user_detected(boxIds=[101]):
            return 임무01(self.ctx)


class 임무01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(triggerIds=[10001074], state=1)
        self.set_interact_object(triggerIds=[10001075], state=1)
        self.set_interact_object(triggerIds=[10001076], state=1)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__5$', arg4=4)
        self.set_scene_skip(state=임무01반응대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 임무01반응대기(self.ctx)


class 임무01반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(boxId=199, skillId=70000107)
        self.select_camera(triggerId=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001074,10001075,10001076], stateValue=2):
            self.set_conversation(type=1, spawnId=1001, script='$52000068_QD__TRIA_SEIGE__6$', arg4=4, arg5=0)
            self.create_item(spawnIds=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012])
            self.add_buff(boxIds=[199], skillId=70000058, level=1, isPlayer=False, isSkillSet=False)
            return 임무02대기(self.ctx)


class 임무02대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 임무02(self.ctx)


class 임무02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
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
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=306, enable=True)
        self.set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__7$', arg4=4)
        self.create_monster(spawnIds=[1101,1102,1103,1104], animationEffect=False, animationDelay=6000)
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_1101')
        self.move_npc(spawnId=1102, patrolName='MS2PatrolData_1102')
        self.move_npc(spawnId=1103, patrolName='MS2PatrolData_1103')
        self.move_npc(spawnId=1104, patrolName='MS2PatrolData_1104')
        self.set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 임무02_2(self.ctx)


class 대사스킵용01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 임무02_2(self.ctx)


class 임무02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
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
        self.set_effect(triggerIds=[602], visible=True)
        self.select_camera(triggerId=307, enable=True)
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__8$', arg4=4)
        self.set_npc_emotion_sequence(spawnId=2003, sequenceName='AttackReady_A')
        self.set_scene_skip(state=임무02종료대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 임무02종료대기(self.ctx)


class 임무02종료대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(boxId=199, skillId=70000107)
        self.select_camera(triggerId=307, enable=False)
        self.set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 임무02종료(self.ctx)
        if self.monster_dead(boxIds=[2003]):
            return 임무02종료(self.ctx)


class 임무02종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=309, enable=True)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[2004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillA', value=1):
            return 데블린카메라이동(self.ctx)


class 데블린카메라이동(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=310, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillB', value=1):
            return 벽파괴대기(self.ctx)


class 벽파괴대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 벽파괴(self.ctx)


class 벽파괴(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2101,2102,2103,2104], animationEffect=False, animationDelay=6000)
        self.move_npc(spawnId=2101, patrolName='MS2PatrolData_air')
        self.move_npc(spawnId=2102, patrolName='MS2PatrolData_air')
        self.move_npc(spawnId=2103, patrolName='MS2PatrolData_air')
        self.move_npc(spawnId=2104, patrolName='MS2PatrolData_air')
        self.select_camera(triggerId=308, enable=True)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_skill(triggerIds=[701], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 조디대화(self.ctx)


class 조디대화(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__9$', arg4=4)
        self.set_scene_skip(state=대사스킵용02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 조디대화2(self.ctx)


class 대사스킵용02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 조디대화2(self.ctx)


class 조디대화2(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__10$', arg4=4)
        self.set_scene_skip(state=벽파괴종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 벽파괴종료(self.ctx)


class 벽파괴종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_portal(portalId=2, visible=False, enable=True, minimapVisible=True)
        self.destroy_monster(spawnIds=[2101,2102,2103,2104])
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(boxId=199, skillId=70000107)
        self.select_camera(triggerId=308, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
