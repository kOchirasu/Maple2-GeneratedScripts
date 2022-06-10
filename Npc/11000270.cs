using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000270: Gabrielle
/// </summary>
public class _11000270 : NpcScript {
    internal _11000270(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000812$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:1121222006000813$ 
                // - Plants will liven up your house.
                return true;
            default:
                return true;
        }
    }
}
