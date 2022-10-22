""" trigger/52010003_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101])
        set_actor(triggerId=2001, visible=False, initialSequence='Sit_Down_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10002802], questStates=[1]):
            return Event_01()
        if quest_user_detected(boxIds=[701], questIds=[10002836], questStates=[1]):
            return B_Event_01()


class B_Event_01(state.State):
    def on_enter(self):
        set_actor(triggerId=2001, visible=True, initialSequence='Sit_Down_A')
        select_camera(triggerId=8001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[103,104,105,106])
        set_timer(timerId='4', seconds=4)
        move_npc(spawnId=103, patrolName='MS2PatrolData_1004')
        move_npc(spawnId=104, patrolName='MS2PatrolData_1005')
        move_npc(spawnId=105, patrolName='MS2PatrolData_1006')
        # <action name="스킵을설정한다" arg1="Event_02_IDLE" />

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return B_Event_02_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_02_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_02()


class B_Event_02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__13$', arg4=5) # 에레브
        set_skip(state=B_Event_03_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_03_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_03_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_03()


class B_Event_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010003_QD__MAIN__14$', arg4=5) # 스타츠
        set_skip(state=B_Event_04_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_04_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_04_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_04()


class B_Event_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__15$', arg4=5) # 에레브
        set_skip(state=B_Event_05_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_05_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_05_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_05()


class B_Event_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001218, script='$52010003_QD__MAIN__16$', arg4=5) # 타라
        set_skip(state=B_Event_06_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_06_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_06_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_06()


class B_Event_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001217, script='$52010003_QD__MAIN__17$', arg4=5) # 둔바
        set_skip(state=B_Event_07_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_07_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class B_Event_07_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return B_Event_07()


class B_Event_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__18$', arg4=5) # 에레브
        set_skip(state=B_Event_08_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return B_Event_08_IDLE()

    def on_exit(self):
        remove_cinematic_talk()
        select_camera(triggerId=8001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        set_achievement(triggerId=701, type='trigger', achieve='Hope_Lumieragon') # Hope_Lumieragon


class B_Event_08_IDLE(state.State):
    pass


class Event_01(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[102])
        set_timer(timerId='4', seconds=4)
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__0$', arg4=4)
        move_npc(spawnId=102, patrolName='MS2PatrolData_1002')
        set_skip(state=Event_02_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_02_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_02_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__1$', arg4=5)
        set_skip(state=Event_03_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Event_03_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_03_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__2$', arg4=4)
        set_skip(state=Event_04_IDLE)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_04_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_04_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__3$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_05_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_05_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_05_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__4$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_06_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_06_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_06_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__5$', arg4=5)
        set_timer(timerId='5', seconds=5)
        set_skip(state=Event_07_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Event_07_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_07_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_07()


class Event_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__6$', arg4=4)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_08_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_08_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_08_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_08()


class Event_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__7$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_09_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_09_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_09_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_09()


class Event_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__8$', arg4=3)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_10()

    def on_exit(self):
        remove_cinematic_talk()


class Event_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010003_QD__MAIN__9$', arg4=4)
        set_timer(timerId='4', seconds=4)
        # Missing State: Event_11
        set_skip()

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return PlayMovie_01()

    def on_exit(self):
        remove_cinematic_talk()


class PlayMovie_01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='DestinyofMika.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return PlayMovie_02()


class PlayMovie_02(state.State):
    def on_enter(self):
        set_timer(timerId='45', seconds=4)
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__10$', arg4=4)
        set_skip(state=Event_12)

    def on_tick(self) -> state.State:
        if time_expired(timerId='45'):
            return Event_12()

    def on_exit(self):
        remove_cinematic_talk()


class Event_12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__11$', arg4=3)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_13)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_13()


class Event_13(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010003_QD__MAIN__12$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_14)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_14()

    def on_exit(self):
        select_camera(triggerId=8001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class Event_14(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='MikaDestiny') # MikaDestiny
        move_npc(spawnId=102, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[102]):
            return End()


class End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])


