using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001348: Cathy Catalina
/// </summary>
public class _11001348 : NpcScript {
    internal _11001348(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005305$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1217012607005308$ 
                // -  I came here to expand my business, but my partner is being completely impossible. And on top of that, the weather's too hot here and the people are too stubborn. What a terrible day...
                return true;
            default:
                return true;
        }
    }
}
