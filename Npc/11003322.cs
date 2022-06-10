using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003322: Soldier
/// </summary>
public class _11003322 : NpcScript {
    internal _11003322(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0424104307008425$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0424104307008426$ 
                // - The enemy is up to something.
                return true;
            default:
                return true;
        }
    }
}
