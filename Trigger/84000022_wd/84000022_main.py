""" trigger/84000022_wd/84000022_main.xml """
from common import *
import state


class 초기화(state.State):
    def on_enter(self):
        set_user_value(key='Weddingceremonystarts', value=0)
        set_portal(portalId=99, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 결혼식연출시작요청대기()


class 결혼식연출시작요청대기(state.State):
    def on_enter(self):
        lock_my_pc(isLock=False) # PC 움직임 풀어줌 (초기화)
        hide_guide_summary(entityId=28400140) # 알수없는오류로결혼식재진행필요하다는안내메시지 삭제 / 스트링 ID 신규발급 필요

    def on_tick(self) -> state.State:
        if user_value(key='Weddingceremonystarts', value=1):
            set_user_value(key='Weddingceremonystarts', value=0)
            lock_my_pc(isLock=True)
            return 시작알림()


class 시작알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400134, textId=28400134) # 결혼식 시작한다는 메시지

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출시작()

    def on_exit(self):
        hide_guide_summary(entityId=28400134)


class 연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        wedding_move_user(entryType='Guest', mapId=84000022, portalIds=[22,23], boxId=701) # 799번 박스(입장구역)에 있는 하객들은 22,23번으로 랜덤이동
        wedding_move_user(entryType='Guest', mapId=84000022, portalIds=[22,23], boxId=703) # 701번 박스(버진로드)에 있는 하객들은 22,23번으로 랜덤이동
        wedding_move_user(entryType='Groom', mapId=84000022, portalIds=[11], boxId=702) # 신랑 11번으로
        wedding_move_user(entryType='Bride', mapId=84000022, portalIds=[12], boxId=702) # 신부는 12번으로
        set_portal(portalId=99, visible=True, enabled=True, minimapVisible=True) # 입,출구포털 활성화	/ 중간탈주 케이스 발생할 경우 나갈 수 있도록

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 주례줌인01()


class 주례줌인01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[8002,8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 주례줌인02()


class 주례줌인02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__0$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시선돌리기01()


class 시선돌리기01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세레나데()


class 세레나데(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return UI테스트()


class UI테스트(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 입장준비01()


class 입장준비01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8009], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 입장준비02()


class 입장준비02(state.State):
    def on_enter(self):
        wedding_set_user_emotion(entryType='Bride', id=6)
        wedding_set_user_emotion(entryType='Groom', id=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 입장01()


class 입장01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8005], returnView=False)
        wedding_user_to_patrol(patrolName='MS2PatrolData_2001', entryType='Groom', patrolIndex=1) # 신랑 경로이동
        wedding_user_to_patrol(patrolName='MS2PatrolData_2002', entryType='Bride', patrolIndex=2) # 신부 경로이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라이동01()


class 카메라이동01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 카메라이동02()


class 카메라이동02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102]) # 세레나데 끝

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 주례사()


class 주례사(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__1$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 성혼타이핑결과확인()


class 성혼타이핑결과확인(state.State):
    def on_enter(self):
        wedding_mutual_agree(agreeType='partnerName')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            wedding_mutual_cancel(agreeType='partnerName')
            return 미입력으로중단01()
        if wedding_entry_in_field(entryType='GroomBride', isInField=False):
            wedding_mutual_cancel(agreeType='partnerName')
            return 탈주로중단()
        if wedding_mutual_agree_result(agreeType='partnerName', success=False):
            return 탈주로중단()
        if wedding_mutual_agree_result(agreeType='partnerName', success=True):
            return 성혼발표()


class 탈주로중단(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 탈주로중단선언()


class 탈주로중단선언(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 탈주로중단선언리셋()


class 미입력으로중단01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미입력으로중단선언()


class 미입력으로중단선언(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 탈주로중단선언리셋()


class 탈주로중단선언리셋(state.State):
    def on_enter(self):
        set_user_value(triggerId=4002, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 moveguest에 쏘는 신호
        set_user_value(triggerId=4000, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 wait에 쏘는 신호
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if true():
            return 결혼식연출시작요청대기()


class 성혼발표(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004723, msg='$84000022_WD__84000022_MAIN__6$', duration=2500)
        wedding_vow_complete() # 결혼식 완료 후 신랑신부 보상 부여하는 명령
        set_user_value(triggerId=4002, key='WeddingFinished', value=1) # 하객 옮기기 그만하라고 moveguest에 쏘는 신호
        wedding_set_user_look_at(entryType='Bride', lookAtEntryType='Groom', immediate=True)
        wedding_set_user_look_at(entryType='Groom', lookAtEntryType='Bride', immediate=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 환호성()


class 환호성(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        wedding_set_user_emotion(entryType='Bride', id=4)
        wedding_set_user_emotion(entryType='Groom', id=4)
        play_system_sound_in_box(sound='System_WeddingAudience_01') # 임시사운드 : 박수소리, 환호소리 들어가면 좋을 듯

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 뒷풀이01()


class 뒷풀이01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보상과결혼상태마지막체크()


class 보상과결혼상태마지막체크(state.State):
    def on_enter(self):
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wedding_hall_state(hallState='weddingComplete', success=True):
            return 뒷풀이02()
        if true():
            return 보상결혼상태체크실패()


class 보상결혼상태체크실패(state.State):
    def on_enter(self):
        set_user_value(triggerId=4002, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 moveguest에 쏘는 신호
        set_user_value(triggerId=4000, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 wait에 쏘는 신호
        show_guide_summary(entityId=28400140) # 알수없는오류로결혼식재진행필요하다는안내메시지 / 스트링 ID 신규발급 필요

    def on_tick(self) -> state.State:
        if true():
            return 결혼식연출시작요청대기()


class 뒷풀이02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400135, textId=28400135) # 기념촬영과뒷풀이 즐기세요 메시지
        set_portal(portalId=99, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 뒷풀이03()

    def on_exit(self):
        hide_guide_summary(entityId=28400135)


class 뒷풀이03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400136, textId=28400136) # 주례에게 말 걸어 결혼식 끝내라는 메시지
        set_user_value(key='EndWedding', value=0) # 결혼종료확인 초기화

    def on_tick(self) -> state.State:
        if user_value(key='EndWedding', value=1):
            return 결혼종료확인()

    def on_exit(self):
        hide_guide_summary(entityId=28400136)


class 결혼종료확인(state.State):
    def on_enter(self):
        wedding_mutual_agree(agreeType='endActing') # 결혼식 종료여부 투표 ui 띄우기? / npc한테 말을 걸었는지 아닌지를 이걸로 체크할 수 있나? / 시간제한은 어떻게 체크하나?

    def on_tick(self) -> state.State:
        if wedding_entry_in_field(entryType='GroomBride', isInField=False):
            return 종료알림()
        if wedding_mutual_agree_result(agreeType='endActing', success=True):
            return 종료알림()
        if wedding_mutual_agree_result(agreeType='endActing', success=False):
            return 뒷풀이03()
        """
        <condition name="시간이경과했으면" arg1="8400131">
            <transition state="강퇴안내" />
        </condition>
        """


class 종료알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400137, textId=28400137) # 결혼식장 폐쇄한다는 메시지

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 끄읏()

    def on_exit(self):
        hide_guide_summary(entityId=28400137)


class 끄읏(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


