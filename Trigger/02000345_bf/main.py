""" trigger/02000345_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
# 60002 : 모든 영역
class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002], visible=True, arg3=1, delay=1)
        self.remove_buff(boxId=60002, skillId=99910040)
        self.remove_buff(boxId=60002, skillId=70000106)
        self.create_monster(spawnIds=[102], animationEffect=True) # 촬영 감독
        self.set_mesh(triggerIds=[6010], visible=True) # 벽 생성
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=60001, boxId=1):
            return CheckUserCount(self.ctx)
        if self.wait_tick(waitTick=5000):
            return start_game_01(self.ctx)


class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return touchfield(self.ctx)


class touchfield(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002], visible=False, arg3=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_random_user(mapId=2000345, portalId=99, triggerId=702, count=1)
        self.move_random_user(mapId=2000345, portalId=98, triggerId=60005, count=1)
        self.move_random_user(mapId=2000345, portalId=97, triggerId=60005, count=1)
        self.move_random_user(mapId=2000345, portalId=96, triggerId=60005, count=1)
        self.select_camera_path(pathIds=[8801,8802], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_01(self.ctx)


class start_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8802,8803], returnView=False)
        self.set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__0$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_02(self.ctx)


class start_02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__2$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__3$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_03(self.ctx)


class start_03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__4$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__5$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_04(self.ctx)


class start_04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000345_BF__MAIN__6$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__7$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_05(self.ctx)


class start_05(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[702], skillId=70000106, level=1) # 카메라 스크린을 걸어준다.
        self.select_camera_path(pathIds=[8804,8805,8806,8807], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_06(self.ctx)


class start_06(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__8$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_07(self.ctx)


class start_07(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001376, script='$02000345_BF__MAIN__9$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_game(self.ctx)


class start_game(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[8808], returnView=True)
        self.show_count_ui(text='$02000345_BF__MAIN__10$', stage=0, count=3)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_game_01(self.ctx)


class start_game_01(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN__11$', arg3='3000')
        self.create_monster(spawnIds=[189], animationEffect=True, animationDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_game_02(self.ctx)


class start_game_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8809,8810], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_game_02_b(self.ctx)


class start_game_02_b(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__12$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__13$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_game_03(self.ctx)


class start_game_03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__14$', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__15$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_game_04(self.ctx)


class start_game_04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=189, script='$02000345_BF__MAIN__16$', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=11001890, script='$02000345_BF__MAIN__17$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return start_game_05(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[8808], returnView=True)


class start_game_05(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN__18$', arg3='3000')
        self.create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210], animationEffect=True, animationDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206,207,208,209,210]):
            return start_game_06(self.ctx)


class start_game_06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304,305,306,307], animationEffect=True, animationDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305,306,307]):
            return start_game_07(self.ctx)


class start_game_07(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401,402,403,404,405,406], animationEffect=True, animationDelay=0)


class 대기_01(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(triggerIds=[10000791], state=0) # 보상 상태 (없음)
        self.set_mesh(triggerIds=[6001,6010], visible=True) # 벽 생성
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단
        self.set_ladder(triggerIds=[9001], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        self.set_ladder(triggerIds=[9002], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[9003], visible=False, animationEffect=False, animationDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=60001, boxId=1):
            return 대기_02(self.ctx)


class 대기_02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기_03(self.ctx)


class 대기_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=60001, boxId=1):
            return 오브젝티브_01(self.ctx)


class 오브젝티브_01(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN1__2$', arg3='10000')
        self.set_timer(timerId='10', seconds=10, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 오브젝티브_02(self.ctx)


class 오브젝티브_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001,8002], returnView=True)
        self.create_monster(spawnIds=[101], animationEffect=True) # 보스 등장
        self.set_cinematic_ui(type=1)
        # <action name="유저를이동시킨다" arg1="02000345" arg2="3"/>
        self.set_cinematic_ui(type=3, script='$02000345_BF__MAIN1__0$') # 오브젝티브
        self.set_timer(timerId='5', seconds=5, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 시작_01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 플레이어 감지하면 1초 대기
class 시작_01(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$02000345_BF__MAIN1__3$', stage=0, count=3)
        self.set_timer(timerId='3', seconds=3, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 시작_02(self.ctx)


class 시작_02(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[9001], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        self.set_ladder(triggerIds=[9002], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        self.set_ladder(triggerIds=[9003], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 클리어(self.ctx)


class 클리어(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_event_ui(type=7, arg2='$02000345_BF__MAIN1__1$', arg3='3000')
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, delay=0, scale=10) # 길 생성
        self.set_mesh(triggerIds=[6010], visible=False, delay=0, scale=0) # 벽 삭제
        self.set_interact_object(triggerIds=[10000791], state=1) # 보상 상태 (없음)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 클리어_02(self.ctx)


class 클리어_02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요


initial_state = 대기
