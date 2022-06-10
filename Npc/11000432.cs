using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000432: Hans
/// </summary>
public class _11000432 : NpcScript {
    internal _11000432(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;41
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001803$ 
                // - ...
                return true;
            case 30:
                // $script:0831180407001804$ 
                // - I came here to rest. Stop bothering me.
                return true;
            case 40:
                // $script:0831180407001805$ 
                // - ...
                switch (selection) {
                    // $script:0831180407001806$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001807$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
