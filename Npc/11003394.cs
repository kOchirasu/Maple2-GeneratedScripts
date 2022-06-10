using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003394: Yohoi
/// </summary>
public class _11003394 : NpcScript {
    internal _11003394(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008593$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008594$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
