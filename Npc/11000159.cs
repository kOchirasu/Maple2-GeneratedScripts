using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000159: Tommy
/// </summary>
public class _11000159 : NpcScript {
    internal _11000159(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000670$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407000672$ 
                // - This place is extremely dangerous. Be careful not to fall. 
                return true;
            case 30:
                // $script:0831180407000673$ 
                // - The others must be quite anxious, since they don't know what's going on. 
                return true;
            default:
                return true;
        }
    }
}
