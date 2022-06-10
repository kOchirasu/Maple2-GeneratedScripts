using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001666: Frey
/// </summary>
public class _11001666 : NpcScript {
    internal _11001666(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617211107006381$ 
                // - I look forward to hearing more stories of your heroism.
                return true;
            case 10:
                // $script:0617211107006382$ 
                // - Please remain steadfast in your efforts to protect peace and justice.
                return true;
            default:
                return true;
        }
    }
}
