using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000269: Zachary
/// </summary>
public class _11000269 : NpcScript {
    internal _11000269(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000810$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:1121222006000811$ 
                // - Helping others is a wonderful thing. 
                return true;
            default:
                return true;
        }
    }
}
