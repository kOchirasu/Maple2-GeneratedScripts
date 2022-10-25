""" trigger/52000138_qd/main.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7101, enable=True)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4002, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4003, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4004, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4005, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4006, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4007, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4008, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4009, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4010, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4011, visible=True, initialSequence='Closed') # 사이렌 종료
        self.set_actor(triggerId=1001, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1002, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1003, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1004, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1005, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1006, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1007, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1008, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1009, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1010, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1013, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1014, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1015, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1016, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1017, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1018, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1019, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1020, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1021, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1022, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1023, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1024, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1025, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1026, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1027, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=1028, visible=True, initialSequence='sf_quest_light_A01_Off')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG\weather\Eff_monochrome_03.xml')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_ Object_Train_alert.xml')
        self.set_ambient_light(primary=[0,0,0])
        self.set_ambient_light(primary=[1,1,1])
        self.add_buff(boxIds=[701], skillId=99910230, level=1, isPlayer=False, isSkillSet=True) # 레논 변신
        self.add_buff(boxIds=[701], skillId=99910230, level=1, isPlayer=False, isSkillSet=False) # 레논 변신
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return act1_wave1(self.ctx)


class act1_wave1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52000138_QD__MAIN__0$', arg3='3000', arg4='0') # 1구역 사이렌 시작
        self.set_actor(triggerId=1001, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1002, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1003, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1004, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1009, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1010, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1025, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1026, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1027, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1028, visible=True, initialSequence='sf_quest_light_A01_On') # 다크윈드 대원 101번 대사
        self.set_conversation(type=1, spawnId=101, script='$52000138_QD__MAIN__1$', arg4=3, arg5=0)
        self.set_sound(triggerId=10000, enable=True)
        self.set_sound(triggerId=7002, enable=True)
        # <action name="대화를설정한다" arg1="1" arg2="122" arg3="레논! 사실이 아니지? 네가 그럴리가 없잖아!" arg4="4" arg5="4"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act1_wave2(self.ctx)


class act1_wave2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act1_wave2_move(self.ctx)


class act1_wave2_move(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='Opened')
        self.set_conversation(type=1, spawnId=102, script='$52000138_QD__MAIN__2$', arg4=3, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return act1_wave2_1(self.ctx)


class act1_wave2_1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act1_wave2_move_1(self.ctx)


class act1_wave2_move_1(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        self.set_conversation(type=1, spawnId=104, script='$52000138_QD__MAIN__3$', arg4=3, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return act1_wave3(self.ctx)


class act1_wave3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,105])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return act1_wave3_move(self.ctx)


class act1_wave3_move(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=105, script='$52000138_QD__MAIN__4$', arg4=3, arg5=3) # 1구역 중앙 문 개방
        self.set_actor(triggerId=4003, visible=True, initialSequence='Opened')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return ready_1(self.ctx)


class ready_1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[110,111])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return act2_wave1(self.ctx)


class act2_wave1(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1005, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1006, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1007, visible=True, initialSequence='sf_quest_light_A01_Of')
        self.set_actor(triggerId=1008, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1011, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1012, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1023, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1024, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_conversation(type=1, spawnId=110, script='$52000138_QD__MAIN__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=111, script='$52000138_QD__MAIN__6$', arg4=3, arg5=1)
        # <action name="대화를설정한다" arg1="1" arg2="123" arg3="아니라고 말해줘! 아니라고 말해달라고!" arg4="4" arg5="3"/> 블랙아이 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act2_wave2(self.ctx)


class act2_wave2(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4004, visible=True, initialSequence='Opened') # 다크윈드 대원 106,107번 소환
        self.create_monster(spawnIds=[106,107])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act2_wave2_move(self.ctx)


class act2_wave2_move(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=106, script='$52000138_QD__MAIN__7$', arg4=3, arg5=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return act2_wave3(self.ctx)


class act2_wave3(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4005, visible=True, initialSequence='Opened') # 다크윈드 대원 108,109번 소환
        self.create_monster(spawnIds=[108,109])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return act2_wave3_move(self.ctx)


class act2_wave3_move(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4006, visible=True, initialSequence='Opened')
        self.set_conversation(type=1, spawnId=109, script='$52000138_QD__MAIN__8$', arg4=3, arg5=3)
        self.create_monster(spawnIds=[112])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return act2_wave3_move_1(self.ctx)


class act2_wave3_move_1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=112, script='$52000138_QD__MAIN__9$', arg4=3, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[703]):
            return ready_2(self.ctx)


class ready_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act3_wave1_move(self.ctx)


class act3_wave1_move(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=1013, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1014, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1015, visible=True, initialSequence='sf_quest_light_A01_Of')
        self.set_actor(triggerId=1016, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1017, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1018, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1019, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1020, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1021, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=1022, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_conversation(type=1, spawnId=113, script='$52000138_QD__MAIN__10$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1):
            return act3_wave2_1(self.ctx)


class act3_wave2_1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[114,115,120,121])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return act3_wave2_2(self.ctx)


class act3_wave2_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=114, script='$52000138_QD__MAIN__11$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[116,117,118,119])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return act3_wave2_move(self.ctx)


class act3_wave2_move(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=116, script='$52000138_QD__MAIN__12$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123]):
            return escape(self.ctx)


class escape(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[122])
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_scene_skip(state=endready, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return plot(self.ctx)


class plot(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7102, enable=True)
        self.set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__13$', arg4=3, arg5=4)
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return scheme1(self.ctx)


class scheme1(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__14$', arg4=5, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scheme2(self.ctx)


class scheme2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__15$', arg4=5, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scheme3(self.ctx)


class scheme3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__16$', arg4=5, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scheme4(self.ctx)

    def on_exit(self):
        self.select_camera_path(pathIds=[8002], returnView=False)


class scheme4(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=1500)
        self.set_conversation(type=1, spawnId=122, script='$52000138_QD__MAIN__17$', arg4=5, arg5=0)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return endready(self.ctx)


class endready(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='windead')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='windead')
        self.move_user(mapId=2000153, portalId=2)


initial_state = idle
