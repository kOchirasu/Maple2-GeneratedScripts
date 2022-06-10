using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003891: Dark Lord
/// </summary>
public class _11003891 : NpcScript {
    internal _11003891(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009939$ 
                // - What is it?
                return true;
            case 20:
                // $script:0515102507009940$ 
                // - What is it?
                return true;
            case 30:
                // $script:0515102507009941$ 
                // - Even though the request came from the $npc:11003894[gender:0]$, I'm not interested.
                return true;
            default:
                return true;
        }
    }
}
