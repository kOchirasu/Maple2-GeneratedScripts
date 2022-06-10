using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000305: Broh
/// </summary>
public class _11000305 : NpcScript {
    internal _11000305(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000817$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:1121222006000818$ 
                // - Pretty homes are nice to live in. 
                return true;
            default:
                return true;
        }
    }
}
