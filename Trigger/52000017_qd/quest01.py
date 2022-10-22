""" trigger/52000017_qd/quest01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False)
        set_effect(triggerIds=[5001], visible=False)
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[50001444], questStates=[2]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_Remember_Vision.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 말풍선딜레이()


class 말풍선딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000017_QD__QUEST01__0$', arg4=3, arg5=0)
        set_scene_skip(state=종료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC대사01()


class NPC대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True)
        set_conversation(type=2, spawnId=11001560, script='$52000017_QD__QUEST01__1$', arg4=4)
        set_skip(state=NPC대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NPC대사02()


class NPC대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NPC대사02()


class NPC대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_conversation(type=2, spawnId=11001560, script='$52000017_QD__QUEST01__2$', arg4=3)
        set_skip(state=NPC대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class NPC대사02스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        move_user(mapId=52000040, portalId=1)


