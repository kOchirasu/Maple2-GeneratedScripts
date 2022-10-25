""" trigger/02000252_bf/start.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[151,152,153,154,155,156], visible=True)
        self.set_effect(triggerIds=[601], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[602], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[603], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[8009], visible=False)
        self.set_effect(triggerIds=[8010], visible=False)
        self.set_effect(triggerIds=[8011], visible=False)
        self.set_effect(triggerIds=[8012], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 로딩딜레이(self.ctx)


class 로딩딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002521)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라소환(self.ctx)


class 연출해제(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라소환(self.ctx)


class 벨라소환(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8801,8802], returnView=False)
        self.create_monster(spawnIds=[1001])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 벨라대사(self.ctx)


class 벨라대사(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=벨라스킬딜레이, action='nextState')
        self.set_skip(state=벨라스킬딜레이)
        self.set_timer(timerId='1', seconds=6)
        # action name="이펙트를설정한다" arg1="601" arg2="1"/
        self.set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__4$', arg4=3)
        # action name="스킵을설정한다" arg1="벨라스킬딜레이" /

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=8)
        # <action name="이펙트를설정한다" arg1="602" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__5$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_scene_skip()
        # <action name="이펙트를설정한다" arg1="603" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__6$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6243):
            return 벨라스킬딜레이(self.ctx)


class 벨라스킬딜레이(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1')
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 예고이펙트(self.ctx)


class 예고이펙트(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8804], returnView=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=999, type='trigger', achieve='Bellafirst')
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_effect(triggerIds=[8008], visible=True)
        self.set_effect(triggerIds=[8009], visible=True)
        self.set_effect(triggerIds=[8010], visible=True)
        self.set_effect(triggerIds=[8011], visible=True)
        self.set_effect(triggerIds=[8012], visible=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 스킬시작대기(self.ctx)


class 스킬시작대기(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002522, textId=20002522)
        self.set_mesh(triggerIds=[151,152,153,154,155,156], visible=False)
        self.create_monster(spawnIds=[1051], animationEffect=False)
        self.create_monster(spawnIds=[1052], animationEffect=False)
        self.create_monster(spawnIds=[1053], animationEffect=False)
        self.create_monster(spawnIds=[1054], animationEffect=False)
        self.create_monster(spawnIds=[1055], animationEffect=False)
        self.create_monster(spawnIds=[1056], animationEffect=False)
        self.create_monster(spawnIds=[1057], animationEffect=False)
        self.create_monster(spawnIds=[1058], animationEffect=False)
        self.create_monster(spawnIds=[1059], animationEffect=False)
        self.create_monster(spawnIds=[1060], animationEffect=False)
        self.create_monster(spawnIds=[1061], animationEffect=False)
        self.create_monster(spawnIds=[1062], animationEffect=False)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            self.destroy_monster(spawnIds=[1001])
            return 스킬시작대기2(self.ctx)


class 스킬시작대기2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[8009], visible=False)
        self.set_effect(triggerIds=[8010], visible=False)
        self.set_effect(triggerIds=[8011], visible=False)
        self.set_effect(triggerIds=[8012], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 스킬To08(self.ctx)


class 스킬To08(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[515], enable=True)
        self.set_skill(triggerIds=[516], enable=True)
        self.set_skill(triggerIds=[517], enable=True)
        self.set_skill(triggerIds=[518], enable=True)
        self.set_skill(triggerIds=[519], enable=True)
        self.set_skill(triggerIds=[520], enable=True)
        self.set_skill(triggerIds=[521], enable=True)
        self.set_skill(triggerIds=[522], enable=True)
        self.set_skill(triggerIds=[523], enable=True)
        self.set_skill(triggerIds=[524], enable=True)
        self.set_skill(triggerIds=[525], enable=True)
        self.set_skill(triggerIds=[526], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To07대기(self.ctx)


class 스킬To07대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[515], enable=False)
        self.set_skill(triggerIds=[516], enable=False)
        self.set_skill(triggerIds=[517], enable=False)
        self.set_skill(triggerIds=[518], enable=False)
        self.set_skill(triggerIds=[519], enable=False)
        self.set_skill(triggerIds=[520], enable=False)
        self.set_skill(triggerIds=[521], enable=False)
        self.set_skill(triggerIds=[522], enable=False)
        self.set_skill(triggerIds=[523], enable=False)
        self.set_skill(triggerIds=[524], enable=False)
        self.set_skill(triggerIds=[525], enable=False)
        self.set_skill(triggerIds=[526], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To07(self.ctx)


class 스킬To07(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[564], enable=True)
        self.set_skill(triggerIds=[517], enable=True)
        self.set_skill(triggerIds=[518], enable=True)
        self.set_skill(triggerIds=[519], enable=True)
        self.set_skill(triggerIds=[520], enable=True)
        self.set_skill(triggerIds=[521], enable=True)
        self.set_skill(triggerIds=[522], enable=True)
        self.set_skill(triggerIds=[523], enable=True)
        self.set_skill(triggerIds=[524], enable=True)
        self.set_skill(triggerIds=[525], enable=True)
        self.set_skill(triggerIds=[526], enable=True)
        self.set_skill(triggerIds=[527], enable=True)
        self.set_skill(triggerIds=[528], enable=True)
        self.set_skill(triggerIds=[529], enable=True)
        self.set_skill(triggerIds=[530], enable=True)
        self.set_skill(triggerIds=[531], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To06대기(self.ctx)


class 스킬To06대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[564], enable=False)
        self.set_skill(triggerIds=[517], enable=False)
        self.set_skill(triggerIds=[518], enable=False)
        self.set_skill(triggerIds=[519], enable=False)
        self.set_skill(triggerIds=[520], enable=False)
        self.set_skill(triggerIds=[521], enable=False)
        self.set_skill(triggerIds=[522], enable=False)
        self.set_skill(triggerIds=[523], enable=False)
        self.set_skill(triggerIds=[524], enable=False)
        self.set_skill(triggerIds=[525], enable=False)
        self.set_skill(triggerIds=[526], enable=False)
        self.set_skill(triggerIds=[527], enable=False)
        self.set_skill(triggerIds=[528], enable=False)
        self.set_skill(triggerIds=[529], enable=False)
        self.set_skill(triggerIds=[530], enable=False)
        self.set_skill(triggerIds=[531], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To06(self.ctx)


class 스킬To06(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[565], enable=True)
        self.set_skill(triggerIds=[564], enable=True)
        self.set_skill(triggerIds=[522], enable=True)
        self.set_skill(triggerIds=[523], enable=True)
        self.set_skill(triggerIds=[524], enable=True)
        self.set_skill(triggerIds=[525], enable=True)
        self.set_skill(triggerIds=[526], enable=True)
        self.set_skill(triggerIds=[527], enable=True)
        self.set_skill(triggerIds=[528], enable=True)
        self.set_skill(triggerIds=[529], enable=True)
        self.set_skill(triggerIds=[530], enable=True)
        self.set_skill(triggerIds=[531], enable=True)
        self.set_skill(triggerIds=[532], enable=True)
        self.set_skill(triggerIds=[533], enable=True)
        self.set_skill(triggerIds=[534], enable=True)
        self.set_skill(triggerIds=[535], enable=True)
        self.set_skill(triggerIds=[536], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To05대기(self.ctx)


class 스킬To05대기(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002522)
        self.set_skill(triggerIds=[565], enable=False)
        self.set_skill(triggerIds=[564], enable=False)
        self.set_skill(triggerIds=[522], enable=False)
        self.set_skill(triggerIds=[523], enable=False)
        self.set_skill(triggerIds=[524], enable=False)
        self.set_skill(triggerIds=[525], enable=False)
        self.set_skill(triggerIds=[526], enable=False)
        self.set_skill(triggerIds=[527], enable=False)
        self.set_skill(triggerIds=[528], enable=False)
        self.set_skill(triggerIds=[529], enable=False)
        self.set_skill(triggerIds=[530], enable=False)
        self.set_skill(triggerIds=[531], enable=False)
        self.set_skill(triggerIds=[532], enable=False)
        self.set_skill(triggerIds=[533], enable=False)
        self.set_skill(triggerIds=[534], enable=False)
        self.set_skill(triggerIds=[535], enable=False)
        self.set_skill(triggerIds=[536], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To05(self.ctx)


class 스킬To05(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[566], enable=True)
        self.set_skill(triggerIds=[567], enable=True)
        self.set_skill(triggerIds=[568], enable=True)
        self.set_skill(triggerIds=[565], enable=True)
        self.set_skill(triggerIds=[564], enable=True)
        self.set_skill(triggerIds=[527], enable=True)
        self.set_skill(triggerIds=[528], enable=True)
        self.set_skill(triggerIds=[529], enable=True)
        self.set_skill(triggerIds=[530], enable=True)
        self.set_skill(triggerIds=[531], enable=True)
        self.set_skill(triggerIds=[532], enable=True)
        self.set_skill(triggerIds=[533], enable=True)
        self.set_skill(triggerIds=[534], enable=True)
        self.set_skill(triggerIds=[535], enable=True)
        self.set_skill(triggerIds=[536], enable=True)
        self.set_skill(triggerIds=[537], enable=True)
        self.set_skill(triggerIds=[538], enable=True)
        self.set_skill(triggerIds=[539], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To04대기(self.ctx)


class 스킬To04대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[566], enable=False)
        self.set_skill(triggerIds=[567], enable=False)
        self.set_skill(triggerIds=[568], enable=False)
        self.set_skill(triggerIds=[565], enable=False)
        self.set_skill(triggerIds=[564], enable=False)
        self.set_skill(triggerIds=[527], enable=False)
        self.set_skill(triggerIds=[528], enable=False)
        self.set_skill(triggerIds=[529], enable=False)
        self.set_skill(triggerIds=[530], enable=False)
        self.set_skill(triggerIds=[531], enable=False)
        self.set_skill(triggerIds=[532], enable=False)
        self.set_skill(triggerIds=[533], enable=False)
        self.set_skill(triggerIds=[534], enable=False)
        self.set_skill(triggerIds=[535], enable=False)
        self.set_skill(triggerIds=[536], enable=False)
        self.set_skill(triggerIds=[537], enable=False)
        self.set_skill(triggerIds=[538], enable=False)
        self.set_skill(triggerIds=[539], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To04(self.ctx)


class 스킬To04(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[566], enable=False)
        self.set_skill(triggerIds=[567], enable=False)
        self.set_skill(triggerIds=[568], enable=False)
        self.set_skill(triggerIds=[565], enable=True)
        self.set_skill(triggerIds=[532], enable=True)
        self.set_skill(triggerIds=[533], enable=True)
        self.set_skill(triggerIds=[534], enable=True)
        self.set_skill(triggerIds=[535], enable=True)
        self.set_skill(triggerIds=[536], enable=True)
        self.set_skill(triggerIds=[537], enable=True)
        self.set_skill(triggerIds=[538], enable=True)
        self.set_skill(triggerIds=[539], enable=True)
        self.set_skill(triggerIds=[540], enable=True)
        self.set_skill(triggerIds=[541], enable=True)
        self.set_skill(triggerIds=[542], enable=True)
        self.set_skill(triggerIds=[543], enable=True)
        self.set_skill(triggerIds=[544], enable=True)
        self.set_skill(triggerIds=[545], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To03대기(self.ctx)


class 스킬To03대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[566], enable=False)
        self.set_skill(triggerIds=[567], enable=False)
        self.set_skill(triggerIds=[568], enable=False)
        self.set_skill(triggerIds=[565], enable=False)
        self.set_skill(triggerIds=[532], enable=False)
        self.set_skill(triggerIds=[533], enable=False)
        self.set_skill(triggerIds=[534], enable=False)
        self.set_skill(triggerIds=[535], enable=False)
        self.set_skill(triggerIds=[536], enable=False)
        self.set_skill(triggerIds=[537], enable=False)
        self.set_skill(triggerIds=[538], enable=False)
        self.set_skill(triggerIds=[539], enable=False)
        self.set_skill(triggerIds=[540], enable=False)
        self.set_skill(triggerIds=[541], enable=False)
        self.set_skill(triggerIds=[542], enable=False)
        self.set_skill(triggerIds=[543], enable=False)
        self.set_skill(triggerIds=[544], enable=False)
        self.set_skill(triggerIds=[545], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To03(self.ctx)


class 스킬To03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[566], enable=True)
        self.set_skill(triggerIds=[567], enable=True)
        self.set_skill(triggerIds=[568], enable=True)
        self.set_skill(triggerIds=[537], enable=True)
        self.set_skill(triggerIds=[538], enable=True)
        self.set_skill(triggerIds=[539], enable=True)
        self.set_skill(triggerIds=[540], enable=True)
        self.set_skill(triggerIds=[541], enable=True)
        self.set_skill(triggerIds=[542], enable=True)
        self.set_skill(triggerIds=[543], enable=True)
        self.set_skill(triggerIds=[544], enable=True)
        self.set_skill(triggerIds=[545], enable=True)
        self.set_skill(triggerIds=[546], enable=True)
        self.set_skill(triggerIds=[547], enable=True)
        self.set_skill(triggerIds=[548], enable=True)
        self.set_skill(triggerIds=[549], enable=True)
        self.set_skill(triggerIds=[550], enable=True)
        self.set_skill(triggerIds=[551], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To02대기(self.ctx)


class 스킬To02대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[566], enable=False)
        self.set_skill(triggerIds=[567], enable=False)
        self.set_skill(triggerIds=[568], enable=False)
        self.set_skill(triggerIds=[537], enable=False)
        self.set_skill(triggerIds=[538], enable=False)
        self.set_skill(triggerIds=[539], enable=False)
        self.set_skill(triggerIds=[540], enable=False)
        self.set_skill(triggerIds=[541], enable=False)
        self.set_skill(triggerIds=[542], enable=False)
        self.set_skill(triggerIds=[543], enable=False)
        self.set_skill(triggerIds=[544], enable=False)
        self.set_skill(triggerIds=[545], enable=False)
        self.set_skill(triggerIds=[546], enable=False)
        self.set_skill(triggerIds=[547], enable=False)
        self.set_skill(triggerIds=[548], enable=False)
        self.set_skill(triggerIds=[549], enable=False)
        self.set_skill(triggerIds=[550], enable=False)
        self.set_skill(triggerIds=[551], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To02(self.ctx)


class 스킬To02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[540], enable=True)
        self.set_skill(triggerIds=[541], enable=True)
        self.set_skill(triggerIds=[542], enable=True)
        self.set_skill(triggerIds=[543], enable=True)
        self.set_skill(triggerIds=[544], enable=True)
        self.set_skill(triggerIds=[545], enable=True)
        self.set_skill(triggerIds=[546], enable=True)
        self.set_skill(triggerIds=[547], enable=True)
        self.set_skill(triggerIds=[548], enable=True)
        self.set_skill(triggerIds=[549], enable=True)
        self.set_skill(triggerIds=[550], enable=True)
        self.set_skill(triggerIds=[551], enable=True)
        self.set_skill(triggerIds=[552], enable=True)
        self.set_skill(triggerIds=[553], enable=True)
        self.set_skill(triggerIds=[554], enable=True)
        self.set_skill(triggerIds=[555], enable=True)
        self.set_skill(triggerIds=[556], enable=True)
        self.set_skill(triggerIds=[557], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬To01대기(self.ctx)


class 스킬To01대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[540], enable=False)
        self.set_skill(triggerIds=[541], enable=False)
        self.set_skill(triggerIds=[542], enable=False)
        self.set_skill(triggerIds=[543], enable=False)
        self.set_skill(triggerIds=[544], enable=False)
        self.set_skill(triggerIds=[545], enable=False)
        self.set_skill(triggerIds=[546], enable=False)
        self.set_skill(triggerIds=[547], enable=False)
        self.set_skill(triggerIds=[548], enable=False)
        self.set_skill(triggerIds=[549], enable=False)
        self.set_skill(triggerIds=[550], enable=False)
        self.set_skill(triggerIds=[551], enable=False)
        self.set_skill(triggerIds=[552], enable=False)
        self.set_skill(triggerIds=[553], enable=False)
        self.set_skill(triggerIds=[554], enable=False)
        self.set_skill(triggerIds=[555], enable=False)
        self.set_skill(triggerIds=[556], enable=False)
        self.set_skill(triggerIds=[557], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬To01(self.ctx)


class 스킬To01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[546], enable=True)
        self.set_skill(triggerIds=[547], enable=True)
        self.set_skill(triggerIds=[548], enable=True)
        self.set_skill(triggerIds=[549], enable=True)
        self.set_skill(triggerIds=[550], enable=True)
        self.set_skill(triggerIds=[551], enable=True)
        self.set_skill(triggerIds=[552], enable=True)
        self.set_skill(triggerIds=[553], enable=True)
        self.set_skill(triggerIds=[554], enable=True)
        self.set_skill(triggerIds=[555], enable=True)
        self.set_skill(triggerIds=[556], enable=True)
        self.set_skill(triggerIds=[557], enable=True)
        self.set_skill(triggerIds=[558], enable=True)
        self.set_skill(triggerIds=[559], enable=True)
        self.set_skill(triggerIds=[560], enable=True)
        self.set_skill(triggerIds=[561], enable=True)
        self.set_skill(triggerIds=[562], enable=True)
        self.set_skill(triggerIds=[563], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬00대기(self.ctx)


class 스킬00대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[546], enable=False)
        self.set_skill(triggerIds=[547], enable=False)
        self.set_skill(triggerIds=[548], enable=False)
        self.set_skill(triggerIds=[549], enable=False)
        self.set_skill(triggerIds=[550], enable=False)
        self.set_skill(triggerIds=[551], enable=False)
        self.set_skill(triggerIds=[552], enable=False)
        self.set_skill(triggerIds=[553], enable=False)
        self.set_skill(triggerIds=[554], enable=False)
        self.set_skill(triggerIds=[555], enable=False)
        self.set_skill(triggerIds=[556], enable=False)
        self.set_skill(triggerIds=[557], enable=False)
        self.set_skill(triggerIds=[558], enable=False)
        self.set_skill(triggerIds=[559], enable=False)
        self.set_skill(triggerIds=[560], enable=False)
        self.set_skill(triggerIds=[561], enable=False)
        self.set_skill(triggerIds=[562], enable=False)
        self.set_skill(triggerIds=[563], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬00(self.ctx)


class 스킬00(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[552], enable=True)
        self.set_skill(triggerIds=[553], enable=True)
        self.set_skill(triggerIds=[554], enable=True)
        self.set_skill(triggerIds=[555], enable=True)
        self.set_skill(triggerIds=[556], enable=True)
        self.set_skill(triggerIds=[557], enable=True)
        self.set_skill(triggerIds=[558], enable=True)
        self.set_skill(triggerIds=[559], enable=True)
        self.set_skill(triggerIds=[560], enable=True)
        self.set_skill(triggerIds=[561], enable=True)
        self.set_skill(triggerIds=[562], enable=True)
        self.set_skill(triggerIds=[563], enable=True)
        self.set_skill(triggerIds=[301], enable=True)
        self.set_skill(triggerIds=[302], enable=True)
        self.set_skill(triggerIds=[303], enable=True)
        self.set_skill(triggerIds=[304], enable=True)
        self.set_skill(triggerIds=[305], enable=True)
        self.set_skill(triggerIds=[306], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬0.5대기(self.ctx)


class 스킬0.5대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[552], enable=False)
        self.set_skill(triggerIds=[553], enable=False)
        self.set_skill(triggerIds=[554], enable=False)
        self.set_skill(triggerIds=[555], enable=False)
        self.set_skill(triggerIds=[556], enable=False)
        self.set_skill(triggerIds=[557], enable=False)
        self.set_skill(triggerIds=[558], enable=False)
        self.set_skill(triggerIds=[559], enable=False)
        self.set_skill(triggerIds=[560], enable=False)
        self.set_skill(triggerIds=[561], enable=False)
        self.set_skill(triggerIds=[562], enable=False)
        self.set_skill(triggerIds=[563], enable=False)
        self.set_skill(triggerIds=[301], enable=False)
        self.set_skill(triggerIds=[302], enable=False)
        self.set_skill(triggerIds=[303], enable=False)
        self.set_skill(triggerIds=[304], enable=False)
        self.set_skill(triggerIds=[305], enable=False)
        self.set_skill(triggerIds=[306], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬0.5(self.ctx)


class 스킬0.5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[558], enable=True)
        self.set_skill(triggerIds=[559], enable=True)
        self.set_skill(triggerIds=[560], enable=True)
        self.set_skill(triggerIds=[561], enable=True)
        self.set_skill(triggerIds=[562], enable=True)
        self.set_skill(triggerIds=[563], enable=True)
        self.set_skill(triggerIds=[301], enable=True)
        self.set_skill(triggerIds=[302], enable=True)
        self.set_skill(triggerIds=[303], enable=True)
        self.set_skill(triggerIds=[304], enable=True)
        self.set_skill(triggerIds=[305], enable=True)
        self.set_skill(triggerIds=[306], enable=True)
        self.set_skill(triggerIds=[307], enable=True)
        self.set_skill(triggerIds=[308], enable=True)
        self.set_skill(triggerIds=[309], enable=True)
        self.set_skill(triggerIds=[310], enable=True)
        self.set_skill(triggerIds=[311], enable=True)
        self.set_skill(triggerIds=[312], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬01대기(self.ctx)


class 스킬01대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[558], enable=False)
        self.set_skill(triggerIds=[559], enable=False)
        self.set_skill(triggerIds=[560], enable=False)
        self.set_skill(triggerIds=[561], enable=False)
        self.set_skill(triggerIds=[562], enable=False)
        self.set_skill(triggerIds=[563], enable=False)
        self.set_skill(triggerIds=[301], enable=False)
        self.set_skill(triggerIds=[302], enable=False)
        self.set_skill(triggerIds=[303], enable=False)
        self.set_skill(triggerIds=[304], enable=False)
        self.set_skill(triggerIds=[305], enable=False)
        self.set_skill(triggerIds=[306], enable=False)
        self.set_skill(triggerIds=[307], enable=False)
        self.set_skill(triggerIds=[308], enable=False)
        self.set_skill(triggerIds=[309], enable=False)
        self.set_skill(triggerIds=[310], enable=False)
        self.set_skill(triggerIds=[311], enable=False)
        self.set_skill(triggerIds=[312], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬01(self.ctx)


class 스킬01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[301], enable=True)
        self.set_skill(triggerIds=[302], enable=True)
        self.set_skill(triggerIds=[303], enable=True)
        self.set_skill(triggerIds=[304], enable=True)
        self.set_skill(triggerIds=[305], enable=True)
        self.set_skill(triggerIds=[306], enable=True)
        self.set_skill(triggerIds=[307], enable=True)
        self.set_skill(triggerIds=[308], enable=True)
        self.set_skill(triggerIds=[309], enable=True)
        self.set_skill(triggerIds=[310], enable=True)
        self.set_skill(triggerIds=[311], enable=True)
        self.set_skill(triggerIds=[312], enable=True)
        self.set_skill(triggerIds=[313], enable=True)
        self.set_skill(triggerIds=[314], enable=True)
        self.set_skill(triggerIds=[315], enable=True)
        self.set_skill(triggerIds=[316], enable=True)
        self.set_skill(triggerIds=[317], enable=True)
        self.set_skill(triggerIds=[318], enable=True)
        self.set_skill(triggerIds=[319], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[301], enable=False)
        self.set_skill(triggerIds=[302], enable=False)
        self.set_skill(triggerIds=[303], enable=False)
        self.set_skill(triggerIds=[304], enable=False)
        self.set_skill(triggerIds=[305], enable=False)
        self.set_skill(triggerIds=[306], enable=False)
        self.set_skill(triggerIds=[307], enable=False)
        self.set_skill(triggerIds=[308], enable=False)
        self.set_skill(triggerIds=[309], enable=False)
        self.set_skill(triggerIds=[310], enable=False)
        self.set_skill(triggerIds=[311], enable=False)
        self.set_skill(triggerIds=[312], enable=False)
        self.set_skill(triggerIds=[313], enable=False)
        self.set_skill(triggerIds=[314], enable=False)
        self.set_skill(triggerIds=[315], enable=False)
        self.set_skill(triggerIds=[316], enable=False)
        self.set_skill(triggerIds=[317], enable=False)
        self.set_skill(triggerIds=[318], enable=False)
        self.set_skill(triggerIds=[319], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬02(self.ctx)


class 스킬02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[307], enable=True)
        self.set_skill(triggerIds=[308], enable=True)
        self.set_skill(triggerIds=[309], enable=True)
        self.set_skill(triggerIds=[310], enable=True)
        self.set_skill(triggerIds=[311], enable=True)
        self.set_skill(triggerIds=[312], enable=True)
        self.set_skill(triggerIds=[313], enable=True)
        self.set_skill(triggerIds=[314], enable=True)
        self.set_skill(triggerIds=[315], enable=True)
        self.set_skill(triggerIds=[316], enable=True)
        self.set_skill(triggerIds=[317], enable=True)
        self.set_skill(triggerIds=[318], enable=True)
        self.set_skill(triggerIds=[319], enable=True)
        self.set_skill(triggerIds=[320], enable=True)
        self.set_skill(triggerIds=[321], enable=True)
        self.set_skill(triggerIds=[322], enable=True)
        self.set_skill(triggerIds=[323], enable=True)
        self.set_skill(triggerIds=[324], enable=True)
        self.set_skill(triggerIds=[325], enable=True)
        self.set_skill(triggerIds=[326], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[307], enable=False)
        self.set_skill(triggerIds=[308], enable=False)
        self.set_skill(triggerIds=[309], enable=False)
        self.set_skill(triggerIds=[310], enable=False)
        self.set_skill(triggerIds=[311], enable=False)
        self.set_skill(triggerIds=[312], enable=False)
        self.set_skill(triggerIds=[313], enable=False)
        self.set_skill(triggerIds=[314], enable=False)
        self.set_skill(triggerIds=[315], enable=False)
        self.set_skill(triggerIds=[316], enable=False)
        self.set_skill(triggerIds=[317], enable=False)
        self.set_skill(triggerIds=[318], enable=False)
        self.set_skill(triggerIds=[319], enable=False)
        self.set_skill(triggerIds=[320], enable=False)
        self.set_skill(triggerIds=[321], enable=False)
        self.set_skill(triggerIds=[322], enable=False)
        self.set_skill(triggerIds=[323], enable=False)
        self.set_skill(triggerIds=[324], enable=False)
        self.set_skill(triggerIds=[325], enable=False)
        self.set_skill(triggerIds=[326], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬03(self.ctx)


class 스킬03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[313], enable=True)
        self.set_skill(triggerIds=[314], enable=True)
        self.set_skill(triggerIds=[315], enable=True)
        self.set_skill(triggerIds=[316], enable=True)
        self.set_skill(triggerIds=[317], enable=True)
        self.set_skill(triggerIds=[318], enable=True)
        self.set_skill(triggerIds=[319], enable=True)
        self.set_skill(triggerIds=[320], enable=True)
        self.set_skill(triggerIds=[321], enable=True)
        self.set_skill(triggerIds=[322], enable=True)
        self.set_skill(triggerIds=[323], enable=True)
        self.set_skill(triggerIds=[324], enable=True)
        self.set_skill(triggerIds=[325], enable=True)
        self.set_skill(triggerIds=[326], enable=True)
        self.set_skill(triggerIds=[327], enable=True)
        self.set_skill(triggerIds=[328], enable=True)
        self.set_skill(triggerIds=[329], enable=True)
        self.set_skill(triggerIds=[330], enable=True)
        self.set_skill(triggerIds=[331], enable=True)
        self.set_skill(triggerIds=[332], enable=True)
        self.set_skill(triggerIds=[333], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[313], enable=False)
        self.set_skill(triggerIds=[314], enable=False)
        self.set_skill(triggerIds=[315], enable=False)
        self.set_skill(triggerIds=[316], enable=False)
        self.set_skill(triggerIds=[317], enable=False)
        self.set_skill(triggerIds=[318], enable=False)
        self.set_skill(triggerIds=[319], enable=False)
        self.set_skill(triggerIds=[320], enable=False)
        self.set_skill(triggerIds=[321], enable=False)
        self.set_skill(triggerIds=[322], enable=False)
        self.set_skill(triggerIds=[323], enable=False)
        self.set_skill(triggerIds=[324], enable=False)
        self.set_skill(triggerIds=[325], enable=False)
        self.set_skill(triggerIds=[326], enable=False)
        self.set_skill(triggerIds=[327], enable=False)
        self.set_skill(triggerIds=[328], enable=False)
        self.set_skill(triggerIds=[329], enable=False)
        self.set_skill(triggerIds=[330], enable=False)
        self.set_skill(triggerIds=[331], enable=False)
        self.set_skill(triggerIds=[332], enable=False)
        self.set_skill(triggerIds=[333], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬04(self.ctx)


class 스킬04(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[320], enable=True)
        self.set_skill(triggerIds=[321], enable=True)
        self.set_skill(triggerIds=[322], enable=True)
        self.set_skill(triggerIds=[323], enable=True)
        self.set_skill(triggerIds=[324], enable=True)
        self.set_skill(triggerIds=[325], enable=True)
        self.set_skill(triggerIds=[326], enable=True)
        self.set_skill(triggerIds=[327], enable=True)
        self.set_skill(triggerIds=[328], enable=True)
        self.set_skill(triggerIds=[329], enable=True)
        self.set_skill(triggerIds=[330], enable=True)
        self.set_skill(triggerIds=[331], enable=True)
        self.set_skill(triggerIds=[332], enable=True)
        self.set_skill(triggerIds=[333], enable=True)
        self.set_skill(triggerIds=[334], enable=True)
        self.set_skill(triggerIds=[335], enable=True)
        self.set_skill(triggerIds=[336], enable=True)
        self.set_skill(triggerIds=[337], enable=True)
        self.set_skill(triggerIds=[338], enable=True)
        self.set_skill(triggerIds=[339], enable=True)
        self.set_skill(triggerIds=[340], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬05대기(self.ctx)


class 스킬05대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[320], enable=False)
        self.set_skill(triggerIds=[321], enable=False)
        self.set_skill(triggerIds=[322], enable=False)
        self.set_skill(triggerIds=[323], enable=False)
        self.set_skill(triggerIds=[324], enable=False)
        self.set_skill(triggerIds=[325], enable=False)
        self.set_skill(triggerIds=[326], enable=False)
        self.set_skill(triggerIds=[327], enable=False)
        self.set_skill(triggerIds=[328], enable=False)
        self.set_skill(triggerIds=[329], enable=False)
        self.set_skill(triggerIds=[330], enable=False)
        self.set_skill(triggerIds=[331], enable=False)
        self.set_skill(triggerIds=[332], enable=False)
        self.set_skill(triggerIds=[333], enable=False)
        self.set_skill(triggerIds=[334], enable=False)
        self.set_skill(triggerIds=[335], enable=False)
        self.set_skill(triggerIds=[336], enable=False)
        self.set_skill(triggerIds=[337], enable=False)
        self.set_skill(triggerIds=[338], enable=False)
        self.set_skill(triggerIds=[339], enable=False)
        self.set_skill(triggerIds=[340], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬05(self.ctx)


class 스킬05(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[327], enable=True)
        self.set_skill(triggerIds=[328], enable=True)
        self.set_skill(triggerIds=[329], enable=True)
        self.set_skill(triggerIds=[330], enable=True)
        self.set_skill(triggerIds=[331], enable=True)
        self.set_skill(triggerIds=[332], enable=True)
        self.set_skill(triggerIds=[333], enable=True)
        self.set_skill(triggerIds=[334], enable=True)
        self.set_skill(triggerIds=[335], enable=True)
        self.set_skill(triggerIds=[336], enable=True)
        self.set_skill(triggerIds=[337], enable=True)
        self.set_skill(triggerIds=[338], enable=True)
        self.set_skill(triggerIds=[339], enable=True)
        self.set_skill(triggerIds=[340], enable=True)
        self.set_skill(triggerIds=[341], enable=True)
        self.set_skill(triggerIds=[342], enable=True)
        self.set_skill(triggerIds=[343], enable=True)
        self.set_skill(triggerIds=[344], enable=True)
        self.set_skill(triggerIds=[345], enable=True)
        self.set_skill(triggerIds=[346], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[327], enable=False)
        self.set_skill(triggerIds=[328], enable=False)
        self.set_skill(triggerIds=[329], enable=False)
        self.set_skill(triggerIds=[330], enable=False)
        self.set_skill(triggerIds=[331], enable=False)
        self.set_skill(triggerIds=[332], enable=False)
        self.set_skill(triggerIds=[333], enable=False)
        self.set_skill(triggerIds=[334], enable=False)
        self.set_skill(triggerIds=[335], enable=False)
        self.set_skill(triggerIds=[336], enable=False)
        self.set_skill(triggerIds=[337], enable=False)
        self.set_skill(triggerIds=[338], enable=False)
        self.set_skill(triggerIds=[339], enable=False)
        self.set_skill(triggerIds=[340], enable=False)
        self.set_skill(triggerIds=[341], enable=False)
        self.set_skill(triggerIds=[342], enable=False)
        self.set_skill(triggerIds=[343], enable=False)
        self.set_skill(triggerIds=[344], enable=False)
        self.set_skill(triggerIds=[345], enable=False)
        self.set_skill(triggerIds=[346], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬06(self.ctx)


class 스킬06(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[334], enable=True)
        self.set_skill(triggerIds=[335], enable=True)
        self.set_skill(triggerIds=[336], enable=True)
        self.set_skill(triggerIds=[337], enable=True)
        self.set_skill(triggerIds=[338], enable=True)
        self.set_skill(triggerIds=[339], enable=True)
        self.set_skill(triggerIds=[340], enable=True)
        self.set_skill(triggerIds=[341], enable=True)
        self.set_skill(triggerIds=[342], enable=True)
        self.set_skill(triggerIds=[343], enable=True)
        self.set_skill(triggerIds=[344], enable=True)
        self.set_skill(triggerIds=[345], enable=True)
        self.set_skill(triggerIds=[346], enable=True)
        self.set_skill(triggerIds=[347], enable=True)
        self.set_skill(triggerIds=[348], enable=True)
        self.set_skill(triggerIds=[349], enable=True)
        self.set_skill(triggerIds=[350], enable=True)
        self.set_skill(triggerIds=[351], enable=True)
        self.set_skill(triggerIds=[352], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬07대기(self.ctx)


class 스킬07대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[334], enable=False)
        self.set_skill(triggerIds=[335], enable=False)
        self.set_skill(triggerIds=[336], enable=False)
        self.set_skill(triggerIds=[337], enable=False)
        self.set_skill(triggerIds=[338], enable=False)
        self.set_skill(triggerIds=[339], enable=False)
        self.set_skill(triggerIds=[340], enable=False)
        self.set_skill(triggerIds=[341], enable=False)
        self.set_skill(triggerIds=[342], enable=False)
        self.set_skill(triggerIds=[343], enable=False)
        self.set_skill(triggerIds=[344], enable=False)
        self.set_skill(triggerIds=[345], enable=False)
        self.set_skill(triggerIds=[346], enable=False)
        self.set_skill(triggerIds=[347], enable=False)
        self.set_skill(triggerIds=[348], enable=False)
        self.set_skill(triggerIds=[349], enable=False)
        self.set_skill(triggerIds=[350], enable=False)
        self.set_skill(triggerIds=[351], enable=False)
        self.set_skill(triggerIds=[352], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬07(self.ctx)


class 스킬07(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[341], enable=True)
        self.set_skill(triggerIds=[342], enable=True)
        self.set_skill(triggerIds=[343], enable=True)
        self.set_skill(triggerIds=[344], enable=True)
        self.set_skill(triggerIds=[345], enable=True)
        self.set_skill(triggerIds=[346], enable=True)
        self.set_skill(triggerIds=[347], enable=True)
        self.set_skill(triggerIds=[348], enable=True)
        self.set_skill(triggerIds=[349], enable=True)
        self.set_skill(triggerIds=[350], enable=True)
        self.set_skill(triggerIds=[351], enable=True)
        self.set_skill(triggerIds=[352], enable=True)
        self.set_skill(triggerIds=[353], enable=True)
        self.set_skill(triggerIds=[354], enable=True)
        self.set_skill(triggerIds=[355], enable=True)
        self.set_skill(triggerIds=[356], enable=True)
        self.set_skill(triggerIds=[357], enable=True)
        self.set_skill(triggerIds=[358], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[341], enable=False)
        self.set_skill(triggerIds=[342], enable=False)
        self.set_skill(triggerIds=[343], enable=False)
        self.set_skill(triggerIds=[344], enable=False)
        self.set_skill(triggerIds=[345], enable=False)
        self.set_skill(triggerIds=[346], enable=False)
        self.set_skill(triggerIds=[347], enable=False)
        self.set_skill(triggerIds=[348], enable=False)
        self.set_skill(triggerIds=[349], enable=False)
        self.set_skill(triggerIds=[350], enable=False)
        self.set_skill(triggerIds=[351], enable=False)
        self.set_skill(triggerIds=[352], enable=False)
        self.set_skill(triggerIds=[353], enable=False)
        self.set_skill(triggerIds=[354], enable=False)
        self.set_skill(triggerIds=[355], enable=False)
        self.set_skill(triggerIds=[356], enable=False)
        self.set_skill(triggerIds=[357], enable=False)
        self.set_skill(triggerIds=[358], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000409], stateValue=0):
            return 굳음(self.ctx)
        if self.true():
            return 스킬08(self.ctx)


class 굳음(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='20'):
            return 스킬08(self.ctx)


class 스킬08(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=False, arg3=0, delay=100)
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[347], enable=True)
        self.set_skill(triggerIds=[348], enable=True)
        self.set_skill(triggerIds=[349], enable=True)
        self.set_skill(triggerIds=[350], enable=True)
        self.set_skill(triggerIds=[351], enable=True)
        self.set_skill(triggerIds=[352], enable=True)
        self.set_skill(triggerIds=[353], enable=True)
        self.set_skill(triggerIds=[354], enable=True)
        self.set_skill(triggerIds=[355], enable=True)
        self.set_skill(triggerIds=[356], enable=True)
        self.set_skill(triggerIds=[357], enable=True)
        self.set_skill(triggerIds=[358], enable=True)
        self.set_skill(triggerIds=[359], enable=True)
        self.set_skill(triggerIds=[360], enable=True)
        self.set_skill(triggerIds=[361], enable=True)
        self.set_skill(triggerIds=[362], enable=True)
        self.set_skill(triggerIds=[363], enable=True)
        self.set_skill(triggerIds=[364], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[347], enable=False)
        self.set_skill(triggerIds=[348], enable=False)
        self.set_skill(triggerIds=[349], enable=False)
        self.set_skill(triggerIds=[350], enable=False)
        self.set_skill(triggerIds=[351], enable=False)
        self.set_skill(triggerIds=[352], enable=False)
        self.set_skill(triggerIds=[353], enable=False)
        self.set_skill(triggerIds=[354], enable=False)
        self.set_skill(triggerIds=[355], enable=False)
        self.set_skill(triggerIds=[356], enable=False)
        self.set_skill(triggerIds=[357], enable=False)
        self.set_skill(triggerIds=[358], enable=False)
        self.set_skill(triggerIds=[359], enable=False)
        self.set_skill(triggerIds=[360], enable=False)
        self.set_skill(triggerIds=[361], enable=False)
        self.set_skill(triggerIds=[362], enable=False)
        self.set_skill(triggerIds=[363], enable=False)
        self.set_skill(triggerIds=[364], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬09(self.ctx)


class 스킬09(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[353], enable=True)
        self.set_skill(triggerIds=[354], enable=True)
        self.set_skill(triggerIds=[355], enable=True)
        self.set_skill(triggerIds=[356], enable=True)
        self.set_skill(triggerIds=[357], enable=True)
        self.set_skill(triggerIds=[358], enable=True)
        self.set_skill(triggerIds=[359], enable=True)
        self.set_skill(triggerIds=[360], enable=True)
        self.set_skill(triggerIds=[361], enable=True)
        self.set_skill(triggerIds=[362], enable=True)
        self.set_skill(triggerIds=[363], enable=True)
        self.set_skill(triggerIds=[364], enable=True)
        self.set_skill(triggerIds=[365], enable=True)
        self.set_skill(triggerIds=[366], enable=True)
        self.set_skill(triggerIds=[367], enable=True)
        self.set_skill(triggerIds=[368], enable=True)
        self.set_skill(triggerIds=[369], enable=True)
        self.set_skill(triggerIds=[370], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[353], enable=False)
        self.set_skill(triggerIds=[354], enable=False)
        self.set_skill(triggerIds=[355], enable=False)
        self.set_skill(triggerIds=[356], enable=False)
        self.set_skill(triggerIds=[357], enable=False)
        self.set_skill(triggerIds=[358], enable=False)
        self.set_skill(triggerIds=[359], enable=False)
        self.set_skill(triggerIds=[360], enable=False)
        self.set_skill(triggerIds=[361], enable=False)
        self.set_skill(triggerIds=[362], enable=False)
        self.set_skill(triggerIds=[363], enable=False)
        self.set_skill(triggerIds=[364], enable=False)
        self.set_skill(triggerIds=[365], enable=False)
        self.set_skill(triggerIds=[366], enable=False)
        self.set_skill(triggerIds=[367], enable=False)
        self.set_skill(triggerIds=[368], enable=False)
        self.set_skill(triggerIds=[369], enable=False)
        self.set_skill(triggerIds=[370], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬10(self.ctx)


class 스킬10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[359], enable=True)
        self.set_skill(triggerIds=[360], enable=True)
        self.set_skill(triggerIds=[361], enable=True)
        self.set_skill(triggerIds=[362], enable=True)
        self.set_skill(triggerIds=[363], enable=True)
        self.set_skill(triggerIds=[364], enable=True)
        self.set_skill(triggerIds=[365], enable=True)
        self.set_skill(triggerIds=[366], enable=True)
        self.set_skill(triggerIds=[367], enable=True)
        self.set_skill(triggerIds=[368], enable=True)
        self.set_skill(triggerIds=[369], enable=True)
        self.set_skill(triggerIds=[370], enable=True)
        self.set_skill(triggerIds=[371], enable=True)
        self.set_skill(triggerIds=[372], enable=True)
        self.set_skill(triggerIds=[373], enable=True)
        self.set_skill(triggerIds=[374], enable=True)
        self.set_skill(triggerIds=[375], enable=True)
        self.set_skill(triggerIds=[376], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=0)
        self.set_skill(triggerIds=[359], enable=False)
        self.set_skill(triggerIds=[360], enable=False)
        self.set_skill(triggerIds=[361], enable=False)
        self.set_skill(triggerIds=[362], enable=False)
        self.set_skill(triggerIds=[363], enable=False)
        self.set_skill(triggerIds=[364], enable=False)
        self.set_skill(triggerIds=[365], enable=False)
        self.set_skill(triggerIds=[366], enable=False)
        self.set_skill(triggerIds=[367], enable=False)
        self.set_skill(triggerIds=[368], enable=False)
        self.set_skill(triggerIds=[369], enable=False)
        self.set_skill(triggerIds=[370], enable=False)
        self.set_skill(triggerIds=[371], enable=False)
        self.set_skill(triggerIds=[372], enable=False)
        self.set_skill(triggerIds=[373], enable=False)
        self.set_skill(triggerIds=[374], enable=False)
        self.set_skill(triggerIds=[375], enable=False)
        self.set_skill(triggerIds=[376], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬12(self.ctx)


class 스킬12(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[365], enable=True)
        self.set_skill(triggerIds=[366], enable=True)
        self.set_skill(triggerIds=[367], enable=True)
        self.set_skill(triggerIds=[368], enable=True)
        self.set_skill(triggerIds=[369], enable=True)
        self.set_skill(triggerIds=[370], enable=True)
        self.set_skill(triggerIds=[371], enable=True)
        self.set_skill(triggerIds=[372], enable=True)
        self.set_skill(triggerIds=[373], enable=True)
        self.set_skill(triggerIds=[374], enable=True)
        self.set_skill(triggerIds=[375], enable=True)
        self.set_skill(triggerIds=[376], enable=True)
        self.set_skill(triggerIds=[377], enable=True)
        self.set_skill(triggerIds=[378], enable=True)
        self.set_skill(triggerIds=[379], enable=True)
        self.set_skill(triggerIds=[380], enable=True)
        self.set_skill(triggerIds=[381], enable=True)
        self.set_skill(triggerIds=[382], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[365], enable=False)
        self.set_skill(triggerIds=[366], enable=False)
        self.set_skill(triggerIds=[367], enable=False)
        self.set_skill(triggerIds=[368], enable=False)
        self.set_skill(triggerIds=[369], enable=False)
        self.set_skill(triggerIds=[370], enable=False)
        self.set_skill(triggerIds=[371], enable=False)
        self.set_skill(triggerIds=[372], enable=False)
        self.set_skill(triggerIds=[373], enable=False)
        self.set_skill(triggerIds=[374], enable=False)
        self.set_skill(triggerIds=[375], enable=False)
        self.set_skill(triggerIds=[376], enable=False)
        self.set_skill(triggerIds=[377], enable=False)
        self.set_skill(triggerIds=[378], enable=False)
        self.set_skill(triggerIds=[379], enable=False)
        self.set_skill(triggerIds=[380], enable=False)
        self.set_skill(triggerIds=[381], enable=False)
        self.set_skill(triggerIds=[382], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬13(self.ctx)


class 스킬13(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[371], enable=True)
        self.set_skill(triggerIds=[372], enable=True)
        self.set_skill(triggerIds=[373], enable=True)
        self.set_skill(triggerIds=[374], enable=True)
        self.set_skill(triggerIds=[375], enable=True)
        self.set_skill(triggerIds=[376], enable=True)
        self.set_skill(triggerIds=[377], enable=True)
        self.set_skill(triggerIds=[378], enable=True)
        self.set_skill(triggerIds=[379], enable=True)
        self.set_skill(triggerIds=[380], enable=True)
        self.set_skill(triggerIds=[381], enable=True)
        self.set_skill(triggerIds=[382], enable=True)
        self.set_skill(triggerIds=[383], enable=True)
        self.set_skill(triggerIds=[384], enable=True)
        self.set_skill(triggerIds=[385], enable=True)
        self.set_skill(triggerIds=[386], enable=True)
        self.set_skill(triggerIds=[387], enable=True)
        self.set_skill(triggerIds=[388], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[371], enable=False)
        self.set_skill(triggerIds=[372], enable=False)
        self.set_skill(triggerIds=[373], enable=False)
        self.set_skill(triggerIds=[374], enable=False)
        self.set_skill(triggerIds=[375], enable=False)
        self.set_skill(triggerIds=[376], enable=False)
        self.set_skill(triggerIds=[377], enable=False)
        self.set_skill(triggerIds=[378], enable=False)
        self.set_skill(triggerIds=[379], enable=False)
        self.set_skill(triggerIds=[380], enable=False)
        self.set_skill(triggerIds=[381], enable=False)
        self.set_skill(triggerIds=[382], enable=False)
        self.set_skill(triggerIds=[383], enable=False)
        self.set_skill(triggerIds=[384], enable=False)
        self.set_skill(triggerIds=[385], enable=False)
        self.set_skill(triggerIds=[386], enable=False)
        self.set_skill(triggerIds=[387], enable=False)
        self.set_skill(triggerIds=[388], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬14(self.ctx)


class 스킬14(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[377], enable=True)
        self.set_skill(triggerIds=[378], enable=True)
        self.set_skill(triggerIds=[379], enable=True)
        self.set_skill(triggerIds=[380], enable=True)
        self.set_skill(triggerIds=[381], enable=True)
        self.set_skill(triggerIds=[382], enable=True)
        self.set_skill(triggerIds=[383], enable=True)
        self.set_skill(triggerIds=[384], enable=True)
        self.set_skill(triggerIds=[385], enable=True)
        self.set_skill(triggerIds=[386], enable=True)
        self.set_skill(triggerIds=[387], enable=True)
        self.set_skill(triggerIds=[388], enable=True)
        self.set_skill(triggerIds=[389], enable=True)
        self.set_skill(triggerIds=[390], enable=True)
        self.set_skill(triggerIds=[391], enable=True)
        self.set_skill(triggerIds=[392], enable=True)
        self.set_skill(triggerIds=[393], enable=True)
        self.set_skill(triggerIds=[394], enable=True)
        self.set_skill(triggerIds=[395], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[377], enable=False)
        self.set_skill(triggerIds=[378], enable=False)
        self.set_skill(triggerIds=[379], enable=False)
        self.set_skill(triggerIds=[380], enable=False)
        self.set_skill(triggerIds=[381], enable=False)
        self.set_skill(triggerIds=[382], enable=False)
        self.set_skill(triggerIds=[383], enable=False)
        self.set_skill(triggerIds=[384], enable=False)
        self.set_skill(triggerIds=[385], enable=False)
        self.set_skill(triggerIds=[386], enable=False)
        self.set_skill(triggerIds=[387], enable=False)
        self.set_skill(triggerIds=[388], enable=False)
        self.set_skill(triggerIds=[389], enable=False)
        self.set_skill(triggerIds=[390], enable=False)
        self.set_skill(triggerIds=[391], enable=False)
        self.set_skill(triggerIds=[392], enable=False)
        self.set_skill(triggerIds=[393], enable=False)
        self.set_skill(triggerIds=[394], enable=False)
        self.set_skill(triggerIds=[395], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬15(self.ctx)


class 스킬15(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[383], enable=True)
        self.set_skill(triggerIds=[384], enable=True)
        self.set_skill(triggerIds=[385], enable=True)
        self.set_skill(triggerIds=[386], enable=True)
        self.set_skill(triggerIds=[387], enable=True)
        self.set_skill(triggerIds=[388], enable=True)
        self.set_skill(triggerIds=[389], enable=True)
        self.set_skill(triggerIds=[390], enable=True)
        self.set_skill(triggerIds=[391], enable=True)
        self.set_skill(triggerIds=[392], enable=True)
        self.set_skill(triggerIds=[393], enable=True)
        self.set_skill(triggerIds=[394], enable=True)
        self.set_skill(triggerIds=[395], enable=True)
        self.set_skill(triggerIds=[396], enable=True)
        self.set_skill(triggerIds=[397], enable=True)
        self.set_skill(triggerIds=[398], enable=True)
        self.set_skill(triggerIds=[399], enable=True)
        self.set_skill(triggerIds=[400], enable=True)
        self.set_skill(triggerIds=[401], enable=True)
        self.set_skill(triggerIds=[402], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[383], enable=False)
        self.set_skill(triggerIds=[384], enable=False)
        self.set_skill(triggerIds=[385], enable=False)
        self.set_skill(triggerIds=[386], enable=False)
        self.set_skill(triggerIds=[387], enable=False)
        self.set_skill(triggerIds=[388], enable=False)
        self.set_skill(triggerIds=[389], enable=False)
        self.set_skill(triggerIds=[390], enable=False)
        self.set_skill(triggerIds=[391], enable=False)
        self.set_skill(triggerIds=[392], enable=False)
        self.set_skill(triggerIds=[393], enable=False)
        self.set_skill(triggerIds=[394], enable=False)
        self.set_skill(triggerIds=[395], enable=False)
        self.set_skill(triggerIds=[396], enable=False)
        self.set_skill(triggerIds=[397], enable=False)
        self.set_skill(triggerIds=[398], enable=False)
        self.set_skill(triggerIds=[399], enable=False)
        self.set_skill(triggerIds=[400], enable=False)
        self.set_skill(triggerIds=[401], enable=False)
        self.set_skill(triggerIds=[402], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬16(self.ctx)


class 스킬16(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[389], enable=True)
        self.set_skill(triggerIds=[390], enable=True)
        self.set_skill(triggerIds=[391], enable=True)
        self.set_skill(triggerIds=[392], enable=True)
        self.set_skill(triggerIds=[393], enable=True)
        self.set_skill(triggerIds=[394], enable=True)
        self.set_skill(triggerIds=[395], enable=True)
        self.set_skill(triggerIds=[396], enable=True)
        self.set_skill(triggerIds=[397], enable=True)
        self.set_skill(triggerIds=[398], enable=True)
        self.set_skill(triggerIds=[399], enable=True)
        self.set_skill(triggerIds=[400], enable=True)
        self.set_skill(triggerIds=[401], enable=True)
        self.set_skill(triggerIds=[402], enable=True)
        self.set_skill(triggerIds=[403], enable=True)
        self.set_skill(triggerIds=[404], enable=True)
        self.set_skill(triggerIds=[405], enable=True)
        self.set_skill(triggerIds=[406], enable=True)
        self.set_skill(triggerIds=[407], enable=True)
        self.set_skill(triggerIds=[408], enable=True)
        self.set_skill(triggerIds=[409], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[389], enable=False)
        self.set_skill(triggerIds=[390], enable=False)
        self.set_skill(triggerIds=[391], enable=False)
        self.set_skill(triggerIds=[392], enable=False)
        self.set_skill(triggerIds=[393], enable=False)
        self.set_skill(triggerIds=[394], enable=False)
        self.set_skill(triggerIds=[395], enable=False)
        self.set_skill(triggerIds=[396], enable=False)
        self.set_skill(triggerIds=[397], enable=False)
        self.set_skill(triggerIds=[398], enable=False)
        self.set_skill(triggerIds=[399], enable=False)
        self.set_skill(triggerIds=[400], enable=False)
        self.set_skill(triggerIds=[401], enable=False)
        self.set_skill(triggerIds=[402], enable=False)
        self.set_skill(triggerIds=[403], enable=False)
        self.set_skill(triggerIds=[404], enable=False)
        self.set_skill(triggerIds=[405], enable=False)
        self.set_skill(triggerIds=[406], enable=False)
        self.set_skill(triggerIds=[407], enable=False)
        self.set_skill(triggerIds=[408], enable=False)
        self.set_skill(triggerIds=[409], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬17(self.ctx)


class 스킬17(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[396], enable=True)
        self.set_skill(triggerIds=[397], enable=True)
        self.set_skill(triggerIds=[398], enable=True)
        self.set_skill(triggerIds=[399], enable=True)
        self.set_skill(triggerIds=[400], enable=True)
        self.set_skill(triggerIds=[401], enable=True)
        self.set_skill(triggerIds=[402], enable=True)
        self.set_skill(triggerIds=[403], enable=True)
        self.set_skill(triggerIds=[404], enable=True)
        self.set_skill(triggerIds=[405], enable=True)
        self.set_skill(triggerIds=[406], enable=True)
        self.set_skill(triggerIds=[407], enable=True)
        self.set_skill(triggerIds=[408], enable=True)
        self.set_skill(triggerIds=[409], enable=True)
        self.set_skill(triggerIds=[410], enable=True)
        self.set_skill(triggerIds=[411], enable=True)
        self.set_skill(triggerIds=[412], enable=True)
        self.set_skill(triggerIds=[413], enable=True)
        self.set_skill(triggerIds=[414], enable=True)
        self.set_skill(triggerIds=[415], enable=True)
        self.set_skill(triggerIds=[416], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[396], enable=False)
        self.set_skill(triggerIds=[397], enable=False)
        self.set_skill(triggerIds=[398], enable=False)
        self.set_skill(triggerIds=[399], enable=False)
        self.set_skill(triggerIds=[400], enable=False)
        self.set_skill(triggerIds=[401], enable=False)
        self.set_skill(triggerIds=[402], enable=False)
        self.set_skill(triggerIds=[403], enable=False)
        self.set_skill(triggerIds=[404], enable=False)
        self.set_skill(triggerIds=[405], enable=False)
        self.set_skill(triggerIds=[406], enable=False)
        self.set_skill(triggerIds=[407], enable=False)
        self.set_skill(triggerIds=[408], enable=False)
        self.set_skill(triggerIds=[409], enable=False)
        self.set_skill(triggerIds=[410], enable=False)
        self.set_skill(triggerIds=[411], enable=False)
        self.set_skill(triggerIds=[412], enable=False)
        self.set_skill(triggerIds=[413], enable=False)
        self.set_skill(triggerIds=[414], enable=False)
        self.set_skill(triggerIds=[415], enable=False)
        self.set_skill(triggerIds=[416], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬18(self.ctx)


class 스킬18(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[403], enable=True)
        self.set_skill(triggerIds=[404], enable=True)
        self.set_skill(triggerIds=[405], enable=True)
        self.set_skill(triggerIds=[406], enable=True)
        self.set_skill(triggerIds=[407], enable=True)
        self.set_skill(triggerIds=[408], enable=True)
        self.set_skill(triggerIds=[409], enable=True)
        self.set_skill(triggerIds=[410], enable=True)
        self.set_skill(triggerIds=[411], enable=True)
        self.set_skill(triggerIds=[412], enable=True)
        self.set_skill(triggerIds=[413], enable=True)
        self.set_skill(triggerIds=[414], enable=True)
        self.set_skill(triggerIds=[415], enable=True)
        self.set_skill(triggerIds=[416], enable=True)
        self.set_skill(triggerIds=[417], enable=True)
        self.set_skill(triggerIds=[418], enable=True)
        self.set_skill(triggerIds=[419], enable=True)
        self.set_skill(triggerIds=[420], enable=True)
        self.set_skill(triggerIds=[421], enable=True)
        self.set_skill(triggerIds=[422], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[403], enable=False)
        self.set_skill(triggerIds=[404], enable=False)
        self.set_skill(triggerIds=[405], enable=False)
        self.set_skill(triggerIds=[406], enable=False)
        self.set_skill(triggerIds=[407], enable=False)
        self.set_skill(triggerIds=[408], enable=False)
        self.set_skill(triggerIds=[409], enable=False)
        self.set_skill(triggerIds=[410], enable=False)
        self.set_skill(triggerIds=[411], enable=False)
        self.set_skill(triggerIds=[412], enable=False)
        self.set_skill(triggerIds=[413], enable=False)
        self.set_skill(triggerIds=[414], enable=False)
        self.set_skill(triggerIds=[415], enable=False)
        self.set_skill(triggerIds=[416], enable=False)
        self.set_skill(triggerIds=[417], enable=False)
        self.set_skill(triggerIds=[418], enable=False)
        self.set_skill(triggerIds=[419], enable=False)
        self.set_skill(triggerIds=[420], enable=False)
        self.set_skill(triggerIds=[421], enable=False)
        self.set_skill(triggerIds=[422], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬19(self.ctx)


class 스킬19(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[410], enable=True)
        self.set_skill(triggerIds=[411], enable=True)
        self.set_skill(triggerIds=[412], enable=True)
        self.set_skill(triggerIds=[413], enable=True)
        self.set_skill(triggerIds=[414], enable=True)
        self.set_skill(triggerIds=[415], enable=True)
        self.set_skill(triggerIds=[416], enable=True)
        self.set_skill(triggerIds=[417], enable=True)
        self.set_skill(triggerIds=[418], enable=True)
        self.set_skill(triggerIds=[419], enable=True)
        self.set_skill(triggerIds=[420], enable=True)
        self.set_skill(triggerIds=[421], enable=True)
        self.set_skill(triggerIds=[422], enable=True)
        self.set_skill(triggerIds=[423], enable=True)
        self.set_skill(triggerIds=[424], enable=True)
        self.set_skill(triggerIds=[425], enable=True)
        self.set_skill(triggerIds=[426], enable=True)
        self.set_skill(triggerIds=[427], enable=True)
        self.set_skill(triggerIds=[428], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[410], enable=False)
        self.set_skill(triggerIds=[411], enable=False)
        self.set_skill(triggerIds=[412], enable=False)
        self.set_skill(triggerIds=[413], enable=False)
        self.set_skill(triggerIds=[414], enable=False)
        self.set_skill(triggerIds=[415], enable=False)
        self.set_skill(triggerIds=[416], enable=False)
        self.set_skill(triggerIds=[417], enable=False)
        self.set_skill(triggerIds=[418], enable=False)
        self.set_skill(triggerIds=[419], enable=False)
        self.set_skill(triggerIds=[420], enable=False)
        self.set_skill(triggerIds=[421], enable=False)
        self.set_skill(triggerIds=[422], enable=False)
        self.set_skill(triggerIds=[423], enable=False)
        self.set_skill(triggerIds=[424], enable=False)
        self.set_skill(triggerIds=[425], enable=False)
        self.set_skill(triggerIds=[426], enable=False)
        self.set_skill(triggerIds=[427], enable=False)
        self.set_skill(triggerIds=[428], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬20(self.ctx)


class 스킬20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[417], enable=True)
        self.set_skill(triggerIds=[418], enable=True)
        self.set_skill(triggerIds=[419], enable=True)
        self.set_skill(triggerIds=[420], enable=True)
        self.set_skill(triggerIds=[421], enable=True)
        self.set_skill(triggerIds=[422], enable=True)
        self.set_skill(triggerIds=[423], enable=True)
        self.set_skill(triggerIds=[424], enable=True)
        self.set_skill(triggerIds=[425], enable=True)
        self.set_skill(triggerIds=[426], enable=True)
        self.set_skill(triggerIds=[427], enable=True)
        self.set_skill(triggerIds=[428], enable=True)
        self.set_skill(triggerIds=[429], enable=True)
        self.set_skill(triggerIds=[430], enable=True)
        self.set_skill(triggerIds=[431], enable=True)
        self.set_skill(triggerIds=[432], enable=True)
        self.set_skill(triggerIds=[433], enable=True)
        self.set_skill(triggerIds=[434], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[417], enable=False)
        self.set_skill(triggerIds=[418], enable=False)
        self.set_skill(triggerIds=[419], enable=False)
        self.set_skill(triggerIds=[420], enable=False)
        self.set_skill(triggerIds=[421], enable=False)
        self.set_skill(triggerIds=[422], enable=False)
        self.set_skill(triggerIds=[423], enable=False)
        self.set_skill(triggerIds=[424], enable=False)
        self.set_skill(triggerIds=[425], enable=False)
        self.set_skill(triggerIds=[426], enable=False)
        self.set_skill(triggerIds=[427], enable=False)
        self.set_skill(triggerIds=[428], enable=False)
        self.set_skill(triggerIds=[429], enable=False)
        self.set_skill(triggerIds=[430], enable=False)
        self.set_skill(triggerIds=[431], enable=False)
        self.set_skill(triggerIds=[432], enable=False)
        self.set_skill(triggerIds=[433], enable=False)
        self.set_skill(triggerIds=[434], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬21(self.ctx)


class 스킬21(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[423], enable=True)
        self.set_skill(triggerIds=[424], enable=True)
        self.set_skill(triggerIds=[425], enable=True)
        self.set_skill(triggerIds=[426], enable=True)
        self.set_skill(triggerIds=[427], enable=True)
        self.set_skill(triggerIds=[428], enable=True)
        self.set_skill(triggerIds=[429], enable=True)
        self.set_skill(triggerIds=[430], enable=True)
        self.set_skill(triggerIds=[431], enable=True)
        self.set_skill(triggerIds=[432], enable=True)
        self.set_skill(triggerIds=[433], enable=True)
        self.set_skill(triggerIds=[434], enable=True)
        self.set_skill(triggerIds=[435], enable=True)
        self.set_skill(triggerIds=[436], enable=True)
        self.set_skill(triggerIds=[437], enable=True)
        self.set_skill(triggerIds=[438], enable=True)
        self.set_skill(triggerIds=[439], enable=True)
        self.set_skill(triggerIds=[440], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[423], enable=False)
        self.set_skill(triggerIds=[424], enable=False)
        self.set_skill(triggerIds=[425], enable=False)
        self.set_skill(triggerIds=[426], enable=False)
        self.set_skill(triggerIds=[427], enable=False)
        self.set_skill(triggerIds=[428], enable=False)
        self.set_skill(triggerIds=[429], enable=False)
        self.set_skill(triggerIds=[430], enable=False)
        self.set_skill(triggerIds=[431], enable=False)
        self.set_skill(triggerIds=[432], enable=False)
        self.set_skill(triggerIds=[433], enable=False)
        self.set_skill(triggerIds=[434], enable=False)
        self.set_skill(triggerIds=[435], enable=False)
        self.set_skill(triggerIds=[436], enable=False)
        self.set_skill(triggerIds=[437], enable=False)
        self.set_skill(triggerIds=[438], enable=False)
        self.set_skill(triggerIds=[439], enable=False)
        self.set_skill(triggerIds=[440], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬22(self.ctx)


class 스킬22(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[429], enable=True)
        self.set_skill(triggerIds=[430], enable=True)
        self.set_skill(triggerIds=[431], enable=True)
        self.set_skill(triggerIds=[432], enable=True)
        self.set_skill(triggerIds=[433], enable=True)
        self.set_skill(triggerIds=[434], enable=True)
        self.set_skill(triggerIds=[435], enable=True)
        self.set_skill(triggerIds=[436], enable=True)
        self.set_skill(triggerIds=[437], enable=True)
        self.set_skill(triggerIds=[438], enable=True)
        self.set_skill(triggerIds=[439], enable=True)
        self.set_skill(triggerIds=[440], enable=True)
        self.set_skill(triggerIds=[441], enable=True)
        self.set_skill(triggerIds=[442], enable=True)
        self.set_skill(triggerIds=[443], enable=True)
        self.set_skill(triggerIds=[444], enable=True)
        self.set_skill(triggerIds=[445], enable=True)
        self.set_skill(triggerIds=[446], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[429], enable=False)
        self.set_skill(triggerIds=[430], enable=False)
        self.set_skill(triggerIds=[431], enable=False)
        self.set_skill(triggerIds=[432], enable=False)
        self.set_skill(triggerIds=[433], enable=False)
        self.set_skill(triggerIds=[434], enable=False)
        self.set_skill(triggerIds=[435], enable=False)
        self.set_skill(triggerIds=[436], enable=False)
        self.set_skill(triggerIds=[437], enable=False)
        self.set_skill(triggerIds=[438], enable=False)
        self.set_skill(triggerIds=[439], enable=False)
        self.set_skill(triggerIds=[440], enable=False)
        self.set_skill(triggerIds=[441], enable=False)
        self.set_skill(triggerIds=[442], enable=False)
        self.set_skill(triggerIds=[443], enable=False)
        self.set_skill(triggerIds=[444], enable=False)
        self.set_skill(triggerIds=[445], enable=False)
        self.set_skill(triggerIds=[446], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬23(self.ctx)


class 스킬23(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[435], enable=True)
        self.set_skill(triggerIds=[436], enable=True)
        self.set_skill(triggerIds=[437], enable=True)
        self.set_skill(triggerIds=[438], enable=True)
        self.set_skill(triggerIds=[439], enable=True)
        self.set_skill(triggerIds=[440], enable=True)
        self.set_skill(triggerIds=[441], enable=True)
        self.set_skill(triggerIds=[442], enable=True)
        self.set_skill(triggerIds=[443], enable=True)
        self.set_skill(triggerIds=[444], enable=True)
        self.set_skill(triggerIds=[445], enable=True)
        self.set_skill(triggerIds=[446], enable=True)
        self.set_skill(triggerIds=[447], enable=True)
        self.set_skill(triggerIds=[448], enable=True)
        self.set_skill(triggerIds=[449], enable=True)
        self.set_skill(triggerIds=[450], enable=True)
        self.set_skill(triggerIds=[451], enable=True)
        self.set_skill(triggerIds=[452], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[435], enable=False)
        self.set_skill(triggerIds=[436], enable=False)
        self.set_skill(triggerIds=[437], enable=False)
        self.set_skill(triggerIds=[438], enable=False)
        self.set_skill(triggerIds=[439], enable=False)
        self.set_skill(triggerIds=[440], enable=False)
        self.set_skill(triggerIds=[441], enable=False)
        self.set_skill(triggerIds=[442], enable=False)
        self.set_skill(triggerIds=[443], enable=False)
        self.set_skill(triggerIds=[444], enable=False)
        self.set_skill(triggerIds=[445], enable=False)
        self.set_skill(triggerIds=[446], enable=False)
        self.set_skill(triggerIds=[447], enable=False)
        self.set_skill(triggerIds=[448], enable=False)
        self.set_skill(triggerIds=[449], enable=False)
        self.set_skill(triggerIds=[450], enable=False)
        self.set_skill(triggerIds=[451], enable=False)
        self.set_skill(triggerIds=[452], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬24(self.ctx)


class 스킬24(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[441], enable=True)
        self.set_skill(triggerIds=[442], enable=True)
        self.set_skill(triggerIds=[443], enable=True)
        self.set_skill(triggerIds=[444], enable=True)
        self.set_skill(triggerIds=[445], enable=True)
        self.set_skill(triggerIds=[446], enable=True)
        self.set_skill(triggerIds=[447], enable=True)
        self.set_skill(triggerIds=[448], enable=True)
        self.set_skill(triggerIds=[449], enable=True)
        self.set_skill(triggerIds=[450], enable=True)
        self.set_skill(triggerIds=[451], enable=True)
        self.set_skill(triggerIds=[452], enable=True)
        self.set_skill(triggerIds=[453], enable=True)
        self.set_skill(triggerIds=[454], enable=True)
        self.set_skill(triggerIds=[455], enable=True)
        self.set_skill(triggerIds=[456], enable=True)
        self.set_skill(triggerIds=[457], enable=True)
        self.set_skill(triggerIds=[458], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[441], enable=False)
        self.set_skill(triggerIds=[442], enable=False)
        self.set_skill(triggerIds=[443], enable=False)
        self.set_skill(triggerIds=[444], enable=False)
        self.set_skill(triggerIds=[445], enable=False)
        self.set_skill(triggerIds=[446], enable=False)
        self.set_skill(triggerIds=[447], enable=False)
        self.set_skill(triggerIds=[448], enable=False)
        self.set_skill(triggerIds=[449], enable=False)
        self.set_skill(triggerIds=[450], enable=False)
        self.set_skill(triggerIds=[451], enable=False)
        self.set_skill(triggerIds=[452], enable=False)
        self.set_skill(triggerIds=[453], enable=False)
        self.set_skill(triggerIds=[454], enable=False)
        self.set_skill(triggerIds=[455], enable=False)
        self.set_skill(triggerIds=[456], enable=False)
        self.set_skill(triggerIds=[457], enable=False)
        self.set_skill(triggerIds=[458], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬25(self.ctx)


class 스킬25(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[447], enable=True)
        self.set_skill(triggerIds=[448], enable=True)
        self.set_skill(triggerIds=[449], enable=True)
        self.set_skill(triggerIds=[450], enable=True)
        self.set_skill(triggerIds=[451], enable=True)
        self.set_skill(triggerIds=[452], enable=True)
        self.set_skill(triggerIds=[453], enable=True)
        self.set_skill(triggerIds=[454], enable=True)
        self.set_skill(triggerIds=[455], enable=True)
        self.set_skill(triggerIds=[456], enable=True)
        self.set_skill(triggerIds=[457], enable=True)
        self.set_skill(triggerIds=[458], enable=True)
        self.set_skill(triggerIds=[459], enable=True)
        self.set_skill(triggerIds=[460], enable=True)
        self.set_skill(triggerIds=[461], enable=True)
        self.set_skill(triggerIds=[462], enable=True)
        self.set_skill(triggerIds=[463], enable=True)
        self.set_skill(triggerIds=[464], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[447], enable=False)
        self.set_skill(triggerIds=[448], enable=False)
        self.set_skill(triggerIds=[449], enable=False)
        self.set_skill(triggerIds=[450], enable=False)
        self.set_skill(triggerIds=[451], enable=False)
        self.set_skill(triggerIds=[452], enable=False)
        self.set_skill(triggerIds=[453], enable=False)
        self.set_skill(triggerIds=[454], enable=False)
        self.set_skill(triggerIds=[455], enable=False)
        self.set_skill(triggerIds=[456], enable=False)
        self.set_skill(triggerIds=[457], enable=False)
        self.set_skill(triggerIds=[458], enable=False)
        self.set_skill(triggerIds=[459], enable=False)
        self.set_skill(triggerIds=[460], enable=False)
        self.set_skill(triggerIds=[461], enable=False)
        self.set_skill(triggerIds=[462], enable=False)
        self.set_skill(triggerIds=[463], enable=False)
        self.set_skill(triggerIds=[464], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬26(self.ctx)


class 스킬26(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[453], enable=True)
        self.set_skill(triggerIds=[454], enable=True)
        self.set_skill(triggerIds=[455], enable=True)
        self.set_skill(triggerIds=[456], enable=True)
        self.set_skill(triggerIds=[457], enable=True)
        self.set_skill(triggerIds=[458], enable=True)
        self.set_skill(triggerIds=[459], enable=True)
        self.set_skill(triggerIds=[460], enable=True)
        self.set_skill(triggerIds=[461], enable=True)
        self.set_skill(triggerIds=[462], enable=True)
        self.set_skill(triggerIds=[463], enable=True)
        self.set_skill(triggerIds=[464], enable=True)
        self.set_skill(triggerIds=[465], enable=True)
        self.set_skill(triggerIds=[466], enable=True)
        self.set_skill(triggerIds=[467], enable=True)
        self.set_skill(triggerIds=[468], enable=True)
        self.set_skill(triggerIds=[469], enable=True)
        self.set_skill(triggerIds=[470], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[453], enable=False)
        self.set_skill(triggerIds=[454], enable=False)
        self.set_skill(triggerIds=[455], enable=False)
        self.set_skill(triggerIds=[456], enable=False)
        self.set_skill(triggerIds=[457], enable=False)
        self.set_skill(triggerIds=[458], enable=False)
        self.set_skill(triggerIds=[459], enable=False)
        self.set_skill(triggerIds=[460], enable=False)
        self.set_skill(triggerIds=[461], enable=False)
        self.set_skill(triggerIds=[462], enable=False)
        self.set_skill(triggerIds=[463], enable=False)
        self.set_skill(triggerIds=[464], enable=False)
        self.set_skill(triggerIds=[465], enable=False)
        self.set_skill(triggerIds=[466], enable=False)
        self.set_skill(triggerIds=[467], enable=False)
        self.set_skill(triggerIds=[468], enable=False)
        self.set_skill(triggerIds=[469], enable=False)
        self.set_skill(triggerIds=[470], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬27(self.ctx)


class 스킬27(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[459], enable=True)
        self.set_skill(triggerIds=[460], enable=True)
        self.set_skill(triggerIds=[461], enable=True)
        self.set_skill(triggerIds=[462], enable=True)
        self.set_skill(triggerIds=[463], enable=True)
        self.set_skill(triggerIds=[464], enable=True)
        self.set_skill(triggerIds=[465], enable=True)
        self.set_skill(triggerIds=[466], enable=True)
        self.set_skill(triggerIds=[467], enable=True)
        self.set_skill(triggerIds=[468], enable=True)
        self.set_skill(triggerIds=[469], enable=True)
        self.set_skill(triggerIds=[470], enable=True)
        self.set_skill(triggerIds=[471], enable=True)
        self.set_skill(triggerIds=[472], enable=True)
        self.set_skill(triggerIds=[473], enable=True)
        self.set_skill(triggerIds=[474], enable=True)
        self.set_skill(triggerIds=[475], enable=True)
        self.set_skill(triggerIds=[476], enable=True)
        self.set_skill(triggerIds=[477], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[459], enable=False)
        self.set_skill(triggerIds=[460], enable=False)
        self.set_skill(triggerIds=[461], enable=False)
        self.set_skill(triggerIds=[462], enable=False)
        self.set_skill(triggerIds=[463], enable=False)
        self.set_skill(triggerIds=[464], enable=False)
        self.set_skill(triggerIds=[465], enable=False)
        self.set_skill(triggerIds=[466], enable=False)
        self.set_skill(triggerIds=[467], enable=False)
        self.set_skill(triggerIds=[468], enable=False)
        self.set_skill(triggerIds=[469], enable=False)
        self.set_skill(triggerIds=[470], enable=False)
        self.set_skill(triggerIds=[471], enable=False)
        self.set_skill(triggerIds=[472], enable=False)
        self.set_skill(triggerIds=[473], enable=False)
        self.set_skill(triggerIds=[474], enable=False)
        self.set_skill(triggerIds=[475], enable=False)
        self.set_skill(triggerIds=[476], enable=False)
        self.set_skill(triggerIds=[477], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬28(self.ctx)


class 스킬28(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[465], enable=True)
        self.set_skill(triggerIds=[466], enable=True)
        self.set_skill(triggerIds=[467], enable=True)
        self.set_skill(triggerIds=[468], enable=True)
        self.set_skill(triggerIds=[469], enable=True)
        self.set_skill(triggerIds=[470], enable=True)
        self.set_skill(triggerIds=[471], enable=True)
        self.set_skill(triggerIds=[472], enable=True)
        self.set_skill(triggerIds=[473], enable=True)
        self.set_skill(triggerIds=[474], enable=True)
        self.set_skill(triggerIds=[475], enable=True)
        self.set_skill(triggerIds=[476], enable=True)
        self.set_skill(triggerIds=[477], enable=True)
        self.set_skill(triggerIds=[478], enable=True)
        self.set_skill(triggerIds=[479], enable=True)
        self.set_skill(triggerIds=[480], enable=True)
        self.set_skill(triggerIds=[481], enable=True)
        self.set_skill(triggerIds=[482], enable=True)
        self.set_skill(triggerIds=[483], enable=True)
        self.set_skill(triggerIds=[484], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[465], enable=False)
        self.set_skill(triggerIds=[466], enable=False)
        self.set_skill(triggerIds=[467], enable=False)
        self.set_skill(triggerIds=[468], enable=False)
        self.set_skill(triggerIds=[469], enable=False)
        self.set_skill(triggerIds=[470], enable=False)
        self.set_skill(triggerIds=[471], enable=False)
        self.set_skill(triggerIds=[472], enable=False)
        self.set_skill(triggerIds=[473], enable=False)
        self.set_skill(triggerIds=[474], enable=False)
        self.set_skill(triggerIds=[475], enable=False)
        self.set_skill(triggerIds=[476], enable=False)
        self.set_skill(triggerIds=[477], enable=False)
        self.set_skill(triggerIds=[478], enable=False)
        self.set_skill(triggerIds=[479], enable=False)
        self.set_skill(triggerIds=[480], enable=False)
        self.set_skill(triggerIds=[481], enable=False)
        self.set_skill(triggerIds=[482], enable=False)
        self.set_skill(triggerIds=[483], enable=False)
        self.set_skill(triggerIds=[484], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬29(self.ctx)


class 스킬29(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[471], enable=True)
        self.set_skill(triggerIds=[472], enable=True)
        self.set_skill(triggerIds=[473], enable=True)
        self.set_skill(triggerIds=[474], enable=True)
        self.set_skill(triggerIds=[475], enable=True)
        self.set_skill(triggerIds=[476], enable=True)
        self.set_skill(triggerIds=[477], enable=True)
        self.set_skill(triggerIds=[478], enable=True)
        self.set_skill(triggerIds=[479], enable=True)
        self.set_skill(triggerIds=[480], enable=True)
        self.set_skill(triggerIds=[481], enable=True)
        self.set_skill(triggerIds=[482], enable=True)
        self.set_skill(triggerIds=[483], enable=True)
        self.set_skill(triggerIds=[484], enable=True)
        self.set_skill(triggerIds=[485], enable=True)
        self.set_skill(triggerIds=[486], enable=True)
        self.set_skill(triggerIds=[487], enable=True)
        self.set_skill(triggerIds=[488], enable=True)
        self.set_skill(triggerIds=[489], enable=True)
        self.set_skill(triggerIds=[490], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[471], enable=False)
        self.set_skill(triggerIds=[472], enable=False)
        self.set_skill(triggerIds=[473], enable=False)
        self.set_skill(triggerIds=[474], enable=False)
        self.set_skill(triggerIds=[475], enable=False)
        self.set_skill(triggerIds=[476], enable=False)
        self.set_skill(triggerIds=[477], enable=False)
        self.set_skill(triggerIds=[478], enable=False)
        self.set_skill(triggerIds=[479], enable=False)
        self.set_skill(triggerIds=[480], enable=False)
        self.set_skill(triggerIds=[481], enable=False)
        self.set_skill(triggerIds=[482], enable=False)
        self.set_skill(triggerIds=[483], enable=False)
        self.set_skill(triggerIds=[484], enable=False)
        self.set_skill(triggerIds=[485], enable=False)
        self.set_skill(triggerIds=[486], enable=False)
        self.set_skill(triggerIds=[487], enable=False)
        self.set_skill(triggerIds=[488], enable=False)
        self.set_skill(triggerIds=[489], enable=False)
        self.set_skill(triggerIds=[490], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬30(self.ctx)


class 스킬30(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[478], enable=True)
        self.set_skill(triggerIds=[479], enable=True)
        self.set_skill(triggerIds=[480], enable=True)
        self.set_skill(triggerIds=[481], enable=True)
        self.set_skill(triggerIds=[482], enable=True)
        self.set_skill(triggerIds=[483], enable=True)
        self.set_skill(triggerIds=[484], enable=True)
        self.set_skill(triggerIds=[485], enable=True)
        self.set_skill(triggerIds=[486], enable=True)
        self.set_skill(triggerIds=[487], enable=True)
        self.set_skill(triggerIds=[488], enable=True)
        self.set_skill(triggerIds=[489], enable=True)
        self.set_skill(triggerIds=[490], enable=True)
        self.set_skill(triggerIds=[491], enable=True)
        self.set_skill(triggerIds=[492], enable=True)
        self.set_skill(triggerIds=[493], enable=True)
        self.set_skill(triggerIds=[494], enable=True)
        self.set_skill(triggerIds=[495], enable=True)
        self.set_skill(triggerIds=[496], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[478], enable=False)
        self.set_skill(triggerIds=[479], enable=False)
        self.set_skill(triggerIds=[480], enable=False)
        self.set_skill(triggerIds=[481], enable=False)
        self.set_skill(triggerIds=[482], enable=False)
        self.set_skill(triggerIds=[483], enable=False)
        self.set_skill(triggerIds=[484], enable=False)
        self.set_skill(triggerIds=[485], enable=False)
        self.set_skill(triggerIds=[486], enable=False)
        self.set_skill(triggerIds=[487], enable=False)
        self.set_skill(triggerIds=[488], enable=False)
        self.set_skill(triggerIds=[489], enable=False)
        self.set_skill(triggerIds=[490], enable=False)
        self.set_skill(triggerIds=[491], enable=False)
        self.set_skill(triggerIds=[492], enable=False)
        self.set_skill(triggerIds=[493], enable=False)
        self.set_skill(triggerIds=[494], enable=False)
        self.set_skill(triggerIds=[495], enable=False)
        self.set_skill(triggerIds=[496], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬31(self.ctx)


class 스킬31(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[485], enable=True)
        self.set_skill(triggerIds=[486], enable=True)
        self.set_skill(triggerIds=[487], enable=True)
        self.set_skill(triggerIds=[488], enable=True)
        self.set_skill(triggerIds=[489], enable=True)
        self.set_skill(triggerIds=[490], enable=True)
        self.set_skill(triggerIds=[491], enable=True)
        self.set_skill(triggerIds=[492], enable=True)
        self.set_skill(triggerIds=[493], enable=True)
        self.set_skill(triggerIds=[494], enable=True)
        self.set_skill(triggerIds=[495], enable=True)
        self.set_skill(triggerIds=[496], enable=True)
        self.set_skill(triggerIds=[497], enable=True)
        self.set_skill(triggerIds=[498], enable=True)
        self.set_skill(triggerIds=[499], enable=True)
        self.set_skill(triggerIds=[500], enable=True)
        self.set_skill(triggerIds=[501], enable=True)
        self.set_skill(triggerIds=[502], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[485], enable=False)
        self.set_skill(triggerIds=[486], enable=False)
        self.set_skill(triggerIds=[487], enable=False)
        self.set_skill(triggerIds=[488], enable=False)
        self.set_skill(triggerIds=[489], enable=False)
        self.set_skill(triggerIds=[490], enable=False)
        self.set_skill(triggerIds=[491], enable=False)
        self.set_skill(triggerIds=[492], enable=False)
        self.set_skill(triggerIds=[493], enable=False)
        self.set_skill(triggerIds=[494], enable=False)
        self.set_skill(triggerIds=[495], enable=False)
        self.set_skill(triggerIds=[496], enable=False)
        self.set_skill(triggerIds=[497], enable=False)
        self.set_skill(triggerIds=[498], enable=False)
        self.set_skill(triggerIds=[499], enable=False)
        self.set_skill(triggerIds=[500], enable=False)
        self.set_skill(triggerIds=[501], enable=False)
        self.set_skill(triggerIds=[502], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬32(self.ctx)


class 스킬32(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[491], enable=True)
        self.set_skill(triggerIds=[492], enable=True)
        self.set_skill(triggerIds=[493], enable=True)
        self.set_skill(triggerIds=[494], enable=True)
        self.set_skill(triggerIds=[495], enable=True)
        self.set_skill(triggerIds=[496], enable=True)
        self.set_skill(triggerIds=[497], enable=True)
        self.set_skill(triggerIds=[498], enable=True)
        self.set_skill(triggerIds=[499], enable=True)
        self.set_skill(triggerIds=[500], enable=True)
        self.set_skill(triggerIds=[501], enable=True)
        self.set_skill(triggerIds=[502], enable=True)
        self.set_skill(triggerIds=[503], enable=True)
        self.set_skill(triggerIds=[504], enable=True)
        self.set_skill(triggerIds=[505], enable=True)
        self.set_skill(triggerIds=[506], enable=True)
        self.set_skill(triggerIds=[507], enable=True)
        self.set_skill(triggerIds=[508], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=0)
        self.set_skill(triggerIds=[491], enable=False)
        self.set_skill(triggerIds=[492], enable=False)
        self.set_skill(triggerIds=[493], enable=False)
        self.set_skill(triggerIds=[494], enable=False)
        self.set_skill(triggerIds=[495], enable=False)
        self.set_skill(triggerIds=[496], enable=False)
        self.set_skill(triggerIds=[497], enable=False)
        self.set_skill(triggerIds=[498], enable=False)
        self.set_skill(triggerIds=[499], enable=False)
        self.set_skill(triggerIds=[500], enable=False)
        self.set_skill(triggerIds=[501], enable=False)
        self.set_skill(triggerIds=[502], enable=False)
        self.set_skill(triggerIds=[503], enable=False)
        self.set_skill(triggerIds=[504], enable=False)
        self.set_skill(triggerIds=[505], enable=False)
        self.set_skill(triggerIds=[506], enable=False)
        self.set_skill(triggerIds=[507], enable=False)
        self.set_skill(triggerIds=[508], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킬33(self.ctx)


class 스킬33(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[497], enable=True)
        self.set_skill(triggerIds=[498], enable=True)
        self.set_skill(triggerIds=[499], enable=True)
        self.set_skill(triggerIds=[500], enable=True)
        self.set_skill(triggerIds=[501], enable=True)
        self.set_skill(triggerIds=[502], enable=True)
        self.set_skill(triggerIds=[503], enable=True)
        self.set_skill(triggerIds=[504], enable=True)
        self.set_skill(triggerIds=[505], enable=True)
        self.set_skill(triggerIds=[506], enable=True)
        self.set_skill(triggerIds=[507], enable=True)
        self.set_skill(triggerIds=[508], enable=True)
        self.set_skill(triggerIds=[509], enable=True)
        self.set_skill(triggerIds=[510], enable=True)
        self.set_skill(triggerIds=[511], enable=True)
        self.set_skill(triggerIds=[512], enable=True)
        self.set_skill(triggerIds=[513], enable=True)
        self.set_skill(triggerIds=[514], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 끝(self.ctx)


class 끝(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[497], enable=False)
        self.set_skill(triggerIds=[498], enable=False)
        self.set_skill(triggerIds=[499], enable=False)
        self.set_skill(triggerIds=[500], enable=False)
        self.set_skill(triggerIds=[501], enable=False)
        self.set_skill(triggerIds=[502], enable=False)
        self.set_skill(triggerIds=[503], enable=False)
        self.set_skill(triggerIds=[504], enable=False)
        self.set_skill(triggerIds=[505], enable=False)
        self.set_skill(triggerIds=[506], enable=False)
        self.set_skill(triggerIds=[507], enable=False)
        self.set_skill(triggerIds=[508], enable=False)
        self.set_skill(triggerIds=[509], enable=False)
        self.set_skill(triggerIds=[510], enable=False)
        self.set_skill(triggerIds=[511], enable=False)
        self.set_skill(triggerIds=[512], enable=False)
        self.set_skill(triggerIds=[513], enable=False)
        self.set_skill(triggerIds=[514], enable=False)


initial_state = 대기
