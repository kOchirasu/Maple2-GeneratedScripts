using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003356: Ralph's Lackey
/// </summary>
public class _11003356 : NpcScript {
    internal _11003356(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008509$ 
                // - Get away from me. I <i>really</i> don't want to talk to you.
                return true;
            case 20:
                // $script:0517164307008511$ 
                // - There's no way the big guy will lose to such a weakling.
                return true;
            default:
                return true;
        }
    }
}
