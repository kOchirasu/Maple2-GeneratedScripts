using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003259: Einos
/// </summary>
public class _11003259 : NpcScript {
    internal _11003259(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008194$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0403155707008195$ 
                // - I hope everyone's all right.  
                return true;
            default:
                return true;
        }
    }
}
