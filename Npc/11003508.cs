using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003508: Sana
/// </summary>
public class _11003508 : NpcScript {
    internal _11003508(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009011$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0816160115009012$ 
                // - My parents ran this store before my brother inherited it. And now he's chasing his dream of turning it into a cafe or something...
                return true;
            case 40:
                // $script:0816160115009013$ 
                // - The cafe's being remodeled right now. You should swing by when it reopens!
                return true;
            default:
                return true;
        }
    }
}
