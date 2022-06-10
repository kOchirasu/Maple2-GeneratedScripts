using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001332: Armachio
/// </summary>
public class _11001332 : NpcScript {
    internal _11001332(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005248$ 
                // - Ugh...
                return true;
            case 30:
                // $script:1217012607005251$ 
                // - Those knuckleheads! Why do they have to fight in here? They'll scare away the customers!
                return true;
            default:
                return true;
        }
    }
}
