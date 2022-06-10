using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004316: Mason
/// </summary>
public class _11004316 : NpcScript {
    internal _11004316(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0928133807011358$ 
                // - It is time my order stood with the rest of the empire.
                return true;
            case 10:
                // $script:0928133807011359$ 
                // - A strange power hangs over this place. A dark power... 
                return true;
            case 20:
                // $script:0116153807012736$ 
                // - Return to me when the time is right.
                return true;
            default:
                return true;
        }
    }
}
