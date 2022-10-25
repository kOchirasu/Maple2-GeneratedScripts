""" trigger/02020120_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.dungeon_reset_time(seconds=720) # 던전 시간 12분 설정 초기화 하기 , 이 던전의 시간 설정은 DoungeonRoom.xml 이 아닌 여기서 진행함
        self.side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__0$', duration=4000, voice='ko/Npc/00002192')
        self.create_monster(spawnIds=[99], animationEffect=False) # 이슈라 등장
        self.set_portal(portalId=9901, visible=False, enable=False, minimapVisible=False) # 버그 때문에 이거 사용 안함, 그렇다고 이거 지우면 대박 버그 생기니 조심 그냥 내버려 두자, 다시 처음으로 되돌리는 순간이동 포탈 Off 처리 하는거 여기서 하기, 스킬브레이크 막기 실패하여 던전 초기화 될 경우를 대비해 여기서 초기화 처리 하는 것이 좋음, 보스 메인 전투판 주변 범위의 포발
        self.set_portal(portalId=9902, visible=False, enable=False, minimapVisible=False) # 버그 때문에 이거 사용 안함, 그렇다고 이거 지우면 대박 버그 생기니 조심 그냥 내버려 두자, 다시 처음으로 되돌리는 순간이동 포탈 Off 처리 하는거 여기서 하기, 스킬브레이크 막기 실패하여 던전 초기화 될 경우를 대비해 여기서 초기화 처리 하는 것이 좋음, 스타팅 포인트 근처 주변 범위의 포발

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DungeonReset', value=1):
            return 던전초기화진행(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 던전초기화진행(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020120, portalId=9903) # 맵 안에 있는 모든 플레이어를 스타팅 지점에 있는 포탈로 이동시킴, arg1 은 이동시킬 맵 코드, arg2 은 도착 장소 포탈ID 임
        self.set_sound(triggerId=19601, enable=True) # 던전 초기화 되면 노말 BGM으로 교체함, 보스 BGM 교체 설정은 BgmChangeSkillBreakReset.xml 트리거에 설정 되어있음
        self.side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_smile', script='$02020120_BF__BOSSSPAWN__1$', duration=7000, voice='ko/Npc/00002193')
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 던전초기화시간등각종설정(self.ctx)


class 던전초기화시간등각종설정(common.Trigger):
    def on_enter(self):
        self.dungeon_stop_timer()
        self.set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수 0 초기화 하기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 보스등장(self.ctx)


class 종료딜레이(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__2$', duration=6576, voice='ko/Npc/00002194')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            self.set_skill(triggerIds=[2222], enable=False)
            self.set_skill(triggerIds=[1212], enable=False)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_clear()
            self.dungeon_set_end_time()
            self.set_achievement(achieve='IshuraDungeonClear')
            return 종료(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_skill(triggerIds=[2222], enable=False)
            self.set_skill(triggerIds=[1212], enable=False)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2101, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2301, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3101, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3102, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3103, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3104, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3202, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3203, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3301, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3302, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3303, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3304, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3305, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3306, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4101, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4102, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4202, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4301, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4302, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5101, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5102, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5202, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5203, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5204, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5205, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5206, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5301, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5302, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5303, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5304, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5401, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6101, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6201, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6301, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6302, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6303, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6304, visible=True, enable=True, minimapVisible=True)
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 시작대기중
