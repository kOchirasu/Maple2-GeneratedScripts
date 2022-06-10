using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003379: Haster
/// </summary>
public class _11003379 : NpcScript {
    internal _11003379(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0613105907008550$ 
                // - ...
                return true;
            case 10:
                // $script:0613105907008551$ 
                // - Can't you find someone else to bother...?
                return true;
            default:
                return true;
        }
    }
}
