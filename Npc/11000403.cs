using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000403: Hochi
/// </summary>
public class _11000403 : NpcScript {
    internal _11000403(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001631$ 
                // - Uuugh...  
                return true;
            case 20:
                // $script:0831180407001633$ 
                // - I-I can't... speak...  
                return true;
            default:
                return true;
        }
    }
}
