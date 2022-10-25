""" trigger/02020142_bf/timecheck.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 던전시간체크(self.ctx)


class 던전시간체크(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=41, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=42, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=43, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=44, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=45, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=46, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=47, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=48, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=49, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.destroy_monster(spawnIds=[-1]) # 던전 Fail 처리, 던전 나가기 포탈 생성하기
        self.set_portal(portalId=41, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=42, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=43, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=44, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=45, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=46, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=47, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=48, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=49, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 시작대기중
