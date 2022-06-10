using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003450: Rolling Thunder
/// </summary>
public class _11003450 : NpcScript {
    internal _11003450(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008655$ 
                // - I wonder if father is all right...
                return true;
            case 10:
                // $script:0706160807008656$ 
                // - I wonder if father is all right...
                return true;
            default:
                return true;
        }
    }
}
