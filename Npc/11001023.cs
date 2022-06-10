using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001023: Lennon
/// </summary>
public class _11001023 : NpcScript {
    internal _11001023(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003476$ 
                // - No...
                return true;
            case 30:
                // $script:0831180407003477$ 
                // - To let him slip through my fingers... After everything he put me through...
                return true;
            default:
                return true;
        }
    }
}
