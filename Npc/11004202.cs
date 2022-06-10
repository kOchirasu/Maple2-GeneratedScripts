using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004202: Tourist
/// </summary>
public class _11004202 : NpcScript {
    internal _11004202(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010652$ 
                // - Hello.
                return true;
            case 10:
                // $script:0806025707010653$ 
                // - Y'know, I wasn't so sure about those mushfolk when I got the brochure, but I've gotta say this place is pretty great!
                return true;
            default:
                return true;
        }
    }
}
