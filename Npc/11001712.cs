using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001712: Tinchai
/// </summary>
public class _11001712 : NpcScript {
    internal _11001712(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006964$ 
                // - Mm? Yes?
                return true;
            case 30:
                // $script:0728024507006998$ 
                // - The artifact must be hidden somewhere nearby. Or something related to it, at the very least.
                return true;
            default:
                return true;
        }
    }
}
