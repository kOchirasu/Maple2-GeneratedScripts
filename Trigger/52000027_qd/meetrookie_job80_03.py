""" trigger/52000027_qd/meetrookie_job80_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        set_agent(triggerIds=[8102], visible=True)
        set_agent(triggerIds=[8103], visible=True)
        set_agent(triggerIds=[8104], visible=True)
        set_agent(triggerIds=[8200], visible=True)
        set_agent(triggerIds=[8201], visible=True)
        set_agent(triggerIds=[8202], visible=True)
        set_agent(triggerIds=[8203], visible=True)
        set_agent(triggerIds=[8204], visible=True)
        set_agent(triggerIds=[8205], visible=True)
        create_monster(spawnIds=[901,902,903,911,912], arg2=False)
        set_ladder(triggerIds=[4000], visible=False, animationEffect=False, animationDelay=2)
        set_ladder(triggerIds=[4001], visible=False, animationEffect=False, animationDelay=2)
        set_mesh(triggerIds=[8900,8901,8902,8903], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[8001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[8002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[8003], visible=True, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=7000, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=7001, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=7100, visible=True, initialSequence='Closed') # floor
        set_actor(triggerId=7101, visible=True, initialSequence='Closed') # floor
        set_actor(triggerId=7102, visible=True, initialSequence='Closed') # floor
        set_actor(triggerId=7103, visible=True, initialSequence='Closed') # floor
        set_actor(triggerId=7200, visible=True, initialSequence='Down_Idle_A') # blackeyeman
        set_actor(triggerId=7201, visible=True, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7202, visible=True, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7203, visible=True, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7204, visible=False, initialSequence='Down_Idle_B') # runebladerscout
        set_actor(triggerId=7300, visible=True, initialSequence='Closed') # lever
        set_breakable(triggerIds=[6201,6202,6203], enabled=False)
        set_visible_breakable_object(triggerIds=[6201,6202,6203], arg2=False)
        set_mesh(triggerIds=[8500], visible=True, arg3=0, arg4=0, arg5=0) # goldsafebox
        set_interact_object(triggerIds=[10000420], state=0) # goldsafebox
        set_effect(triggerIds=[6100], visible=False) # LeverHear
        set_effect(triggerIds=[6200], visible=False) # MetalDoor
        set_effect(triggerIds=[6300], visible=False) # MetalDoor
        set_effect(triggerIds=[6400], visible=False) # GroundDoor
        set_effect(triggerIds=[6401], visible=False) # GroundDoor
        set_effect(triggerIds=[6500], visible=False) # FallDownScream

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10003012], questStates=[1], jobCode=80):
            return 차전투대기1()


class 차전투대기1(state.State):
    def on_enter(self):
        set_actor(triggerId=7204, visible=True, initialSequence='Down_Idle_B') # runebladerscout
        show_guide_summary(entityId=25200271, textId=25200271)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투중1()


class 차전투중1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903]):
            return 차전투종료1()

    def on_exit(self):
        hide_guide_summary(entityId=25200271)


class 차전투종료1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키등장01()


class 루키등장01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키등장02()


class 루키등장02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_1011')
        set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__0$', arg4=3, arg5=0)
        set_skip(state=루키등장03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 루키등장03()

    def on_exit(self):
        remove_cinematic_talk()


class 루키등장03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__1$', arg4=3, arg5=0)
        set_skip(state=사다리생성01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 사다리생성01()

    def on_exit(self):
        remove_cinematic_talk()


class 사다리생성01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 사다리생성02()


class 사다리생성02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8001], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1012')
        select_camera_path(pathIds=[600,601], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 사다리생성03()


class 사다리생성03(state.State):
    def on_enter(self):
        set_actor(triggerId=7300, visible=True, initialSequence='Opened') # lever
        set_effect(triggerIds=[6100], visible=True) # LeverHear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 사다리생성04()


class 사다리생성04(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[4000], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[4001], visible=True, animationEffect=True, animationDelay=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 사다리생성05()


class 사다리생성05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 루키이동01()


class 루키이동01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000027_QD__MEETROOKIE01__2$', arg4=3, arg5=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1013')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 루키이동02()


class 루키이동02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__3$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키이동03()


class 루키이동03(state.State):
    def on_enter(self):
        set_actor(triggerId=7000, visible=True, initialSequence='Opened') # door
        set_effect(triggerIds=[6200], visible=True) # MetalDoor
        set_mesh(triggerIds=[8002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키이동04()


class 루키이동04(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_1014')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작2()


class 차전투시작2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[911,912]):
            return 루키이동10()


class 루키이동10(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_1015')
        set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__4$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9101, spawnIds=[102]):
            return 루키이동11()


class 루키이동11(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 상황연출01()


class 상황연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__5$', arg4=3, arg5=0)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 상황연출02()


class 상황연출02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        set_skip(state=상황연출03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 상황연출03()


class 상황연출03(state.State):
    def on_enter(self):
        select_camera(triggerId=702, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 상황연출04()


class 상황연출04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키경고01()


class 루키경고01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__6$', arg4=3, arg5=0)
        set_skip(state=루키경고02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 루키경고02()

    def on_exit(self):
        remove_cinematic_talk()


class 루키경고02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 루키경고03()


class 루키경고03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__7$', arg4=5, arg5=0)
        set_skip(state=루키경고04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 루키경고04()

    def on_exit(self):
        remove_cinematic_talk()


class 루키경고04(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레버찾기01()


class 레버찾기01(state.State):
    def on_enter(self):
        set_user_value(key='TrapOpen', value=0)
        set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__8$', arg4=3, arg5=1)
        show_guide_summary(entityId=25200272, textId=25200272)
        set_user_value(triggerId=2, key='SetLever', value=1)

    def on_tick(self) -> state.State:
        if true():
            return 레버찾기02()


class 레버찾기02(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='TrapOpen', value=1):
            return 함정연출01()

    def on_exit(self):
        hide_guide_summary(entityId=25200272)


class 함정연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 함정연출02()


class 함정연출02(state.State):
    def on_enter(self):
        select_camera(triggerId=800, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 함정연출03()


class 함정연출03(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[6201,6202,6203], enabled=True)
        set_visible_breakable_object(triggerIds=[6201,6202,6203], arg2=True)
        set_effect(triggerIds=[6500], visible=True) # FallDownScream
        set_actor(triggerId=7201, visible=False, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7202, visible=False, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7203, visible=False, initialSequence='Idle_A') # mafia
        set_actor(triggerId=7100, visible=True, initialSequence='Opened') # floor
        set_actor(triggerId=7101, visible=True, initialSequence='Opened') # floor
        set_actor(triggerId=7102, visible=True, initialSequence='Opened') # floor
        set_actor(triggerId=7103, visible=True, initialSequence='Opened') # floor
        set_mesh(triggerIds=[8900,8901,8902,8903], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[6400], visible=True) # GroundDoor
        set_effect(triggerIds=[6401], visible=True) # GroundDoor

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 함정연출04()


class 함정연출04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=800, enable=False)
        set_visible_breakable_object(triggerIds=[6201,6202,6203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 루키이동20()


class 루키이동20(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200273, textId=25200273, duration=4000)
        set_actor(triggerId=7001, visible=True, initialSequence='Opened') # door
        set_effect(triggerIds=[6300], visible=True) # MetalDoor
        set_mesh(triggerIds=[8003], visible=False, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[8200], visible=False)
        set_agent(triggerIds=[8201], visible=False)
        set_agent(triggerIds=[8202], visible=False)
        set_agent(triggerIds=[8203], visible=False)
        set_agent(triggerIds=[8204], visible=False)
        set_agent(triggerIds=[8205], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9004]):
            return 루키이동21()


class 루키이동21(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__10$', arg4=3, arg5=1)
        move_npc(spawnId=102, patrolName='MS2PatrolData_1017')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 루키이동22()


class 루키이동22(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9102, spawnIds=[102]):
            return 루키이동23()


class 루키이동23(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 루키미션01()


class 루키미션01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=801, enable=True)

    def on_tick(self) -> state.State:
        if true():
            return 루키미션02()


class 루키미션02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__11$', arg4=3, arg5=0)
        set_skip(state=루키미션03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 루키미션03()

    def on_exit(self):
        remove_cinematic_talk()


class 루키미션03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__12$', arg4=4, arg5=0)
        set_mesh(triggerIds=[8500], visible=False, arg3=100, arg4=0, arg5=0) # goldsafebox
        set_interact_object(triggerIds=[10000420], state=1) # goldsafebox
        set_skip(state=루키미션04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 루키미션04()

    def on_exit(self):
        remove_cinematic_talk()


class 루키미션04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=801, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미션완료01()


class 미션완료01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[10003012], questStates=[2]):
            return 미션완료02()


class 미션완료02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 유저퇴장()


class 유저퇴장(state.State):
    def on_enter(self):
        move_user(mapId=2000100, portalId=9, boxId=9900)


