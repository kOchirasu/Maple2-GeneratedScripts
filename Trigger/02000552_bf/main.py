""" trigger/02000552_bf/main.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # 미술관 전투판으로 가는 포탈 최초 감추기, 메인 전투판에 있는 포탈
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # 미술관 전투판으로 가는 포탈 최초 감추기, 최초 시작 지점 2층 지형에 있는 포탈
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False) # 장난감 전투판으로 되돌아가는 포탈 최초 감추기
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기
        self.set_user_value(key='NextPortal', value=0) # NextPortal변수 0으로 초기 셋팅, 다음 전투판 이동할때 숨겨진 포탈 생성시키기 위한 용도로 사용
        self.set_user_value(key='SmallRemove', value=0) # SmallRemove변수 0으로 초기 셋팅, 작아짐 디버프 제거 하는데 사용하는 용도, 만약을 위한 장치임
        self.set_user_value(key='VacuumMessage', value=0) # VacuumMessage변수 0으로 초기 셋팅, 진공청소기 흡수도니 플레이어 있으면 메시지 출력 하기 위한 용도

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 난이도체크(self.ctx)


class 난이도체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_id(dungeonId=23050003):
            return 쉬운난이도보스등장(self.ctx)
        if self.dungeon_id(dungeonId=23051003):
            return 여려움난이도보스등장(self.ctx)
        if self.wait_tick(waitTick=1100):
            return 여려움난이도보스등장(self.ctx)


class 여려움난이도보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 101 어려움 난이도

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 보스전투중(self.ctx)


class 쉬운난이도보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음 , 스폰ID 102 쉬운 난이도

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 보스전투중(self.ctx)


class 보스전투중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SmallRemove', value=1):
            return 작아짐제거(self.ctx)
        if self.user_value(key='VacuumMessage', value=1):
            return 메시지출력(self.ctx)
        if self.user_value(key='NextPortal', value=1):
            return 다음이동포탈등장(self.ctx)
        if self.user_value(key='End', value=1):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 메시지출력(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=29200008, textId=29200008, duration=6200)
        self.set_user_value(key='VacuumMessage', value=0) # VacuumMessage변수 0으로 초기 셋팅

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 보스전투중(self.ctx)


class 작아짐제거(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[702], skillId=50001556, level=1, isPlayer=False, isSkillSet=False) # 플레이어가 진공청소기 공격 받아서 작아졌는데, 흡수 안되는 이상한 버그가 있어서 만약을 위한 장치로 작아짐 걸렸으면, 여기서 풀어주도록 함
        self.add_buff(boxIds=[701], skillId=50001556, level=1, isPlayer=False, isSkillSet=False) # 플레이어가 진공청소기 공격 받아서 작아졌는데, 흡수 안되는 이상한 버그가 있어서 만약을 위한 장치로 작아짐 걸렸으면, 여기서 풀어주도록 함
        self.set_user_value(key='SmallRemove', value=0) # SmallRemove변수 0으로 초기 셋팅

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 보스전투중(self.ctx)


class 다음이동포탈등장(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True) # 미술관 전투판으로 가는 포탈 등장하기, 메인 전투판에 있는 포탈
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True) # 미술관 전투판으로 가는 포탈 등장하기, 최초 시작지점 2층 지형에 있는 포탈
        self.add_buff(boxIds=[702], skillId=50001556, level=1, isPlayer=False, isSkillSet=False) # 플레이어가 진공청소기 공격 받아서 작아졌는데, 흡수 안되는 이상한 버그가 있어서 만약을 위한 장치로 작아짐 걸렸으면, 여기서 풀어주도록 함
        self.add_buff(boxIds=[701], skillId=50001556, level=1, isPlayer=False, isSkillSet=False) # 플레이어가 진공청소기 공격 받아서 작아졌는데, 흡수 안되는 이상한 버그가 있어서 만약을 위한 장치로 작아짐 걸렸으면, 여기서 풀어주도록 함
        self.set_user_value(key='NextPortal', value=0) # NextPortal변수 0으로 초기 셋팅
        self.set_user_value(key='SmallRemove', value=0) # SmallRemove변수 0으로 초기 셋팅, 혹시 모르니 만약을 위한 장치

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return 보스전투중(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_fail()
            return 게임오버(self.ctx)


class 게임오버(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0') # 701 는 두번째 전투판 영역, 702는 첫번째 전투판 영역, 블랙빈 죽여 클리어 했는데도, 대미지 필드 때문에 죽는 안타까운 상황이 생길 수 있어서 블랙빈 죽이면 바로 플레이어에게 8초간 무적버프 걸어서 죽지 않게 해줌
        self.add_buff(boxIds=[701], skillId=50000266, level=1, isPlayer=False, isSkillSet=False) # 플레이어에게 무적 버프 & 진공청소기 흡수에 의한 소인화 디버프 제거, 혹시 바닥 RYB 대미지에맞아서 클리어 했는데 죽는 경우를 막기 위해
        self.add_buff(boxIds=[702], skillId=50000266, level=1, isPlayer=False, isSkillSet=False) # 플레이어에게 무적 버프 & 진공청소기 흡수에 의한 소인화 디버프 제거, 혹시 바닥 RYB 대미지에맞아서 클리어 했는데 죽는 경우를 막기 위해

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료딜레이(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=50000266, level=1, isPlayer=False, isSkillSet=False) # 플레이어에게 무적 버프 & 진공청소기 흡수에 의한 소인화 디버프 제거, 혹시 바닥 RYB 대미지에맞아서 클리어 했는데 죽는 경우를 막기 위해
        self.add_buff(boxIds=[702], skillId=50000266, level=1, isPlayer=False, isSkillSet=False) # 플레이어에게 무적 버프 & 진공청소기 흡수에 의한 소인화 디버프 제거, 혹시 바닥 RYB 대미지에맞아서 클리어 했는데 죽는 경우를 막기 위해

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 클리어처리(self.ctx)


class 클리어처리(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True) # 나가기 포탈 등장
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True) # 나가기 포탈 등장
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True) # 장난감 전투판으로 되돌아가는 포탈 등장


initial_state = 시작대기중
