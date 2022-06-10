using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000504: Rue
/// </summary>
public class _11000504 : NpcScript {
    internal _11000504(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002187$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:1217012607005230$ 
                // - This place is... How do I say? Full of contradictions. A rich, gorgeous facade that hides a lingering melancholy. This hotel is luxurious, but it's not for the regular people who live around it. Those people belong to a different world. 
                return true;
            default:
                return true;
        }
    }
}
