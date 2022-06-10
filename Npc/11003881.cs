using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003881: Gardener
/// </summary>
public class _11003881 : NpcScript {
    internal _11003881(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009878$ 
                // - Whenever a new herb is discovered, I plant it here.
                return true;
            case 10:
                // $script:0417135107009879$ 
                // - Whenever a new herb is discovered, I plant it here.
                return true;
            default:
                return true;
        }
    }
}
