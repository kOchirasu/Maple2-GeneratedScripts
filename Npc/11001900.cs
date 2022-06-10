using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001900: Lennon
/// </summary>
public class _11001900 : NpcScript {
    internal _11001900(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122193107007458$ 
                // - Eve was right...
                return true;
            case 30:
                // $script:1122193107007461$ 
                // - We've got to hold out long enough for Eve to get reinforcements.
                return true;
            default:
                return true;
        }
    }
}
