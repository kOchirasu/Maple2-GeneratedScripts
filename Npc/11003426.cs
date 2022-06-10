using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003426: Yohoi
/// </summary>
public class _11003426 : NpcScript {
    internal _11003426(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008639$ 
                // - Yoo-hoo! 
                return true;
            case 10:
                // $script:0706160807008640$ 
                // - Yoo-hoo! 
                return true;
            default:
                return true;
        }
    }
}
