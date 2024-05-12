""" trigger/52020001_qd/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[40001], enable=False)
        self.set_skill(triggerIds=[6001], enable=False)
        self.set_interact_object(triggerIds=[10002001], state=2)
        self.set_interact_object(triggerIds=[10002002], state=2)
        self.set_interact_object(triggerIds=[10002003], state=2)
        self.create_monster(spawnIds=[6000020], animationEffect=False)
        self.set_effect(triggerIds=[10090], visible=False)
        self.set_effect(triggerIds=[10091], visible=False)
        self.set_effect(triggerIds=[10092], visible=False)
        self.set_mesh(triggerIds=[80000], visible=False, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[5]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인트로_카메라(self.ctx)


class 인트로_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=2000012, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인트로_폭발_1(self.ctx)


class 인트로_폭발_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10011], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 인트로_폭발_2(self.ctx)


class 인트로_폭발_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 인트로_폭발_3(self.ctx)


class 인트로_폭발_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 인트로_폭발_4(self.ctx)


class 인트로_폭발_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10014], visible=True)
        self.set_skill(triggerIds=[6001], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 인트로_종료(self.ctx)


class 인트로_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(triggerId=2000012, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='시간이 얼마 없습니다.\\n폭격을 일삼는 에고웨폰들을 처치하며 크리티아스로 침투하세요.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 감지(self.ctx)


class 감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1]):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='100', seconds=180, startDelay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 몬스터출현_1(self.ctx)


"""
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None # Missing State: 대기_2

"""


"""
class 대기_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=2000004, enable=True)
        self.set_conversation(type=2, script='저 녀석의 공격을 조심해야 겠어...', arg4=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return None # Missing State: 대기_초기화

"""


"""
class 대기_초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(triggerId=2000004, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 알림(self.ctx)

"""


class 몬스터출현_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[40001], enable=True)
        self.create_monster(spawnIds=[6000001], animationEffect=False)
        self.create_monster(spawnIds=[6000002], animationEffect=False)
        self.create_monster(spawnIds=[6000003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터사망_1(self.ctx)
        if self.time_expired(timerId='100'):
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.set_conversation(type=1, spawnId=0, script='서둘러야 해!', arg4=3, arg5=0)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6000001]) and self.monster_dead(boxIds=[6000002]) and self.monster_dead(boxIds=[6000003]):
            return 몬스터출현_2(self.ctx)
        if self.time_expired(timerId='100'):
            return 실패(self.ctx)


class 몬스터출현_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[6000004], animationEffect=False)
        self.create_monster(spawnIds=[6000005], animationEffect=False)
        self.create_monster(spawnIds=[6000006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터사망_2(self.ctx)
        if self.time_expired(timerId='100'):
            return 실패(self.ctx)


class 몬스터사망_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6000004]) and self.monster_dead(boxIds=[6000005]) and self.monster_dead(boxIds=[6000006]):
            return 스위치생성연출(self.ctx)
        if self.time_expired(timerId='100'):
            return 실패(self.ctx)


class 스위치생성연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='100')
        self.destroy_monster(spawnIds=[6100001])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 스위치생성연출_카메라(self.ctx)


class 스위치생성연출_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=2000003, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 생성_1(self.ctx)


class 생성_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002001], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스위치생성연출_카메라_초기화(self.ctx)


class 스위치생성연출_카메라_초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(triggerId=2000003, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 작동(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[6100001], animationEffect=False)
        self.set_conversation(type=1, spawnId=0, script='저 스위치를 한번 작동시켜 볼까?', arg4=3, arg5=0)


class 작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002001], stateValue=0):
            return 연출시작_1(self.ctx)


class 연출시작_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[6100001])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 발사_카메라연출_1(self.ctx)


class 발사_카메라연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=2000001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 폭발배경연출_1(self.ctx)


class 폭발배경연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10028], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 폭발배경연출_2(self.ctx)


class 폭발배경연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10029], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 폭발_1(self.ctx)


class 폭발_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 날라감_1(self.ctx)


class 날라감_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera_path(pathIds=[2000002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return pc소환(self.ctx)


class pc소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52020001, portalId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 폭발배경연출_3(self.ctx)


class 폭발배경연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10023], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return 폭발배경연출_4(self.ctx)


class 폭발배경연출_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10024], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 폭발배경연출_5(self.ctx)


class 폭발배경연출_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10025], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return 맵폭발연출_1(self.ctx)


class 맵폭발연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10021], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return 맵폭발연출_2(self.ctx)


class 폭발배경연출_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10026], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 폭발배경연출_7(self.ctx)


class 폭발배경연출_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10027], visible=True)
        self.set_skill(triggerIds=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 맵폭발연출_2(self.ctx)


class 맵폭발연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10022], visible=True)
        self.set_skill(triggerIds=[6003], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=15, visible=True, enable=True, minimapVisible=False)
        self.reset_camera(interpolationTime=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            pass


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[10090], visible=True)
        self.set_effect(triggerIds=[10091], visible=True)
        self.set_effect(triggerIds=[10092], visible=True)
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[-1])
        self.set_event_ui(type=1, arg2='미션에 실패하였습니다. 다시 재도전 해보세요.', arg3='4000')
        self.move_user(mapId=52020001, portalId=99)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            pass


initial_state = 시작
