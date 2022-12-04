""" trigger/02000348_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
# 60002 : 모든 영역
class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=34808, key='cage_01', value=0)
        self.set_user_value(triggerId=34805, key='cage_02', value=0)
        self.set_user_value(triggerId=34806, key='cage_03', value=0)
        self.set_user_value(triggerId=34807, key='cage_04', value=0)
        self.set_mesh(triggerIds=[2001,2002], visible=True, arg3=1, delay=1)
        self.remove_buff(boxId=60002, skillId=99910040)
        self.remove_buff(boxId=60002, skillId=70000106)
        self.create_monster(spawnIds=[102], animationEffect=True) # 촬영 감독
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(triggerIds=[10000789], state=0) # 보상 상태 (없음)
        self.set_mesh(triggerIds=[6010], visible=True) # 벽 생성
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=60001, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return touchfield(self.ctx)


class touchfield(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002], visible=False, arg3=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_random_user(mapId=2000348, portalId=99, triggerId=702, count=1)
        self.move_random_user(mapId=2000348, portalId=98, triggerId=60005, count=1)
        self.move_random_user(mapId=2000348, portalId=97, triggerId=60005, count=1)
        self.move_random_user(mapId=2000348, portalId=96, triggerId=60005, count=1)
        self.select_camera_path(pathIds=[8801,8802], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_01(self.ctx)


class start_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8802,8803], returnView=False)
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__0$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__1$', arg4=3)
        self.set_skip(state=start_game)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__2$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__4$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__5$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__6$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__7$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[702], skillId=70000106, level=1) # 카메라 스크린을 걸어준다.
        self.select_camera_path(pathIds=[8804,8805,8806,8807], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__8$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__9$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_game(self.ctx)


class start_game(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[702], skillId=70000106, level=1) # 카메라 스크린을 걸어준다.
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[8808], returnView=True)
        self.show_count_ui(text='$02000348_BF__MAIN__10$', stage=0, count=3)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_game_01(self.ctx)


class start_game_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003446, textId=20003446, duration=5000)
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__11$', arg3='3000')
        self.create_monster(spawnIds=[201,202,203,204,211,212,213,214], animationEffect=True)
        self.set_user_value(triggerId=34808, key='cage_01', value=1)
        self.set_user_value(triggerId=34805, key='cage_02', value=1)
        self.set_user_value(triggerId=34806, key='cage_03', value=1)
        self.set_user_value(triggerId=34807, key='cage_04', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[211,212,213,214]):
            return start_game_02(self.ctx)


class start_game_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_game_03(self.ctx)


class start_game_03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003442, textId=20003442, duration=5000)
        self.create_monster(spawnIds=[231,232], animationEffect=True)
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__12$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_game_03_a(self.ctx)


class start_game_03_a(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[233,234], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[231,232,233,234]):
            return start_game_03_b(self.ctx)


class start_game_03_b(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8811,8810], returnView=True)
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__13$', arg3='3000')
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_skill(triggerIds=[7702], enable=True)
        self.set_skill(triggerIds=[7703], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return start_game_05(self.ctx)


class start_game_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__14$', arg3='3000')
        self.create_monster(spawnIds=[101,205,206,207,208], animationEffect=True) # 촬영 감독

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return start_game_06(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[205,206,207,208])


class start_game_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.remove_buff(boxId=60002, skillId=99910040)
        self.remove_buff(boxId=60002, skillId=70000106)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, delay=0, scale=10) # 길 생성
        self.set_mesh(triggerIds=[6010], visible=False, delay=0, scale=0) # 벽 삭제
        self.set_interact_object(triggerIds=[10000789], state=1) # 보상 상태 (없음)
        self.set_timer(timerId='5', seconds=5)
        self.select_camera_path(pathIds=[8801,8803], returnView=False)
        self.set_skip(state=클리어_03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 클리어_02(self.ctx)


class 클리어_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__15$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000348_BF__MAIN__16$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클리어_03(self.ctx)


class 클리어_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__MAIN__17$', arg4=2, arg5=0)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클리어_04(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[102])


class 클리어_04(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=1, value=1) # 1번 던전 클리어 처리
        self.show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요
        self.select_camera_path(pathIds=[8808], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
