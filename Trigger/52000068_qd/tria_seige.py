""" trigger/52000068_qd/tria_seige.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 퀘스트분기()


class 퀘스트분기(state.State):
    def on_enter(self):
        set_actor(triggerId=11010, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=16000, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=16001, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=16002, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16003, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16004, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16005, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16006, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16007, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=16008, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16009, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16010, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16011, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=16012, visible=False, initialSequence='Stun_A')
        set_interact_object(triggerIds=[10001074], state=2)
        set_interact_object(triggerIds=[10001075], state=2)
        set_interact_object(triggerIds=[10001076], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_breakable(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016], enabled=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[20002264], questStates=[3]):
            return 재접속유저케어()
        if quest_user_detected(boxIds=[199], questIds=[20002263], questStates=[3]):
            return 조디사망연출()
        if not quest_user_detected(boxIds=[199], questIds=[20002263], questStates=[3]):
            return 침공이벤트시작()


class 재접속유저케어(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023], arg2=False)
        create_monster(spawnIds=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], arg2=False)
        set_visible_breakable_object(triggerIds=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012], arg2=False)
        set_sound(triggerId=90000, arg2=True) # TriaAttack

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 트리거멈춤()


class 트리거멈춤(state.State):
    pass


# 여기서부터 NPC조디 사망연출
class 조디사망연출(state.State):
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
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        set_agent(triggerIds=[8016], visible=False)
        set_agent(triggerIds=[8017], visible=False)
        set_agent(triggerIds=[8018], visible=False)
        set_agent(triggerIds=[8019], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출트리거로고고()


class 연출트리거로고고(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999201, key='tria_seige', value=1)


# 여기서부터 군단 침공 이벤트
class 침공이벤트시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[701], isEnable=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
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
        create_monster(spawnIds=[1001,2001,2002], arg2=False)
        create_monster(spawnIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026], arg2=False)
        create_monster(spawnIds=[4100,4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124], arg2=False)
        set_breakable(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016], enabled=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동2()


class 카메라이동2(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 데블린동작()


class 데블린동작(state.State):
    def on_enter(self):
        set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        set_npc_emotion_sequence(spawnId=2001, sequenceName='AttackReady_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마드리아카메라()


class 마드리아카메라(state.State):
    def on_enter(self):
        select_camera(triggerId=311, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마드리아백샷()


class 마드리아백샷(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2002, script='$52000068_QD__TRIA_SEIGE__0$', arg4=3, arg5=0)
        set_onetime_effect(id=1990, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_01_00001990.xml')
        select_camera(triggerId=303, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 레논대사01()


class 레논대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__1$', arg4=4)
        select_camera(triggerId=304, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레논대사02()


class 레논대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레논대사03()


class 레논대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__3$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레논대사03_1()


class 레논대사03_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class Skip_1(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=4)
        reset_camera(interpolationTime=0.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        add_buff(boxIds=[199], skillId=70000109, level=1, arg4=False, arg5=False) # 초생회
        select_camera(triggerId=304, enable=False) # action name="카메라리셋" interpolationTime="0.0"/
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_conversation(type=1, spawnId=1001, script='$52000068_QD__TRIA_SEIGE__4$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 임무01()
        if user_detected(boxIds=[101]):
            return 임무01()


class 임무01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_interact_object(triggerIds=[10001074], state=1)
        set_interact_object(triggerIds=[10001075], state=1)
        set_interact_object(triggerIds=[10001076], state=1)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=305, enable=True)
        set_conversation(type=2, spawnId=11000064, script='$52000068_QD__TRIA_SEIGE__5$', arg4=4)
        set_scene_skip(state=임무01반응대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 임무01반응대기()


class 임무01반응대기(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        remove_buff(boxId=199, skillId=70000107)
        select_camera(triggerId=305, enable=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001074,10001075,10001076], arg2=2):
            set_conversation(type=1, spawnId=1001, script='$52000068_QD__TRIA_SEIGE__6$', arg4=4, arg5=0)
            create_item(spawnIds=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012])
            add_buff(boxIds=[199], skillId=70000058, level=1, arg4=False, arg5=False)
            return 임무02대기()


class 임무02대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 임무02()


class 임무02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
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
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=306, enable=True)
        set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__7$', arg4=4)
        create_monster(spawnIds=[1101,1102,1103,1104], arg2=False, arg3=6000)
        move_npc(spawnId=1101, patrolName='MS2PatrolData_1101')
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102')
        move_npc(spawnId=1103, patrolName='MS2PatrolData_1103')
        move_npc(spawnId=1104, patrolName='MS2PatrolData_1104')
        set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 임무02_2()


class 대사스킵용01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 임무02_2()


class 임무02_2(state.State):
    def on_enter(self):
        set_scene_skip()
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
        set_effect(triggerIds=[602], visible=True)
        select_camera(triggerId=307, enable=True)
        create_monster(spawnIds=[2003], arg2=False)
        set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__8$', arg4=4)
        set_npc_emotion_sequence(spawnId=2003, sequenceName='AttackReady_A')
        set_scene_skip(state=임무02종료대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 임무02종료대기()


class 임무02종료대기(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        remove_buff(boxId=199, skillId=70000107)
        select_camera(triggerId=307, enable=False)
        set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 임무02종료()
        if monster_dead(boxIds=[2003]):
            return 임무02종료()


class 임무02종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=309, enable=True)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        destroy_monster(spawnIds=[2001])
        create_monster(spawnIds=[2004], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='SetSkillA', value=1):
            return 데블린카메라이동()


class 데블린카메라이동(state.State):
    def on_enter(self):
        select_camera(triggerId=310, enable=True)

    def on_tick(self) -> state.State:
        if user_value(key='SetSkillB', value=1):
            return 벽파괴대기()


class 벽파괴대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 벽파괴()


class 벽파괴(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2101,2102,2103,2104], arg2=False, arg3=6000)
        move_npc(spawnId=2101, patrolName='MS2PatrolData_air')
        move_npc(spawnId=2102, patrolName='MS2PatrolData_air')
        move_npc(spawnId=2103, patrolName='MS2PatrolData_air')
        move_npc(spawnId=2104, patrolName='MS2PatrolData_air')
        select_camera(triggerId=308, enable=True)
        set_effect(triggerIds=[603], visible=True)
        set_skill(triggerIds=[701], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 조디대화()


class 조디대화(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__9$', arg4=4)
        set_scene_skip(state=대사스킵용02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 조디대화2()


class 대사스킵용02(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 조디대화2()


class 조디대화2(state.State):
    def on_enter(self):
        set_scene_skip()
        set_conversation(type=2, spawnId=11001838, script='$52000068_QD__TRIA_SEIGE__10$', arg4=4)
        set_scene_skip(state=벽파괴종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 벽파괴종료()


class 벽파괴종료(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[2101,2102,2103,2104])
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[603], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        remove_buff(boxId=199, skillId=70000107)
        select_camera(triggerId=308, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 종료()


class 종료(state.State):
    pass


