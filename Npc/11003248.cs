using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003248: Strange Wall
/// </summary>
public class _11003248 : NpcScript {
    internal _11003248(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008163$ 
                // - <font color="#909090">(You feel a chill from behind the waterfall.)</font>
                return true;
            case 30:
                // $script:0403155707008164$ 
                // - <font color="#909090">(Maybe there's something there... or maybe not.)</font>
                return true;
            default:
                return true;
        }
    }
}
