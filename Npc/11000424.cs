using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000424: Old Lady Balmony
/// </summary>
public class _11000424 : NpcScript {
    internal _11000424(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001767$ 
                // - What is it? 
                return true;
            case 60:
                // $script:0831180407001771$ 
                // - Have you seen a lost, crying girl on the street? She's carrying a doll in her arms like it's a real baby. 
                return true;
            default:
                return true;
        }
    }
}
