using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000523: Eve
/// </summary>
public class _11000523 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407002234$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002237$
                // - After my father passed away, I found his journal among his things. My father was the guardian of the Blue Lapenta, and he wanted $npcName:11000064[gender:0]$ to be his successor. So I knew.
                return 30;
            case (30, 1):
                // $script:0831180407002238$
                // - I knew there was no way $npcName:11000064[gender:0]$ did what the others said he did.
                return 30;
            case (30, 2):
                // $script:0831180407002239$
                // - I'm glad the truth finally came out and everything is back to normal, even though $npcName:11000044[gender:0]$ hasn't paid for his crimes.
                return -1;
            case (40, 0):
                // $script:0831180407002240$
                // - Being with $npcName:11000064[gender:0]$ reminds me of the gorilla pie that we used to bake together when we were young.
                switch (selection) {
                    // $script:0831180407002241$
                    // - What could gorilla pie possibly be...?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002242$
                // - It's one of those pies topped with walnuts, almonds, and blueberries. When $npcName:11000064[gender:0]$ and I first made it, it was so bumpy and ugly that it looked like a gorilla. Why? What did you <i>think</i> it was?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
