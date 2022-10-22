""" trigger/52000138_qd/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_sound(triggerId=7101, arg2=True)
        set_actor(triggerId=4001, visible=True, initialSequence='Closed')
        set_actor(triggerId=4002, visible=True, initialSequence='Closed')
        set_actor(triggerId=4003, visible=True, initialSequence='Closed')
        set_actor(triggerId=4004, visible=True, initialSequence='Closed')
        set_actor(triggerId=4005, visible=True, initialSequence='Closed')
        set_actor(triggerId=4006, visible=True, initialSequence='Closed')
        set_actor(triggerId=4007, visible=True, initialSequence='Closed')
        set_actor(triggerId=4008, visible=True, initialSequence='Closed')
        set_actor(triggerId=4009, visible=True, initialSequence='Closed')
        set_actor(triggerId=4010, visible=True, initialSequence='Closed')
        set_actor(triggerId=4011, visible=True, initialSequence='Closed') # 사이렌 종료
        set_actor(triggerId=1001, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1002, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1003, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1004, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1005, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1006, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1007, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1008, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1009, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1010, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1013, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1014, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1015, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1016, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1017, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1018, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1019, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1020, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1021, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1022, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1023, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1024, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1025, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1026, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1027, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=1028, visible=True, initialSequence='sf_quest_light_A01_Off')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG\weather\Eff_monochrome_03.xml')
        set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_ Object_Train_alert.xml')
        set_ambient_light(primary=[0,0,0])
        set_ambient_light(primary=[1,1,1])
        add_buff(boxIds=[701], skillId=99910230, level=1, arg4=False, arg5=True) # 레논 변신
        add_buff(boxIds=[701], skillId=99910230, level=1, arg4=False, arg5=False) # 레논 변신
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return act1_wave1()


class act1_wave1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000138_QD__MAIN__0$', arg3='3000', arg4='0') # 1구역 사이렌 시작
        set_actor(triggerId=1001, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1002, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1003, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1004, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1009, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1010, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1025, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1026, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1027, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1028, visible=True, initialSequence='sf_quest_light_A01_On') # 다크윈드 대원 101번 대사
        set_conversation(type=1, spawnId=101, script='$52000138_QD__MAIN__1$', arg4=3, arg5=0)
        set_sound(triggerId=10000, arg2=True)
        set_sound(triggerId=7002, arg2=True)
        # <action name="대화를설정한다" arg1="1" arg2="122" arg3="레논! 사실이 아니지? 네가 그럴리가 없잖아!" arg4="4" arg5="4"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act1_wave2()


class act1_wave2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act1_wave2_move()


class act1_wave2_move(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=True, initialSequence='Opened')
        set_conversation(type=1, spawnId=102, script='$52000138_QD__MAIN__2$', arg4=3, arg5=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return act1_wave2_1()


class act1_wave2_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act1_wave2_move_1()


class act1_wave2_move_1(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        set_conversation(type=1, spawnId=104, script='$52000138_QD__MAIN__3$', arg4=3, arg5=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return act1_wave3()


class act1_wave3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103,105])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return act1_wave3_move()


class act1_wave3_move(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=105, script='$52000138_QD__MAIN__4$', arg4=3, arg5=3) # 1구역 중앙 문 개방
        set_actor(triggerId=4003, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return ready_1()


class ready_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[110,111])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return act2_wave1()


class act2_wave1(state.State):
    def on_enter(self):
        set_actor(triggerId=1005, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1006, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1007, visible=True, initialSequence='sf_quest_light_A01_Of')
        set_actor(triggerId=1008, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1023, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1024, visible=True, initialSequence='sf_quest_light_A01_On')
        set_conversation(type=1, spawnId=110, script='$52000138_QD__MAIN__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=111, script='$52000138_QD__MAIN__6$', arg4=3, arg5=1)
        # <action name="대화를설정한다" arg1="1" arg2="123" arg3="아니라고 말해줘! 아니라고 말해달라고!" arg4="4" arg5="3"/> 블랙아이 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act2_wave2()


class act2_wave2(state.State):
    def on_enter(self):
        set_actor(triggerId=4004, visible=True, initialSequence='Opened') # 다크윈드 대원 106,107번 소환
        create_monster(spawnIds=[106,107])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act2_wave2_move()


class act2_wave2_move(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=106, script='$52000138_QD__MAIN__7$', arg4=3, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return act2_wave3()


class act2_wave3(state.State):
    def on_enter(self):
        set_actor(triggerId=4005, visible=True, initialSequence='Opened') # 다크윈드 대원 108,109번 소환
        create_monster(spawnIds=[108,109])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return act2_wave3_move()


class act2_wave3_move(state.State):
    def on_enter(self):
        set_actor(triggerId=4006, visible=True, initialSequence='Opened')
        set_conversation(type=1, spawnId=109, script='$52000138_QD__MAIN__8$', arg4=3, arg5=3)
        create_monster(spawnIds=[112])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return act2_wave3_move_1()


class act2_wave3_move_1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=112, script='$52000138_QD__MAIN__9$', arg4=3, arg5=4)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703]):
            return ready_2()


class ready_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act3_wave1_move()


class act3_wave1_move(state.State):
    def on_enter(self):
        set_actor(triggerId=1013, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1014, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1015, visible=True, initialSequence='sf_quest_light_A01_Of')
        set_actor(triggerId=1016, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1017, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1018, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1019, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1020, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1021, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=1022, visible=True, initialSequence='sf_quest_light_A01_On')
        set_conversation(type=1, spawnId=113, script='$52000138_QD__MAIN__10$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1):
            return act3_wave2_1()


class act3_wave2_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114,115,120,121])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return act3_wave2_2()


class act3_wave2_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=114, script='$52000138_QD__MAIN__11$', arg4=2, arg5=2)
        create_monster(spawnIds=[116,117,118,119])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return act3_wave2_move()


class act3_wave2_move(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=116, script='$52000138_QD__MAIN__12$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123]):
            return escape()


class escape(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[122])
        select_camera_path(pathIds=[8001], returnView=False)
        set_scene_skip(state=endready, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return plot()


class plot(state.State):
    def on_enter(self):
        set_sound(triggerId=7102, arg2=True)
        set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__13$', arg4=3, arg5=4)
        move_npc(spawnId=122, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return scheme1()


class scheme1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__14$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scheme2()


class scheme2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__15$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scheme3()


class scheme3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__16$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scheme4()

    def on_exit(self):
        select_camera_path(pathIds=[8002], returnView=False)


class scheme4(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=1500)
        set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__17$', arg4=5, arg5=0)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return endready()


class endready(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='windead')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return end()


class end(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='windead')
        move_user(mapId=2000153, portalId=2)


