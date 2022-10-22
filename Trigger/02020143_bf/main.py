""" trigger/02020143_bf/main.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[2]):
            return 이동()
        if quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[3]):
            return 이동()
        if user_detected(boxIds=[102]):
            return 보스등장준비()


class 보스등장준비(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)
        add_buff(boxIds=[102], skillId=50000554, level=1, arg4=False, arg5=False) # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안의 플레이어에게 애디셔널 50000554(레벨1) 회복 버프 부여하기, 이 맵은 추락하면서 시작하는데 추락 대미지에 의해 죽을 수있기 때문에 시작하자마자 무조건 HP회복 버프 부여함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[99], arg2=False) # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   arg1="99"

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1100):
            return 클리어성공유무체크시작()


class 클리어성공유무체크시작(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 연출딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 던전실패(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


class 연출딜레이(state.State):
    def on_enter(self):
        set_achievement(achieve='TurkaQuestDungeonClear') # arg3="TurkaQuestDungeonClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 영상재생준비()


class 영상재생준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\Kritias_03.usm', movieId=1)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Quit()
        if wait_tick(waitTick=129000):
            return Quit()


class Quit(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[2]):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=52100304, portalId=1)

    def on_tick(self) -> state.State:
        if true():
            return 시작대기중()


