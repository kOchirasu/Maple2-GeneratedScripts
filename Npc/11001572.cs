using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001572: Ishura
/// </summary>
public class _11001572 : NpcScript {
    internal _11001572(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006060$ 
                // - Ah, $MyPCName$!
                return true;
            case 10:
                // $script:0515180307006113$ 
                // - The bond between our ancestors makes us strong. I couldn't be more grateful. 
                // $script:0515180307006114$ 
                // - $MyPCName$, remember: no one crosses paths by accident. Be kind to everyone you meet, no matter how insignificant they may seem at the time.
                return true;
            case 20:
                // $script:0524142307006213$ 
                // - The bond between our ancestors makes us strong. I couldn't be more grateful. 
                return true;
            default:
                return true;
        }
    }
}
