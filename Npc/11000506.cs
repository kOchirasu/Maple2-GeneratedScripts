using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000506: Blackstar Gangster
/// </summary>
public class _11000506 : NpcScript {
    internal _11000506(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002191$ 
                // - What brings you here?
                return true;
            case 10:
                // $script:0831180407002192$ 
                // - Who are you? I don't recognize you. 
                return true;
            default:
                return true;
        }
    }
}
