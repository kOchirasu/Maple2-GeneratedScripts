using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004241: Landevian
/// </summary>
public class _11004241 : NpcScript {
    internal _11004241(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010943$ 
                // - I'm ashamed of myself.
                return true;
            case 10:
                // $script:0809223207010944$ 
                // - I'm ashamed of myself.
                // $script:0809223207010945$ 
                // - What you saw back there, that wasn't me.
                // $script:0809223207010946$ 
                // - You better not tell anyone else about this! Especially not $npcName:11004054[gender:1]$!
                return true;
            default:
                return true;
        }
    }
}
