""" trigger/02020146_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 맵 나가기 포탈, 시작 지점에
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 맵 나가기 포탈, 전투판 지점에
        set_portal(portalId=601, visible=False, enabled=False, minimapVisible=False) # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 보스등장이벤트대기()


class 보스등장이벤트대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[99], arg2=False) # 이슈라 등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출대기()


class 연출대기(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__0$', duration=4000, voice='ko/Npc/00002192')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투진행()


class 전투진행(state.State):
    def on_enter(self):
        set_portal(portalId=601, visible=True, enabled=True, minimapVisible=True) # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_enter(self):
        set_achievement(achieve='IshuraDungeonClear_Quest') # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마무리연출()


class 마무리연출(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__2$', duration=6576, voice='ko/Npc/00002194')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


