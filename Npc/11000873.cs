using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000873: Bostie
/// </summary>
public class _11000873 : NpcScript {
    internal _11000873(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003155$ 
                // - Sigh...
                return true;
            case 30:
                // $script:0831180407003158$ 
                // - I've got this awful, creeping feeling that something bad is coming. I really hope I'm wrong.
                return true;
            default:
                return true;
        }
    }
}
