""" trigger/82000003_survival/17_noticeextraevent.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_user_value(key='NoticeExtraEvent', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='NoticeExtraEvent', value=1):
            return NoticeExtraEvent01()


class NoticeExtraEvent01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28200000, textId=28200000, duration=3000) # 가이드 : 누군가 [b:모쿰]을 목격했습니다!
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NoticeExtraEvent02()


class NoticeExtraEvent02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__17_NoticeExtraEvent__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NoticeExtraEvent03()


class NoticeExtraEvent03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28200001, textId=28200001, duration=5000) # 가이드 : [b:다섯 마리]의 모쿰이 섬 어딘가에 있습니다!
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')


