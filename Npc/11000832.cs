using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000832: Whitingale
/// </summary>
public class _11000832 : NpcScript {
    internal _11000832(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003044$ 
                // - Whew, I wish I had more hands.
                return true;
            case 20:
                // $script:0831180407003046$ 
                // - There's no better medicine than hope. Stop being a crybaby and come over here.
                return true;
            default:
                return true;
        }
    }
}
