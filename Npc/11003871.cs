using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003871: Mighton
/// </summary>
public class _11003871 : NpcScript {
    internal _11003871(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009858$ 
                // - Are you supposed to be here? 
                return true;
            case 10:
                // $script:0417135107009859$ 
                // - I hate, hate, <i>hate</i> managing people! 
                return true;
            default:
                return true;
        }
    }
}
