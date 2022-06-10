using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000602: Tarre
/// </summary>
public class _11000602 : NpcScript {
    internal _11000602(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002479$ 
                // - Ugh... What... brings you... to me? 
                return true;
            case 20:
                // $script:0831180407002481$ 
                // - P-please go... I'll be okay...  
                return true;
            default:
                return true;
        }
    }
}
