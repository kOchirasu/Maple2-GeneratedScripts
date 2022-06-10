using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000539: Lennon
/// </summary>
public class _11000539 : NpcScript {
    internal _11000539(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002304$ 
                // - What brings you here? 
                return true;
            case 10:
                // $script:0831180407002305$ 
                // - Ugh...  
                return true;
            default:
                return true;
        }
    }
}
