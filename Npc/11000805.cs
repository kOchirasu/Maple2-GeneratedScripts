using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000805: Hozzie
/// </summary>
public class _11000805 : NpcScript {
    internal _11000805(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002966$ 
                // - H-how can I...? 
                return true;
            case 20:
                // $script:0831180407002968$ 
                // - I don't care who you are. Just stop talking to me. They'll beat me up if they see me talking to you.
                return true;
            default:
                return true;
        }
    }
}
