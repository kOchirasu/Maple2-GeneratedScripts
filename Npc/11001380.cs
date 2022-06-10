using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001380: Balba
/// </summary>
public class _11001380 : NpcScript {
    internal _11001380(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005377$ 
                // - Mm? What?
                return true;
            case 30:
                // $script:1217144507005380$ 
                // - Who are these guys? Get them out of here! The match would already be over by now if they didn't ruin everything!
                return true;
            default:
                return true;
        }
    }
}
