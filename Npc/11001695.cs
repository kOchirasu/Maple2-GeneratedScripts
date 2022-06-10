using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001695: 
/// </summary>
public class _11001695 : NpcScript {
    internal _11001695(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0702184010001573$ 
                // - Welcome, welcome!
                return true;
            case 30:
                // $script:0702184010001574$ 
                // - Would you like to spin $npc:11001695$?
                switch (selection) {
                    // $script:0702184010001575$
                    // - Pay 50,000 mesos, then spin!
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0702184010001576$
                    // - Pay the $item:30000557$, then spin!
                    case 1:
                        Id = 0; // TODO: 33 | 34
                        return false;
                }
                return true;
            case 31:
                // $script:0702184010001577$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                // $script:0702184010001578$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return true;
            case 32:
                // $script:0702184010001579$ 
                // - A roulette spin costs 50,000 mesos.
                //   If you don't have enough mesos, you can always use $itemPlural:30000557$ instead.
                return true;
            case 33:
                // $script:0702184010001580$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                // $script:0702184010001581$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return true;
            case 34:
                // $script:0702184010001582$ 
                // - Spinning the roulette costs $itemPlural:30000557$. But don't fret! You can get 2 $itemPlural:30000557$ in your mailbox on weekdays, and 4 of them on Saturdays and Sundays!
                return true;
            default:
                return true;
        }
    }
}
