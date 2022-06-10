using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001839: Joddy
/// </summary>
public class _11001839 : NpcScript {
    internal _11001839(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1020165907007297$ 
                // - Ah... What should I do? 
                return true;
            case 30:
                // $script:1020165907007300$ 
                // - I can't wait to become a full-fledged guard. 
                switch (selection) {
                    // $script:1020165907007301$
                    // - Did you run into any mushrooms on the way here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1020165907007302$ 
                // - M-mushrooms? Are there mushrooms here? Oh no... 
<font color="#909090">(All the color drains from $npcName:11001839[gender:0]$'s face. What terrible happening has made him so afraid of something as innocuous as mushrooms?)</font> 
                switch (selection) {
                    // $script:1020165907007303$
                    // - Relax, I was only kidding.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1020165907007304$ 
                // - H-how could you do that to me, $MyPCName$? I... I thought we were friends. Have you just been pretending to like me all this time?
<font color="#909090">($npcName:11001839[gender:0]$'s eyes begin to water.)</font> 
                return true;
            default:
                return true;
        }
    }
}
