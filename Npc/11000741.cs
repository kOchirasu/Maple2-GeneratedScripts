using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000741: Bevento
/// </summary>
public class _11000741 : NpcScript {
    internal _11000741(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002883$ 
                // - What? I'm in the middle of creating music that speaks to the soul!
                return true;
            case 20:
                // $script:0831180407002885$ 
                // - Sigh... Do you even know the pain of creation? Bah, there's no soul in this music. If there was, I'd be able to feel it!
                return true;
            default:
                return true;
        }
    }
}
