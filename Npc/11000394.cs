using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000394: Emma
/// </summary>
public class _11000394 : NpcScript {
    internal _11000394(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001600$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407001602$ 
                // - They say that old miser, $npcName:11000252[gender:0]$, is the worst... but they haven't met $npcName:11000491[gender:1]$!
                return true;
            default:
                return true;
        }
    }
}
