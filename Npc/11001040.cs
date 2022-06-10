using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001040: Fordson
/// </summary>
public class _11001040 : NpcScript {
    internal _11001040(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003552$ 
                // - The wind is so cold.
                return true;
            case 30:
                // $script:0831180407003555$ 
                // - Maritime Leaguers are atmospheric, oceanic, and geologic specialists gathered to observe and collect information about the oceans and everything in it.
                return true;
            default:
                return true;
        }
    }
}
