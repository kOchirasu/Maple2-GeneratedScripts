using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004078: Scribbles under the Bridge
/// </summary>
public class _11004078 : NpcScript {
    internal _11004078(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010226$ 
                // - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
                return true;
            case 10:
                // $script:0619202207010227$ 
                // - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
                // $script:0619202207010228$ 
                // - <i>$npcName:11000015[gender:1]$'s secret, exposed! She actually has a boyfriend! We've been betrayed!</i>
                // $script:0619202207010229$ 
                // - <font color="#909090">(Is the person who wrote this... angry? $npcName:11000015[gender:1]$'s fans can be scary sometimes...)</font>
                // $script:0619202207010230$ 
                // - <font color="#909090">(Wait. There's another note written here!)</font>
                // $script:0619202207010231$ 
                // - <i>Interesting rumor. If you happen to meet my boyfriend, bring him to me. I want to know what he looks like.
                //   - $npcName:11000015[gender:1]$</i>
                return true;
            default:
                return true;
        }
    }
}
