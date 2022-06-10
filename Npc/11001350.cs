using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001350: Oliver Olivieta
/// </summary>
public class _11001350 : NpcScript {
    internal _11001350(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005313$ 
                // - Good. Right. Perfect!
                return true;
            case 30:
                // $script:1217012607005316$ 
                // - Yeeees? It's rude to barge in on someone's summer home, you know. Please remove yourself from the premises.
                return true;
            default:
                return true;
        }
    }
}
