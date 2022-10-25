""" trigger/51000002_dg/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020], isVisible=True)
        self.arcade_boom_boom_ocean(type='StartGame', lifeCount=20)
        self.select_camera_path(pathIds=[8001], returnView=False) # 카메라 뒤로 당김
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[99], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        self.set_timer(timerId='6100', seconds=6100)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료체크(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 종료체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[99])


class 종료체크(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
