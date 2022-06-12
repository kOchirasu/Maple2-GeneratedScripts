using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001695: 
/// </summary>
public class _11001695 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0702184010001573$ 
                // - Welcome, welcome!
                return default;
            case 30:
                // $script:0702184010001574$ 
                // - Would you like to spin $npc:11001695$?
                switch (selection) {
                    // $script:0702184010001575$
                    // - Pay 50,000 mesos, then spin!
                    case 0:
                        // TODO: goto 31
                        // (Id, Button) = (31, NpcTalkButton.Next);
                        // TODO: gotoFail 32
                        // (Id, Button) = (32, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0702184010001576$
                    // - Pay the $item:30000557$, then spin!
                    case 1:
                        // TODO: goto 33
                        // (Id, Button) = (33, NpcTalkButton.Next);
                        // TODO: gotoFail 34
                        // (Id, Button) = (34, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 31:
                switch (Index++) {
                    case 0:
                        // $script:0702184010001577$ functionID=1 buttonSet=16 
                        // - Spin the roulette for a chance to win great prizes!
                        //   Come on, you know you want to!
                        return (31, NpcTalkButton.Close);
                    case 1:
                        // $script:0702184010001578$ buttonSet=1 
                        // - May Lady Luck blow you a kiss, $MyPCName$!
                        return default;
                }
                break;
            case 32:
                // $script:0702184010001579$ 
                // - A roulette spin costs 50,000 mesos.
                //   If you don't have enough mesos, you can always use $itemPlural:30000557$ instead.
                return default;
            case 33:
                switch (Index++) {
                    case 0:
                        // $script:0702184010001580$ functionID=1 buttonSet=16 
                        // - Spin the roulette for a chance to win great prizes!
                        //   Come on, you know you want to!
                        return (33, NpcTalkButton.Close);
                    case 1:
                        // $script:0702184010001581$ buttonSet=1 
                        // - May Lady Luck blow you a kiss, $MyPCName$!
                        return default;
                }
                break;
            case 34:
                // $script:0702184010001582$ 
                // - Spinning the roulette costs $itemPlural:30000557$. But don't fret! You can get 2 $itemPlural:30000557$ in your mailbox on weekdays, and 4 of them on Saturdays and Sundays!
                return default;
        }
        
        return default;
    }
}
