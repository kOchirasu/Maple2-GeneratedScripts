using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000309: Elvis
/// </summary>
public class _11000309 : NpcScript {
    internal _11000309(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000823$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:1121222006000824$ 
                // - I dream of developing tall buildings or landmark packages. 
                return true;
            default:
                return true;
        }
    }
}
