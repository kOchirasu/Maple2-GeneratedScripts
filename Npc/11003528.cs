using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003528: Small Hut
/// </summary>
public class _11003528 : NpcScript {
    internal _11003528(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816165015009054$ 
                // - (It's locked.)
                return true;
            case 30:
                // $script:0816165015009055$ 
                // - (It's locked.)
                return true;
            default:
                return true;
        }
    }
}
