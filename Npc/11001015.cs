using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001015: Yena
/// </summary>
public class _11001015 : NpcScript {
    internal _11001015(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003459$ 
                // - Hello.
                return true;
            case 30:
                // $script:0831180407003462$ 
                // - Each magic-user has their own spell. I haven't chosen mine yet. Alio olio! Hoi, hoi! Chacharachat! Which one sounds the best to you?
                return true;
            default:
                return true;
        }
    }
}
