using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003870: Donald
/// </summary>
public class _11003870 : NpcScript {
    internal _11003870(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009856$ 
                // - Welcome to $map:02000424$. Enjoy your stay! 
                return true;
            case 10:
                // $script:0417135107009857$ 
                // - Beautiful day, isn't it? 
                return true;
            case 20:
                // $script:0419172107009856$ 
                // - Welcome to $map:02000424$. Enjoy your stay! 
                return true;
            default:
                return true;
        }
    }
}
