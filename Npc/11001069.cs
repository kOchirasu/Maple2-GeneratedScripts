using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001069: Yorke
/// </summary>
public class _11001069 : NpcScript {
    internal _11001069(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003643$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407003646$ 
                // - I like groupies, so long as they don't steal my things. 
                return true;
            default:
                return true;
        }
    }
}
