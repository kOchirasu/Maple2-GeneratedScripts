using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001308: Dunbard
/// </summary>
public class _11001308 : NpcScript {
    internal _11001308(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005027$ 
                // - Hello!
                return true;
            case 30:
                // $script:1227194507005653$ 
                // - Do you need something?
                // $script:1227194507005654$ 
                // - If I don't have it, then it probably doesn't exist. I'm also interested in buying rare and unusual pieces.
                // $script:1227194507005655$ 
                // - Take a look! I'm sure something will catch your fancy.
                return true;
            default:
                return true;
        }
    }
}
