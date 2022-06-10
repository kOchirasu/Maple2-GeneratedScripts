using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001118: Happi
/// </summary>
public class _11001118 : NpcScript {
    internal _11001118(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0909142907003751$ 
                // - Welcome, $MyPCName$! 
                return true;
            case 40:
                // $script:0909142907003755$ 
                // - Did you come to join the event? I'm sorry, but you forgot the most important thing. To spin this $npcName:11001120$, you need a $item:30000406$. Luckily, they're easy to get! 
                // $script:0914175707003914$ 
                // - You'll get a <i>free cake</i> in the mail every 20 minutes, just for having a good time in Maple World! You can receive up to <b>9 a day</b>. If you get a hold of a $item:30000406$, be sure to swing by $map:02000064$! 
                return true;
            case 50:
                // $script:0909142907003756$ 
                // - Oh good, you have a $item:30000406$! You can use $itemPlural:30000406$ to spin this here $npcName:11001120$ next to me for a chance to win great prizes. Come on, why not try it? 
                return true;
            default:
                return true;
        }
    }
}
