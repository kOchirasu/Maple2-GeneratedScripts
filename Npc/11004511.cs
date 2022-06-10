using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004511: Mannstad Patrolman
/// </summary>
public class _11004511 : NpcScript {
    internal _11004511(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012461$ 
                // - Ugh... I'm ready to pass out on my feet...
                return true;
            case 10:
                // $script:1228182607012462$ 
                // - Ugh... I'm ready to pass out on my feet...
                // $script:1228182607012463$ 
                // - AAAAH! Ugh, you startled me.
                return true;
            default:
                return true;
        }
    }
}
