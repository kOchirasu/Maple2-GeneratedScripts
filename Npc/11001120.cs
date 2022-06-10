using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001120: Lucky Wheel
/// </summary>
public class _11001120 : NpcScript {
    internal _11001120(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0909140310001157$;$script:0909140310001158$;$script:0909140310001159$
        // Id = 30;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0909140310001156$ 
                // - Spin the $npc:11001120$ for just 1 $item:30000406$! 
                return true;
            case 30:
                // $script:0909140310001157$ 
                // - Look at all those $itemPlural:30000406$> you've got! You're sitting pretty! Why don't you invest them in a chance to spin the $npc:11001120$? Could be a wise investment, indeed! 
                // $script:0909140310001158$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to. 
                // $script:0909140310001159$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 40:
                // $script:0909140310001160$ 
                // - To take a spin on the $npc:11001120$, you need $itemPlural:30000406$. But good news! You can get 1 $item:30000406$ in your mailbox every 20 minutes, up to 9 times a day. 
                // $script:0909140310001161$ 
                // - If you get a $item:30000406$, don't forget to come to $map:02000064$! 
                return true;
            default:
                return true;
        }
    }
}
