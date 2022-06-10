using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004034: Lanemone
/// </summary>
public class _11004034 : NpcScript {
    internal _11004034(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010053$ 
                // - Sigh... How did I end up with that one again? We have unfinished business.
                return true;
            case 20:
                // $script:0614185307010054$ 
                // - Sigh... This one is useless without me. That's why I'm always busy cleaning up the mess. Can't really say whether or not I like it at this point.
                return true;
            default:
                return true;
        }
    }
}
