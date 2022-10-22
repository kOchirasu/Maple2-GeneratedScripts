""" trigger/02010055_bf/scene02.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 난이도체크()
        if not is_dungeon_room():
            return 퀘스트던전대기()


class 난이도체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_level(level=2):
            return 레이드대기()
        if dungeon_level(level=3):
            return None # Missing State: 카오스레이드


class 퀘스트던전대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2299]):
            return 영상준비()


class 레이드대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 영상준비()


class 카오스레이드대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2199]):
            return 영상준비()


class 연출시작딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)
        create_monster(spawnIds=[1002,1003,1004], arg2=False)
        set_skip(state=NPC이동)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 스타츠대사01()


class 스타츠대사01(state.State):
    def on_enter(self):
        set_skip(state=NPC이동)
        set_conversation(type=2, spawnId=11001292, script='$02010055_BF__SCENE02__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 타라대사01()


class 타라대사01(state.State):
    def on_enter(self):
        set_skip(state=NPC이동)
        set_conversation(type=2, spawnId=11001218, script='$02010055_BF__SCENE02__1$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 스타츠대사02()


class 스타츠대사02(state.State):
    def on_enter(self):
        set_skip(state=NPC이동)
        set_conversation(type=2, spawnId=11001292, script='$02010055_BF__SCENE02__2$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=302, enable=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_A')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            destroy_monster(spawnIds=[1002,1003,1004])
            return 종료()


class 영상준비(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='21', seconds=10)
        select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\KarKarBossEvent.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 종료()
        if wait_tick(waitTick=10000):
            return 종료()


class 종료(state.State):
    pass


