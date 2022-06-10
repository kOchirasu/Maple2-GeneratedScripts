using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001335: Tizzy
/// </summary>
public class _11001335 : NpcScript {
    internal _11001335(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005259$ 
                // - Oh, wait...
                return true;
            case 30:
                // $script:1217012607005262$ 
                // - I forgot to return the board I rented and road it all the way home. I don't want to go all the way back to the rental place... Maybe I should just buy one for myself.
                return true;
            default:
                return true;
        }
    }
}
