""" trigger/02020130_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 공중에서 등장하는 소환몹이 밟는  트리거박스임
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 2셋트 전투판에 배치된 포탈
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 12시 전투판에 배치된 포탈
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 8시 전투판에 배치된 포탈
        self.set_portal(portalId=23, visible=False, enable=False, minimapVisible=False) # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 4시 전투판에 배치된 포탈

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[600]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[701,702,703], animationEffect=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[701,702,703]):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 종료딜레이(common.Trigger):
    def on_enter(self):
        self.dungeon_stop_timer() # 보스 3마리 다 죽이면 제일 먼저 던전 시간 멈추게 하기
        self.dungeon_mission_complete(missionId=23040000) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            self.dungeon_clear()
            self.set_achievement(achieve='IshuraFinalDungeonClear')
            return 종료(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portalId=22, visible=True, enable=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portalId=23, visible=True, enable=True, minimapVisible=True) # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 시작대기중
