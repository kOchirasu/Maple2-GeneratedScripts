using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000233: Brittany
/// </summary>
public class _11000233 : NpcScript {
    internal _11000233(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000987$ 
                // - Can I help you?
                return true;
            case 20:
                // $script:0831180407000989$ 
                // - Excuse me, what did you say?
                switch (selection) {
                    // $script:0831180407000990$
                    // - Have you seen $npcName:11000064[gender:0]$?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000991$ 
                // - I don't know. I don't think so. This place is small enough that newcomers should be easy to spot, and the last person who settled here was $npcName:11000006[gender:0]$.
                return true;
            case 30:
                // $script:0831180407000992$ 
                // - As you can see, $map:02000100$ suffers from a huge gap between the rich and the poor. It's all because of $npcName:11000065[gender:0]$ and $npcName:11000252[gender:0]$.
                return true;
            default:
                return true;
        }
    }
}
