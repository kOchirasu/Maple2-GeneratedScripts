using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000523: Eve
/// </summary>
public class _11000523 : NpcScript {
    internal _11000523(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002234$ 
                // - Welcome.
                return true;
            case 30:
                // $script:0831180407002237$ 
                // - After my father passed away, I found his journal among his things. My father was the guardian of the Blue Lapenta, and he wanted $npcName:11000064[gender:0]$ to be his successor. So I knew.
                // $script:0831180407002238$ 
                // - I knew there was no way $npcName:11000064[gender:0]$ did what the others said he did.
                // $script:0831180407002239$ 
                // - I'm glad the truth finally came out and everything is back to normal, even though $npcName:11000044[gender:0]$ hasn't paid for his crimes.
                return true;
            case 40:
                // $script:0831180407002240$ 
                // - Being with $npcName:11000064[gender:0]$ reminds me of the gorilla pie that we used to bake together when we were young.
                switch (selection) {
                    // $script:0831180407002241$
                    // - What could gorilla pie possibly be...?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002242$ 
                // - It's one of those pies topped with walnuts, almonds, and blueberries. When $npcName:11000064[gender:0]$ and I first made it, it was so bumpy and ugly that it looked like a gorilla. Why? What did you <i>think</i> it was?
                return true;
            default:
                return true;
        }
    }
}
