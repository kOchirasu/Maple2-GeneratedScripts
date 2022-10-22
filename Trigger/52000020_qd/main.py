""" trigger/52000020_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[60001022], questStates=[1]):
            return camera_01()


class camera_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return monster_spawn_01()


class monster_spawn_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[111,112,113,114], arg2=True) # 1차 스폰
        set_conversation(type=1, spawnId=111, script='$52000020_QD__MAIN__2$', arg4=5)
        set_conversation(type=1, spawnId=112, script='$52000020_QD__MAIN__3$', arg4=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return battle_01()
        if monster_dead(boxIds=[111,112,113,114]):
            return camera_02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class battle_01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114]):
            return camera_02()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class camera_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)
        select_camera_path(pathIds=[8003,8004], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return monster_spawn_02()


class monster_spawn_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[121,122,123,124,125,126], arg2=True) # 2차 스폰
        set_conversation(type=1, spawnId=121, script='$52000020_QD__MAIN__4$', arg4=5)
        set_conversation(type=1, spawnId=124, script='$52000020_QD__MAIN__5$', arg4=5)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return battle_02()
        if monster_dead(boxIds=[121,122,123,124,125,126]):
            return camera_03()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class battle_02(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122,123,124,125,126]):
            return camera_03()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class camera_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)
        select_camera_path(pathIds=[8005,8006], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return monster_spawn_03()


class monster_spawn_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[131,132,133,134,135,136], arg2=True) # 3차 스폰
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return battle_03()
        if monster_dead(boxIds=[131,132,133,134,135,136]):
            return complete()

    def on_exit(self):
        set_conversation(type=1, spawnId=131, script='$52000020_QD__MAIN__1$', arg4=5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class battle_03(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[131,132,133,134,135,136]):
            return complete()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class complete(state.State):
    pass


