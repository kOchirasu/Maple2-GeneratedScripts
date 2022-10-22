""" trigger/02000346_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[9001], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        set_ladder(triggerIds=[9002], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        set_ladder(triggerIds=[9003], visible=False, animationEffect=False, animationDelay=0) # 사다리 가려
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        set_interact_object(triggerIds=[10000791], state=0) # 보상 상태 (없음)
        set_mesh(triggerIds=[6001,6010], visible=True) # 벽 생성
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=False) # 길 차단

    def on_tick(self) -> state.State:
        if count_users(boxId=60001, boxId=1):
            return 오브젝티브_01()


class 오브젝티브_01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 오브젝티브_02()


class 오브젝티브_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=True)
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[101], arg2=True) # 보스 등장
        set_cinematic_ui(type=3, script='$02000346_BF__MAIN1__0$') # 오브젝티브
        set_timer(timerId='5', seconds=5, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 시작_01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


#    플레이어 감지하면 1초 대기 
class 시작_01(state.State):
    def on_enter(self):
        show_count_ui(text='$02000346_BF__MAIN1__2$', stage=0, count=3)
        set_timer(timerId='3', seconds=3, display=False)
        set_mesh(triggerIds=[6001], visible=False) # 가림막

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 시작_02()


class 시작_02(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[9001], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        set_ladder(triggerIds=[9002], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여
        set_ladder(triggerIds=[9003], visible=True, animationEffect=True, animationDelay=0) # 사다리 보여

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 클리어()


class 클리어(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (on)
        set_event_ui(type=7, arg2='$02000346_BF__MAIN1__1$', arg3='3000')
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, arg4=0, arg5=10) # 길 생성
        set_mesh(triggerIds=[6010], visible=False, arg4=0, arg5=0) # 벽 삭제
        set_interact_object(triggerIds=[10000791], state=1) # 보상 상태 (없음)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 클리어_02()


class 클리어_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=110, textId=40009) # 포탈 이용하세요


