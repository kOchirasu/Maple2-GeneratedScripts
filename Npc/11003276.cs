using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003276: Old Lady Balmony
/// </summary>
public class _11003276 : NpcScript {
    internal _11003276(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0405160907008263$ 
                // - What is it?
                return true;
            case 30:
                // $script:0405160907008266$ 
                // - Who goes there? My eyes aren't what they used to be.
                return true;
            default:
                return true;
        }
    }
}
