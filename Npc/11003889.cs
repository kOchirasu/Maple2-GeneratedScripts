using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003889: Piris
/// </summary>
public class _11003889 : NpcScript {
    internal _11003889(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009933$ 
                // - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
                return true;
            case 20:
                // $script:0515102507009934$ 
                // - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
                return true;
            case 30:
                // $script:0515102507009935$ 
                // - I'll punish any who threaten the seas. Even you.
                return true;
            default:
                return true;
        }
    }
}
