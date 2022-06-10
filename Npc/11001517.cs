using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001517: Lucky Wheel
/// </summary>
public class _11001517 : NpcScript {
    internal _11001517(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0204150510001434$ 
                // - Welcome, welcome! 
                return true;
            case 30:
                // $script:0217184010001441$ 
                // - Would you like to spin the $npcName:11001517$? 
                switch (selection) {
                    // $script:0217184010001442$
                    // - (Pay 50,000 mesos for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0217184010001443$
                    // - (Pay 1 $item:30000522$ for 1 spin.)
                    case 1:
                        Id = 0; // TODO: 33 | 34
                        return false;
                }
                return true;
            case 31:
                // $script:0217184010001444$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to. 
                // $script:0217184010001445$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 32:
                // $script:0217184010001446$ 
                // - It costs 50,000 mesos for a spin. If you don't have enough mesos, you can always use $itemPlural:30000522$ instead. 
                return true;
            case 33:
                // $script:0217184010001447$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to. 
                // $script:0217184010001448$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 34:
                // $script:0217184010001449$ 
                // - Spinning the roulette costs $itemPlural:30000522$. But don't fret! You can get 1 $item:30000522$ in your mailbox on weekdays and 5 of them on Saturdays and Sundays! 
                return true;
            default:
                return true;
        }
    }
}
