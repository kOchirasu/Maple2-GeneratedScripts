using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003388: Screaming Fist
/// </summary>
public class _11003388 : NpcScript {
    internal _11003388(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0722190307008718$ 
                // - Thanks for the help.
                return true;
            case 10:
                // $script:0722190307008719$ 
                // - Thanks for the help.
                return true;
            default:
                return true;
        }
    }
}
