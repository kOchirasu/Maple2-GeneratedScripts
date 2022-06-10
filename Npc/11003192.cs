using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003192: Kyle
/// </summary>
public class _11003192 : NpcScript {
    internal _11003192(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0405160907008256$ 
                // - Heh heh heh...
                return true;
            case 30:
                // $script:0405160907008258$ 
                // - What brings you here?
                return true;
            default:
                return true;
        }
    }
}
