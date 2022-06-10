using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000505: Blackstar Gangster
/// </summary>
public class _11000505 : NpcScript {
    internal _11000505(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002188$ 
                // - What brings you here? 
                return true;
            case 10:
                // $script:0831180407002189$ 
                // - Scram, punk.  
                return true;
            case 20:
                // $script:0831180407002190$ 
                // - Who are you? Stop bothering me. 
                return true;
            default:
                return true;
        }
    }
}
