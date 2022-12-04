""" trigger/52010003_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101])
        self.set_actor(triggerId=2001, visible=False, initialSequence='Sit_Down_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10002802], questStates=[1]):
            return Event_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002836], questStates=[1]):
            return B_Event_01(self.ctx)


class B_Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=2001, visible=True, initialSequence='Sit_Down_A')
        self.select_camera(triggerId=8001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[103,104,105,106])
        self.set_timer(timerId='4', seconds=4)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_1004')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_1005')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_1006')
        # <action name="스킵을설정한다" arg1="Event_02_IDLE" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return B_Event_02_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_02(self.ctx)


class B_Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__13$', arg4=5) # 에레브
        self.set_skip(state=B_Event_03_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_03_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_03_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_03(self.ctx)


class B_Event_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010003_QD__MAIN__14$', arg4=5) # 스타츠
        self.set_skip(state=B_Event_04_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_04_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_04_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_04(self.ctx)


class B_Event_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__15$', arg4=5) # 에레브
        self.set_skip(state=B_Event_05_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_05_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_05_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_05(self.ctx)


class B_Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001218, script='$52010003_QD__MAIN__16$', arg4=5) # 타라
        self.set_skip(state=B_Event_06_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_06_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_06_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_06(self.ctx)


class B_Event_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001217, script='$52010003_QD__MAIN__17$', arg4=5) # 둔바
        self.set_skip(state=B_Event_07_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_07_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class B_Event_07_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return B_Event_07(self.ctx)


class B_Event_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__18$', arg4=5) # 에레브
        self.set_skip(state=B_Event_08_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return B_Event_08_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()
        self.select_camera(triggerId=8001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.set_achievement(triggerId=701, type='trigger', achieve='Hope_Lumieragon') # Hope_Lumieragon


class B_Event_08_IDLE(trigger_api.Trigger):
    pass


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[102])
        self.set_timer(timerId='4', seconds=4)
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__0$', arg4=4)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1002')
        self.set_skip(state=Event_02_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_02_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__1$', arg4=5)
        self.set_skip(state=Event_03_IDLE)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Event_03_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_03_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__2$', arg4=4)
        self.set_skip(state=Event_04_IDLE)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_04_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_04_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__3$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_05_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_05_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_05_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__4$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_06_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_06_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_06_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__5$', arg4=5)
        self.set_timer(timerId='5', seconds=5)
        self.set_skip(state=Event_07_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Event_07_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_07_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_07(self.ctx)


class Event_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__6$', arg4=4)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_08_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_08_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_08_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_08(self.ctx)


class Event_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__7$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_09_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_09_IDLE(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_09_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Event_09(self.ctx)


class Event_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__8$', arg4=3)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_10(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__9$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        # Missing State: Event_11
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return PlayMovie_01(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class PlayMovie_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='DestinyofMika.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return PlayMovie_02(self.ctx)


class PlayMovie_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='45', seconds=4)
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__10$', arg4=4)
        self.set_skip(state=Event_12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='45'):
            return Event_12(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Event_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__11$', arg4=3)
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=Event_13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return Event_13(self.ctx)


class Event_13(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__12$', arg4=4)
        self.set_timer(timerId='4', seconds=4)
        self.set_skip(state=Event_14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Event_14(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=8001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Event_14(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='MikaDestiny') # MikaDestiny
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[102]):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])


initial_state = idle
