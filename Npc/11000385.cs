using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000385: Shalin
/// </summary>
public class _11000385 : NpcScript {
    internal _11000385(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001568$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0831180407001570$ 
                // - If you see trash on the street, by all means pick it up! Everyone has to do their part to keep their homes clean.
                return true;
            default:
                return true;
        }
    }
}
