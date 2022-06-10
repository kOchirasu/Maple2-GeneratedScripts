using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001669: Happi
/// </summary>
public class _11001669 : NpcScript {
    internal _11001669(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0620231807006383$ 
                // - Welcome, $MyPCName$!
                return true;
            case 40:
                // $script:0620231807006387$ 
                // - For one spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
                // $script:0620231807006388$ 
                // - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
                return true;
            default:
                return true;
        }
    }
}
