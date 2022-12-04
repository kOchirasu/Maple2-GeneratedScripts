""" trigger/02000551_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=9, visible=False, enable=False, minimapVisible=False) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=25, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id(dungeonId=23050003):
            return 쉬운난이도보스등장(self.ctx)
        if self.dungeon_id(dungeonId=23051003):
            return 여려움난이도보스등장(self.ctx)
        if self.wait_tick(waitTick=1100):
            return 여려움난이도보스등장(self.ctx)


class 여려움난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 101 어려움 난이도

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1800):
            return 일러스트대화창(self.ctx)


class 쉬운난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 102 쉬운 난이도

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1800):
            return 일러스트대화창(self.ctx)


class 일러스트대화창(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23000101, illust='BlackBean_Smile', script='$02000551_BF__BOSSSPAWN__0$', duration=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2100):
            return 전투진행중(self.ctx)


class 전투진행중(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='GuideMessage', value=0) # GuideMessage 0으로 초기 셋팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GuideMessage', value=1):
            return 메시지출력(self.ctx)
        if self.user_value(key='NextPortal', value=1):
            return 다음진행딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 메시지출력(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=29200007, textId=29200007, duration=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 전투진행중(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_fail()
            return 게임오버(self.ctx)


class 게임오버(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')
        # StartPortal.xml 트리거에서 <action name="DungeonEnableGiveUp" isEnable="1" /> 설정함
        self.set_portal(portalId=21, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=22, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=23, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=24, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=25, visible=True, enable=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)


class 다음진행딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5800):
            return 다음맵가는포탈등장(self.ctx)


class 다음맵가는포탈등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
