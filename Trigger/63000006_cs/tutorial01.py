""" trigger/63000006_cs/tutorial01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_widget(type='Guide')
        set_portal(portalId=1, visible=True, enabled=False, minimapVisible=True)
        set_skill(triggerIds=[900], isEnable=False)
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)
        set_skill(triggerIds=[903], isEnable=False)
        set_skill(triggerIds=[904], isEnable=False)
        set_skill(triggerIds=[905], isEnable=False)
        set_skill(triggerIds=[906], isEnable=False)
        set_skill(triggerIds=[907], isEnable=False)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # bridge 1st barrier ON
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # bridge 2nd  barrier ON
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0) # bridge left guide barrier ON
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0) # bridge right guide barrier ON
        set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0) # bridge 3rd guide barrier OFF
        set_effect(triggerIds=[5011], visible=False) # bridge enter 01
        set_effect(triggerIds=[5012], visible=False) # bridge enter 02
        set_effect(triggerIds=[5013], visible=False) # bridge enter 03
        set_effect(triggerIds=[5014], visible=False) # bridge enter 04
        set_effect(triggerIds=[5015], visible=False) # bridge enter 05
        set_effect(triggerIds=[5000], visible=False) # move point 1
        set_effect(triggerIds=[5001], visible=False) # move point 2
        set_effect(triggerIds=[5012], visible=False) # bridge enter 03
        set_effect(triggerIds=[5013], visible=False) # bridge enter 04
        set_effect(triggerIds=[5020], visible=False) # after swim 01
        set_effect(triggerIds=[5021], visible=False) # after swim 02
        set_effect(triggerIds=[5022], visible=False) # after swim 03
        set_effect(triggerIds=[5023], visible=False) # after swim 04
        set_effect(triggerIds=[5024], visible=False) # after swim 05
        set_effect(triggerIds=[5025], visible=False) # after swim 06
        set_effect(triggerIds=[5026], visible=False) # after swim 07
        set_effect(triggerIds=[5027], visible=False) # after swim 08
        set_effect(triggerIds=[5028], visible=False) # after swim 09
        set_effect(triggerIds=[5040], visible=False) # toward portal 01
        set_effect(triggerIds=[5041], visible=False) # toward portal 02
        set_effect(triggerIds=[5042], visible=False) # toward portal 03
        set_effect(triggerIds=[5043], visible=False) # toward portal 04
        set_effect(triggerIds=[5044], visible=False) # toward portal 05
        set_effect(triggerIds=[5045], visible=False) # toward portal 06
        set_effect(triggerIds=[5046], visible=False) # toward portal 07
        set_effect(triggerIds=[5047], visible=False) # toward portal 08
        set_effect(triggerIds=[5048], visible=False) # toward portal 09
        set_effect(triggerIds=[5050], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5051], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5052], visible=False) # 화살표  안내 사운드 이펙트
        set_effect(triggerIds=[5060], visible=False) # 이슈라 음성 사운드 이펙트 01
        set_effect(triggerIds=[5061], visible=False) # 이슈라 음성 사운드 이펙트 02
        set_effect(triggerIds=[5062], visible=False) # 이슈라 음성 사운드 이펙트 03
        set_effect(triggerIds=[5063], visible=False) # 이슈라 음성 사운드 이펙트 04
        set_effect(triggerIds=[5064], visible=False) # 이슈라 음성 사운드 이펙트 05
        set_effect(triggerIds=[5065], visible=False) # 이슈라 음성 사운드 이펙트 06
        set_effect(triggerIds=[5066], visible=False) # 이슈라 음성 사운드 이펙트 07
        set_effect(triggerIds=[5080], visible=False) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        set_effect(triggerIds=[5090], visible=False) # PC 물에 빠질 때 풍덩 사운드  이펙트
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 영상준비_01()


class 영상준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생_01()


class 영상재생_01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\Common_Opening.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 룬블영상준비_01()
        if wait_tick(waitTick=190000):
            return 룬블영상준비_01()


class 룬블영상준비_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 룬블영상재생_01()


class 룬블영상재생_01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\RuneBlader_Intro.usm', movieId=2)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='2'):
            return 룬블영상완료_01()
        if wait_tick(waitTick=30000):
            return 룬블영상완료_01()


class 룬블영상완료_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 키타입설정안내01()
        if user_detected(boxIds=[9050,9051,9052,9053]):
            return 로딩딜레이()


class 키타입설정안내01(state.State):
    def on_enter(self):
        guide_event(eventId=10010005) # 트리거 To가이드 : 키타입설정

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10010009'):
            return 플레이준비()


class 플레이준비(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010001, textId=10010001) # 가이드 : 화살표 키를 눌러 움직이기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9050,9051,9052,9053]):
            return 로딩딜레이()

    def on_exit(self):
        hide_guide_summary(entityId=10010001)


class 로딩딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 기상준비01()


class 기상준비01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_999')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 기상대화01()


class 기상대화01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=4)
        set_effect(triggerIds=[5060], visible=True) # 이슈라 음성 사운드 이펙트 01
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__0$', arg4=4)
        set_skip(state=움직이기01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 움직이기01()

    def on_exit(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 움직이기01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 목표지점 바닥
        set_effect(triggerIds=[5001], visible=True) # 목표지점 화살표
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10010000, textId=10010000) # 가이드 : 화살표 키를 눌러 움직이기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[6001]):
            return 움직이기02()

    def on_exit(self):
        set_effect(triggerIds=[5060], visible=False) # 이슈라 음성 사운드 이펙트 01


class 움직이기02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_998')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[6000]):
            return 이동완료01()

    def on_exit(self):
        set_effect(triggerIds=[5051], visible=True) # 미션 완료 사운드 이펙트
        hide_guide_summary(entityId=10010000)


class 이동완료01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 목표지점 바닥
        set_effect(triggerIds=[5001], visible=False) # 목표지점 화살표
        move_npc(spawnId=101, patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if true():
            return 이동전대화01()

    def on_exit(self):
        set_effect(triggerIds=[5050], visible=False) # 가이드 서머리 사운드 이펙트


class 이동전대화01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return 이동전대화02()


class 이동전대화02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__1$', arg4=3)
        set_effect(triggerIds=[5061], visible=True) # 이슈라 음성 사운드 이펙트 02

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 이동전대화03()


class 이동전대화03(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__2$', arg4=3)
        set_effect(triggerIds=[5061], visible=False) # 이슈라 음성 사운드 이펙트 02
        set_effect(triggerIds=[5062], visible=True) # 이슈라 음성 사운드 이펙트 03
        set_skip(state=미니맵가이드01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 미니맵가이드01()

    def on_exit(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


#  트리거 To가이드  
class 미니맵가이드01(state.State):
    def on_enter(self):
        guide_event(eventId=10010010) # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='10010020'):
            return 이슈라이동01()


class 이슈라이동01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=101, script='$63000006_CS__TUTORIAL01__3$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 이슈라이동02()


class 이슈라이동02(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=1)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 이슈라이동03()


class 이슈라이동03(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=4)
        set_conversation(type=1, spawnId=101, script='$63000006_CS__TUTORIAL01__4$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 이슈라이동04()


class 이슈라이동04(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=4)
        set_conversation(type=1, spawnId=101, script='$63000006_CS__TUTORIAL01__5$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 이슈라이동05()


class 이슈라이동05(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=101, script='$63000006_CS__TUTORIAL01__6$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다리연출준비()


class 다리연출준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8002, spawnIds=[101]):
            return 다리연출01()


class 다리연출01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__7$', arg4=3)
        set_effect(triggerIds=[5064], visible=True) # 이슈라 음성 사운드 이펙트 05
        set_skip(state=다리연출02)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 다리연출02()

    def on_exit(self):
        remove_cinematic_talk()


class 다리연출02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        set_effect(triggerIds=[5080], visible=True) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        move_npc(spawnId=101, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8004, spawnIds=[101]):
            return 다리연출03()


class 다리연출03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8005, spawnIds=[101]):
            return 다리연출종료()


class 다리연출종료(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000006_CS__TUTORIAL01__8$', arg4=3)
        set_effect(triggerIds=[5080], visible=False) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        set_effect(triggerIds=[5064], visible=False) # 이슈라 음성 사운드 이펙트 05
        set_effect(triggerIds=[5011], visible=True) # bridge enter 01
        set_effect(triggerIds=[5012], visible=True) # bridge enter 02
        set_effect(triggerIds=[5013], visible=True) # bridge enter 03
        set_effect(triggerIds=[5014], visible=True) # bridge enter 04
        set_effect(triggerIds=[5015], visible=True) # bridge enter 05
        show_guide_summary(entityId=10010020, textId=10010020) # 가이드 : 이슈라에게 이동하기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5052], visible=True) # 화살표  안내 사운드 이펙트

    def on_tick(self) -> state.State:
        if true():
            return 다리붕괴01()


class 다리붕괴01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0) # 1st bridge barrier OFF

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 다리붕괴02()

    def on_exit(self):
        set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0) # bridge 3rd guide barrier ON
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0) # bridge left guide barrier OFF
        set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0) # bridge right guide barrier OFF
        hide_guide_summary(entityId=10010020)
        set_effect(triggerIds=[5050], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5052], visible=False) # 화살표  안내 사운드 이펙트
        set_effect(triggerIds=[5011], visible=False) # bridge enter 01
        set_effect(triggerIds=[5012], visible=False) # bridge enter 02
        set_effect(triggerIds=[5013], visible=False) # bridge enter 03
        set_effect(triggerIds=[5014], visible=False) # bridge enter 04
        set_effect(triggerIds=[5015], visible=False) # bridge enter 05


class 다리붕괴02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[902], isEnable=True)
        set_skill(triggerIds=[906], isEnable=True)
        set_effect(triggerIds=[5090], visible=True) # PC 물에 빠질 때 풍덩 사운드  이펙트

    def on_tick(self) -> state.State:
        if true():
            return 다리붕괴03()


class 다리붕괴03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[900], isEnable=True)
        set_skill(triggerIds=[904], isEnable=True)
        set_skill(triggerIds=[901], isEnable=True)
        set_skill(triggerIds=[905], isEnable=True)

    def on_tick(self) -> state.State:
        if true():
            return 다리붕괴04()


class 다리붕괴04(state.State):
    def on_enter(self):
        set_skill(triggerIds=[903], isEnable=True)

    def on_tick(self) -> state.State:
        if true():
            return 다리붕괴05()


class 다리붕괴05(state.State):
    def on_enter(self):
        set_skill(triggerIds=[907], isEnable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9004]):
            return 수영안내01()

    def on_exit(self):
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)
        set_skill(triggerIds=[903], isEnable=False)
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # bridge barrier OFF
        set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0) # bridge 3rd guide barrier OFF


class 수영안내01(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5090], visible=False) # PC 물에 빠질 때 풍덩 사운드  이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 수영안내02()


class 수영안내02(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__9$', arg4=3)
        set_effect(triggerIds=[5065], visible=True) # 이슈라 음성 사운드 이펙트 06

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 수영안내03()


class 수영안내03(state.State):
    def on_enter(self):
        set_timer(timerId='32', seconds=3)
        set_conversation(type=2, spawnId=11001244, script='$63000006_CS__TUTORIAL01__10$', arg4=3)
        set_effect(triggerIds=[5065], visible=False) # 이슈라 음성 사운드 이펙트 06
        set_effect(triggerIds=[5066], visible=True) # 이슈라 음성 사운드 이펙트 07
        set_skip(state=이슈라교체)

    def on_tick(self) -> state.State:
        if time_expired(timerId='32'):
            return 이슈라교체()

    def on_exit(self):
        remove_cinematic_talk()


class 이슈라교체(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010030, textId=10010030) # 가이드 : 방향키를 눌러 수영하기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5020], visible=True) # after swim 01
        set_effect(triggerIds=[5021], visible=True) # after swim 02
        set_effect(triggerIds=[5022], visible=True) # after swim 03
        set_effect(triggerIds=[5023], visible=True) # after swim 04
        set_effect(triggerIds=[5024], visible=True) # after swim 05
        set_effect(triggerIds=[5025], visible=True) # after swim 06
        set_effect(triggerIds=[5026], visible=True) # after swim 07
        set_effect(triggerIds=[5027], visible=True) # after swim 08
        set_effect(triggerIds=[5028], visible=True) # after swim 09
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8006, spawnIds=[101]):
            return 연출05종료()

    def on_exit(self):
        set_effect(triggerIds=[5066], visible=False) # 이슈라 음성 사운드 이펙트 07


class 연출05종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9010,9011,9012,9013,9014,9015]):
            return 사다리유도01()

    def on_exit(self):
        hide_guide_summary(entityId=10010030)


class 사다리유도01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010020, textId=10010020) # 가이드 : 이슈라에게 이동하기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9006]):
            return 사다리유도02()

    def on_exit(self):
        hide_guide_summary(entityId=10010020)


class 사다리유도02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010040, textId=10010040) # 가이드 : ↑키를 눌러 사다리 올라가기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5040], visible=True) # toward portal 01

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9005]):
            return 언덕유도01()

    def on_exit(self):
        hide_guide_summary(entityId=10010040)


class 언덕유도01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010020, textId=10010020) # 가이드 : 이슈라에게 이동하기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5041], visible=True) # toward portal 02
        set_effect(triggerIds=[5042], visible=True) # toward portal 03
        set_effect(triggerIds=[5043], visible=True) # toward portal 04
        set_effect(triggerIds=[5044], visible=True) # toward portal 05
        set_effect(triggerIds=[5045], visible=True) # toward portal 06
        set_effect(triggerIds=[5046], visible=True) # toward portal 07
        set_effect(triggerIds=[5047], visible=True) # toward portal 08
        set_effect(triggerIds=[5048], visible=True) # toward portal 09

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9020]):
            return 언덕유도02()

    def on_exit(self):
        hide_guide_summary(entityId=10010020)


class 언덕유도02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010050, textId=10010050) # 가이드 : C키로 점프하여 언덕 올라가기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9021]):
            return 퀘스트수락유도01()

    def on_exit(self):
        hide_guide_summary(entityId=10010050)


class 퀘스트수락유도01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010060, textId=10010060) # 가이드 : 이슈라와 대화해서 퀘스트 수락하기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9030], questIds=[90000410], questStates=[1]):
            return 포털생성01()

    def on_exit(self):
        hide_guide_summary(entityId=10010060)
        set_effect(triggerIds=[5040], visible=False) # toward portal 01
        set_effect(triggerIds=[5041], visible=False) # toward portal 02
        set_effect(triggerIds=[5042], visible=False) # toward portal 03
        set_effect(triggerIds=[5043], visible=False) # toward portal 04
        set_effect(triggerIds=[5044], visible=False) # toward portal 05
        set_effect(triggerIds=[5045], visible=False) # toward portal 06
        set_effect(triggerIds=[5046], visible=False) # toward portal 07
        set_effect(triggerIds=[5020], visible=False) # after swim 01
        set_effect(triggerIds=[5021], visible=False) # after swim 02
        set_effect(triggerIds=[5022], visible=False) # after swim 03
        set_effect(triggerIds=[5023], visible=False) # after swim 04
        set_effect(triggerIds=[5024], visible=False) # after swim 05
        set_effect(triggerIds=[5025], visible=False) # after swim 06
        set_effect(triggerIds=[5026], visible=False) # after swim 07
        set_effect(triggerIds=[5027], visible=False) # after swim 08
        set_effect(triggerIds=[5028], visible=False) # after swim 09


class 포털생성01(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=1)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        guide_event(eventId=10010080) # 트리거 To가이드 : 포털 위에 노란색 화살표 타겟팅
        show_guide_summary(entityId=10010070, textId=10010070) # 가이드 : 포털 위치에서 스페이스 키 누르기
        set_effect(triggerIds=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 이슈라퇴장01()


class 이슈라퇴장01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$63000006_CS__TUTORIAL01__11$', arg4=3)
        move_npc(spawnId=102, patrolName='MS2PatrolData_1004')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8008, spawnIds=[102]):
            return 이슈라퇴장02()

    def on_exit(self):
        set_effect(triggerIds=[5050], visible=False) # 가이드 서머리 사운드 이펙트


class 이슈라퇴장02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9040]):
            return 맵이동완료()


class 맵이동완료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10010070)
        set_effect(triggerIds=[5047], visible=False) # toward portal 08
        set_effect(triggerIds=[5048], visible=False) # toward portal 09


