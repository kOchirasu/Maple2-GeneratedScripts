""" trigger/02000551_bf/main.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=25, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 난이도체크()


class 난이도체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_id(dungeonId=23050003):
            return 쉬운난이도보스등장()
        if dungeon_id(dungeonId=23051003):
            return 여려움난이도보스등장()
        if wait_tick(waitTick=1100):
            return 여려움난이도보스등장()


class 여려움난이도보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 101 어려움 난이도

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 일러스트대화창()


class 쉬운난이도보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 102 쉬운 난이도

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 일러스트대화창()


class 일러스트대화창(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23000101, illust='BlackBean_Smile', script='$02000551_BF__BOSSSPAWN__0$', duration=7000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2100):
            return 전투진행중()


class 전투진행중(state.State):
    def on_enter(self):
        set_user_value(key='GuideMessage', value=0) # GuideMessage 0으로 초기 셋팅

    def on_tick(self) -> state.State:
        if user_value(key='GuideMessage', value=1):
            return 메시지출력()
        if user_value(key='NextPortal', value=1):
            return 다음진행딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 메시지출력(state.State):
    def on_enter(self):
        show_guide_summary(entityId=29200007, textId=29200007, duration=7000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 전투진행중()


class 던전실패(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_fail()
            return 게임오버()


class 게임오버(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0') # StartPortal.xml 트리거에서 <action name="DungeonEnableGiveUp" isEnable="1" /> 설정함
        set_portal(portalId=21, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=22, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=23, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=24, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=25, visible=True, enabled=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


class 다음진행딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5800):
            return 다음맵가는포탈등장()


class 다음맵가는포탈등장(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


