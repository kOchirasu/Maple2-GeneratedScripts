using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001611: Ishura
/// </summary>
public class _11001611 : NpcScript {
    internal _11001611(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0509213707006098$ 
                // - <font color="#909090">(He's sound asleep.)</font>
                return true;
            case 10:
                // $script:0511194807006105$ 
                // - I miss the master. I still hear his voice in my head...
                return true;
            case 20:
                // $script:0515180407006106$ 
                // - $npcName:11001229[gender:0]$... Will he ever wake up?
                return true;
            default:
                return true;
        }
    }
}
