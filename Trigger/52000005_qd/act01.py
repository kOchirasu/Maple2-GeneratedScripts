""" trigger/52000005_qd/act01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[202], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002781], questStates=[1]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[202])
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 영감대화준비()


class 영감대화준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return 영감대화01()


class 영감대화01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=3)
        set_conversation(type=2, spawnId=11000031, script='$52000005_QD__ACT01__0$', arg4=3)
        set_skip(state=영감대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 영감대화02대기()


class 영감대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 영감대화02()


class 영감대화02(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=2, spawnId=11000001, script='$52000005_QD__ACT01__1$', arg4=3)
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[201], arg2=True)
        set_skip(state=여제입장01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 여제입장01()


class 여제입장01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='10', seconds=1)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 딜레이03()


class 딜레이03(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 여제대화01()


class 여제대화01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=3)
        set_conversation(type=2, spawnId=11000075, script='$52000005_QD__ACT01__2$', arg4=3)
        set_skip(state=영상준비)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 영상준비()


class 영상준비(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='21', seconds=3)
        select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_scene_movie(fileName='lumieragonhistory.swf', movieId=1)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상종료()


class 영상종료(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000075, script='$52000005_QD__ACT01__3$', arg4=4)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 업적발생()


class 업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=9001, type='trigger', achieve='Lumieragon_History')
        select_camera(triggerId=601, enable=False)
        select_camera(triggerId=602, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


