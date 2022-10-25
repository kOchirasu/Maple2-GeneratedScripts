""" trigger/02000410_bf/etcset.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 타이머(self.ctx)


class 타이머(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=28000):
            self.set_event_ui(type=1, arg2='$02000410_BF__BARRICADE_GIVEUP_0$', arg3='5000')
            self.dungeon_enable_give_up(isEnable='1')
            return 입구포탈제거(self.ctx)


class 입구포탈제거(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
            return 보스HP체크(self.ctx)


class 보스HP체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_damage(spawnId=102, damageRate=1):
            self.add_buff(boxIds=[102], skillId=50004522, level=1, isPlayer=True)
            self.dungeon_mission_complete(feature='DungeonRankBalance_01', missionId=24090004)
            self.dungeon_mission_complete(feature='DungeonRankBalance_02', missionId=24090014)
            return 메시지알림(self.ctx)
        """
        condition name="CheckNpcDamage"   파라미터 기능 설명
        
                    spawnPointID: 체크할 NPC스폰포인트ID 스포너 안에 여러 NPC가 있을 경우 맨 첫 NPC를 체크합니다. 
                    damageRate: 누적 대미지 기준 값 1.0 일경우 해당 npc의 maxHP 0.5의 경우 50% 
                    operator: 연산자 기준 입니다 생략시 해당 값 이상 (GreaterEqual 이며) 다음 옵션을 사용 가능합니다. 
                    Greater,
                    GreaterEqual,
                    Equal,
                    LessEqual,
                    Less,
        """


class 메시지알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20041005, textId=20041005) # 인페르녹의 쉴드가 사라졌다는 것을 메시지로 알려줌

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20041005)


class 종료(common.Trigger):
    pass


initial_state = Ready
