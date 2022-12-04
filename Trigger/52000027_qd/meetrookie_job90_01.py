""" trigger/52000027_qd/meetrookie_job90_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.set_agent(triggerIds=[8102], visible=True)
        self.set_agent(triggerIds=[8103], visible=True)
        self.set_agent(triggerIds=[8104], visible=True)
        self.set_agent(triggerIds=[8200], visible=True)
        self.set_agent(triggerIds=[8201], visible=True)
        self.set_agent(triggerIds=[8202], visible=True)
        self.set_agent(triggerIds=[8203], visible=True)
        self.set_agent(triggerIds=[8204], visible=True)
        self.set_agent(triggerIds=[8205], visible=True)
        self.create_monster(spawnIds=[901,902,903,911,912], animationEffect=False)
        self.set_ladder(triggerIds=[4000], visible=False, animationEffect=False, animationDelay=2)
        self.set_ladder(triggerIds=[4001], visible=False, animationEffect=False, animationDelay=2)
        self.set_mesh(triggerIds=[8900,8901,8902,8903], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[8001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[8002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[8003], visible=True, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=7000, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=7001, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=7100, visible=True, initialSequence='Closed') # floor
        self.set_actor(triggerId=7101, visible=True, initialSequence='Closed') # floor
        self.set_actor(triggerId=7102, visible=True, initialSequence='Closed') # floor
        self.set_actor(triggerId=7103, visible=True, initialSequence='Closed') # floor
        self.set_actor(triggerId=7200, visible=True, initialSequence='Down_Idle_A') # blackeyeman
        self.set_actor(triggerId=7201, visible=True, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7202, visible=True, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7203, visible=True, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7204, visible=False, initialSequence='Down_Idle_B') # runebladerscout
        self.set_actor(triggerId=7300, visible=True, initialSequence='Closed') # lever
        self.set_breakable(triggerIds=[6201,6202,6203], enable=False)
        self.set_visible_breakable_object(triggerIds=[6201,6202,6203], visible=False)
        self.set_mesh(triggerIds=[8500], visible=True, arg3=0, delay=0, scale=0) # goldsafebox
        self.set_interact_object(triggerIds=[10000420], state=0) # goldsafebox
        self.set_effect(triggerIds=[6100], visible=False) # LeverHear
        self.set_effect(triggerIds=[6200], visible=False) # MetalDoor
        self.set_effect(triggerIds=[6300], visible=False) # MetalDoor
        self.set_effect(triggerIds=[6400], visible=False) # GroundDoor
        self.set_effect(triggerIds=[6401], visible=False) # GroundDoor
        self.set_effect(triggerIds=[6500], visible=False) # FallDownScream

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[20002243], questStates=[1], jobCode=90):
            return 차전투대기1(self.ctx)


class 차전투대기1(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25200271, textId=25200271)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차전투중1(self.ctx)


class 차전투중1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903]):
            return 차전투종료1(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25200271)


class 차전투종료1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키등장01(self.ctx)


class 루키등장01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키등장02(self.ctx)


class 루키등장02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1011')
        self.set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__0$', arg4=3, arg5=0)
        self.set_skip(state=루키등장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 루키등장03(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 루키등장03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__1$', arg4=3, arg5=0)
        self.set_skip(state=사다리생성01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 사다리생성01(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 사다리생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 사다리생성02(self.ctx)


class 사다리생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8001], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1012')
        self.select_camera_path(pathIds=[600,601], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 사다리생성03(self.ctx)


class 사다리생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=7300, visible=True, initialSequence='Opened') # lever
        self.set_effect(triggerIds=[6100], visible=True) # LeverHear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 사다리생성04(self.ctx)


class 사다리생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[4000], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[4001], visible=True, animationEffect=True, animationDelay=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 사다리생성05(self.ctx)


class 사다리생성05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 루키이동01(self.ctx)


class 루키이동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000027_QD__MEETROOKIE01__2$', arg4=3, arg5=1)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 루키이동02(self.ctx)


class 루키이동02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__3$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키이동03(self.ctx)


class 루키이동03(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=7000, visible=True, initialSequence='Opened') # door
        self.set_effect(triggerIds=[6200], visible=True) # MetalDoor
        self.set_mesh(triggerIds=[8002], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키이동04(self.ctx)


class 루키이동04(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차전투시작2(self.ctx)


class 차전투시작2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[911,912]):
            return 루키이동10(self.ctx)


class 루키이동10(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1015')
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__4$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9101, spawnIds=[102]):
            return 루키이동11(self.ctx)


class 루키이동11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 상황연출01(self.ctx)


class 상황연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__5$', arg4=3, arg5=0)
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 상황연출02(self.ctx)


class 상황연출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=701, enable=True)
        self.set_skip(state=상황연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 상황연출03(self.ctx)


class 상황연출03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=702, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 상황연출04(self.ctx)


class 상황연출04(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키경고01(self.ctx)


class 루키경고01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__6$', arg4=3, arg5=0)
        self.set_skip(state=루키경고02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 루키경고02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 루키경고02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 루키경고03(self.ctx)


class 루키경고03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__7$', arg4=5, arg5=0)
        self.set_skip(state=루키경고04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 루키경고04(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 루키경고04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=701, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레버찾기01(self.ctx)


class 레버찾기01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TrapOpen', value=0)
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__8$', arg4=3, arg5=1)
        self.show_guide_summary(entityId=25200272, textId=25200272)
        self.set_user_value(triggerId=2, key='SetLever', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 레버찾기02(self.ctx)


class 레버찾기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOpen', value=1):
            return 함정연출01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=25200272)


class 함정연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001610, script='$52000027_QD__MEETROOKIE01__9$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 함정연출02(self.ctx)


class 함정연출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=800, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 함정연출03(self.ctx)


class 함정연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[6201,6202,6203], enable=True)
        self.set_visible_breakable_object(triggerIds=[6201,6202,6203], visible=True)
        self.set_effect(triggerIds=[6500], visible=True) # FallDownScream
        self.set_actor(triggerId=7201, visible=False, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7202, visible=False, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7203, visible=False, initialSequence='Idle_A') # mafia
        self.set_actor(triggerId=7100, visible=True, initialSequence='Opened') # floor
        self.set_actor(triggerId=7101, visible=True, initialSequence='Opened') # floor
        self.set_actor(triggerId=7102, visible=True, initialSequence='Opened') # floor
        self.set_actor(triggerId=7103, visible=True, initialSequence='Opened') # floor
        self.set_mesh(triggerIds=[8900,8901,8902,8903], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[6400], visible=True) # GroundDoor
        self.set_effect(triggerIds=[6401], visible=True) # GroundDoor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 함정연출04(self.ctx)


class 함정연출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=800, enable=False)
        self.set_visible_breakable_object(triggerIds=[6201,6202,6203], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 루키이동20(self.ctx)


class 루키이동20(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25200273, textId=25200273, duration=4000)
        self.set_actor(triggerId=7001, visible=True, initialSequence='Opened') # door
        self.set_effect(triggerIds=[6300], visible=True) # MetalDoor
        self.set_mesh(triggerIds=[8003], visible=False, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[8200], visible=False)
        self.set_agent(triggerIds=[8201], visible=False)
        self.set_agent(triggerIds=[8202], visible=False)
        self.set_agent(triggerIds=[8203], visible=False)
        self.set_agent(triggerIds=[8204], visible=False)
        self.set_agent(triggerIds=[8205], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9004]):
            return 루키이동21(self.ctx)


class 루키이동21(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000027_QD__MEETROOKIE01__10$', arg4=3, arg5=1)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1017')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 루키이동22(self.ctx)


class 루키이동22(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9102, spawnIds=[102]):
            return 루키이동23(self.ctx)


class 루키이동23(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9003]):
            return 루키미션01(self.ctx)


class 루키미션01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=801, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 루키미션02(self.ctx)


class 루키미션02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__11$', arg4=3, arg5=0)
        self.set_skip(state=루키미션03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 루키미션03(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 루키미션03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000027_QD__MEETROOKIE01__12$', arg4=4, arg5=0)
        self.set_mesh(triggerIds=[8500], visible=False, arg3=100, delay=0, scale=0) # goldsafebox
        self.set_interact_object(triggerIds=[10000420], state=1) # goldsafebox
        self.set_skip(state=루키미션04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 루키미션04(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 루키미션04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미션완료01(self.ctx)


class 미션완료01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[20002243], questStates=[2]):
            return 미션완료02(self.ctx)


class 미션완료02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유저퇴장(self.ctx)


class 유저퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000100, portalId=9, boxId=9900)


initial_state = 대기
