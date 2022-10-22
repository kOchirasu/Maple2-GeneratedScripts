""" trigger/51000002_dg/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020], isVisible=True)
        arcade_boom_boom_ocean(type='StartGame', lifeCount=20)
        select_camera_path(pathIds=[8001], returnView=False) # 카메라 뒤로 당김
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[99], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        set_timer(timerId='6100', seconds=6100)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료체크()
        if monster_dead(boxIds=[99]):
            return 종료체크()

    def on_exit(self):
        destroy_monster(spawnIds=[99])


class 종료체크(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


