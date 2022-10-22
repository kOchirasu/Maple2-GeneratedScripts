""" trigger/02000410_bf/etcset.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 타이머()


class 타이머(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=28000):
            set_event_ui(type=1, arg2='$02000410_BF__BARRICADE_GIVEUP_0$', arg3='5000')
            dungeon_enable_give_up(isEnable='1')
            return 입구포탈제거()


class 입구포탈제거(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
            return 보스HP체크()


class 보스HP체크(state.State):
    def on_tick(self) -> state.State:
        if check_npc_damage(spawnId=102, damageRate=1):
            add_buff(boxIds=[102], skillId=50004522, level=1, arg4=True)
            dungeon_mission_complete(feature='DungeonRankBalance_01', missionId=24090004)
            dungeon_mission_complete(feature='DungeonRankBalance_02', missionId=24090014)
            return 메시지알림()
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


class 메시지알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041005, textId=20041005) # 인페르녹의 쉴드가 사라졌다는 것을 메시지로 알려줌

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=20041005)


class 종료(state.State):
    pass


