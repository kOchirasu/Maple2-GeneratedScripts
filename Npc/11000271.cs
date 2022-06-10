using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000271: Jeffery
/// </summary>
public class _11000271 : NpcScript {
    internal _11000271(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000815$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:1121222006000816$ 
                // - How may I help you? 
                return true;
            default:
                return true;
        }
    }
}
