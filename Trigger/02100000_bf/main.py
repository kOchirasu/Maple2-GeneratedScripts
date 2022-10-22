""" trigger/02100000_bf/main.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_user():
            return CheckUser10_GuildRaid()


class CheckUser10_GuildRaid(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=False, arg5=0) # 최대 30초 대기

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if count_users(boxId=101, boxId=10, operator='Less'):
            return MaxCount10_Wait()


class MaxCount10_Wait(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if time_expired(timerId='1'):
            return MaxCount10_Start()
        if wait_tick(waitTick=6000):
            return MaxCount10_Wait()


class MaxCount10_Start(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if true():
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        select_camera(triggerId=904, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShowCaption01()

state.DungeonStart = DungeonStart


#  설명문 출력 
class ShowCaption01(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100000_BF__MAIN__0$')
        set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return ShowCaption01Skip()


class ShowCaption01Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption02()


class ShowCaption02(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100000_BF__MAIN__1$')
        set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return ShowCaption02Skip()


class ShowCaption02Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CloseCaptionSetting()


class CloseCaptionSetting(state.State):
    def on_enter(self):
        close_cinematic()
        select_camera(triggerId=904, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000133, level=1, arg4=False, arg5=False)
        add_buff(boxIds=[101], skillId=70000133, level=1, arg4=False, arg5=True)
        set_effect(triggerIds=[8001], visible=False)
        set_effect(triggerIds=[8002], visible=False)
        set_effect(triggerIds=[8003], visible=False)
        set_mesh(triggerIds=[80000], visible=False, arg3=0, arg4=0, arg5=0)
        set_skill(triggerIds=[910001], isEnable=True)
        set_skill(triggerIds=[910002], isEnable=True)
        set_skill(triggerIds=[910003], isEnable=True)
        set_skill(triggerIds=[910004], isEnable=True)
        set_skill(triggerIds=[910005], isEnable=True)
        set_skill(triggerIds=[910006], isEnable=True)
        set_skill(triggerIds=[910007], isEnable=True)
        set_skill(triggerIds=[910008], isEnable=True)
        set_skill(triggerIds=[910009], isEnable=True)
        set_skill(triggerIds=[910010], isEnable=True)
        set_skill(triggerIds=[910011], isEnable=True)
        set_skill(triggerIds=[910012], isEnable=True)
        set_skill(triggerIds=[910013], isEnable=True)
        set_skill(triggerIds=[910014], isEnable=True)
        set_skill(triggerIds=[910015], isEnable=True)
        set_skill(triggerIds=[910016], isEnable=True)
        set_skill(triggerIds=[910017], isEnable=True)
        set_skill(triggerIds=[910018], isEnable=True)
        set_skill(triggerIds=[910019], isEnable=True)
        set_skill(triggerIds=[910020], isEnable=True)
        set_skill(triggerIds=[920001], isEnable=True)
        set_skill(triggerIds=[920002], isEnable=True)
        set_skill(triggerIds=[920003], isEnable=True)
        set_skill(triggerIds=[920004], isEnable=True)
        set_skill(triggerIds=[920005], isEnable=True)
        set_skill(triggerIds=[920006], isEnable=True)
        set_skill(triggerIds=[920007], isEnable=True)
        set_skill(triggerIds=[920008], isEnable=True)
        set_skill(triggerIds=[920009], isEnable=True)
        set_skill(triggerIds=[920010], isEnable=True)
        set_skill(triggerIds=[920011], isEnable=True)
        set_skill(triggerIds=[920012], isEnable=True)
        set_skill(triggerIds=[920013], isEnable=True)
        set_skill(triggerIds=[920014], isEnable=True)
        set_skill(triggerIds=[920015], isEnable=True)
        set_skill(triggerIds=[930001], isEnable=True)
        set_skill(triggerIds=[930002], isEnable=True)
        set_skill(triggerIds=[930003], isEnable=True)
        set_skill(triggerIds=[930004], isEnable=True)
        set_skill(triggerIds=[930005], isEnable=True)
        set_skill(triggerIds=[930006], isEnable=True)
        set_skill(triggerIds=[930007], isEnable=True)
        set_skill(triggerIds=[930008], isEnable=True)
        set_skill(triggerIds=[930009], isEnable=True)
        set_skill(triggerIds=[930010], isEnable=True)
        set_skill(triggerIds=[930011], isEnable=True)
        set_skill(triggerIds=[930012], isEnable=True)
        set_skill(triggerIds=[930013], isEnable=True)
        set_skill(triggerIds=[930014], isEnable=True)
        set_skill(triggerIds=[930015], isEnable=True)
        set_skill(triggerIds=[930016], isEnable=True)
        set_skill(triggerIds=[940001], isEnable=True)
        set_skill(triggerIds=[940002], isEnable=True)
        set_skill(triggerIds=[940003], isEnable=True)
        set_skill(triggerIds=[940004], isEnable=True)
        set_skill(triggerIds=[940005], isEnable=True)
        set_skill(triggerIds=[940006], isEnable=True)
        set_skill(triggerIds=[940007], isEnable=True)
        set_skill(triggerIds=[940008], isEnable=True)
        set_skill(triggerIds=[940009], isEnable=True)
        set_skill(triggerIds=[940010], isEnable=True)
        set_skill(triggerIds=[940011], isEnable=True)
        set_skill(triggerIds=[940012], isEnable=True)
        set_skill(triggerIds=[940013], isEnable=True)
        set_skill(triggerIds=[940014], isEnable=True)
        set_skill(triggerIds=[940015], isEnable=True)
        set_skill(triggerIds=[940016], isEnable=True)
        set_skill(triggerIds=[940017], isEnable=True)
        set_skill(triggerIds=[940018], isEnable=True)
        set_skill(triggerIds=[940019], isEnable=True)
        set_skill(triggerIds=[940020], isEnable=True)
        set_skill(triggerIds=[940021], isEnable=True)
        set_skill(triggerIds=[940022], isEnable=True)
        set_skill(triggerIds=[940023], isEnable=True)
        set_skill(triggerIds=[940024], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버프_2()


class 버프_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02100000_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 바리케이트()


class 바리케이트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02100000_BF__MAIN__3$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 닫기()


class 닫기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8001], visible=True)
        set_effect(triggerIds=[8002], visible=True)
        set_effect(triggerIds=[8003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


