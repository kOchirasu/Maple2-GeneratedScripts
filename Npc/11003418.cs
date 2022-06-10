using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003418: Screaming Fist
/// </summary>
public class _11003418 : NpcScript {
    internal _11003418(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008623$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008624$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
