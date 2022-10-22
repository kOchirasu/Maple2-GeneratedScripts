""" trigger/02020130_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 공중에서 등장하는 소환몹이 밟는  트리거박스임
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 2셋트 전투판에 배치된 포탈
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 12시 전투판에 배치된 포탈
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 8시 전투판에 배치된 포탈
        set_portal(portalId=23, visible=False, enabled=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 4시 전투판에 배치된 포탈

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[600]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701,702,703], arg2=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701,702,703]):
            return 종료딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 종료딜레이(state.State):
    def on_enter(self):
        dungeon_stop_timer() # 보스 3마리 다 죽이면 제일 먼저 던전 시간 멈추게 하기
        dungeon_mission_complete(missionId=23040000) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            dungeon_clear()
            set_achievement(achieve='IshuraFinalDungeonClear')
            return 종료()


class 던전실패(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        set_portal(portalId=21, visible=True, enabled=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        set_portal(portalId=22, visible=True, enabled=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        set_portal(portalId=23, visible=True, enabled=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        dungeon_enable_give_up(isEnable='0')


