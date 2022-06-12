using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004251: Faint Writings
/// </summary>
public class _11004251 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010962$
    // - <font color="#909090">(Something is crudely scratched here.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010963$
                // - <font color="#909090">(Something is crudely scratched here.)</font>
                return 10;
            case (10, 1):
                // $script:0830163207010991$
                // - "That man is the root of all evil!"
                return 10;
            case (10, 2):
                // $script:0830163207010992$
                // - "He appeared out of the blue, pale as a ghost. Even my cows were scared of him."
                return 10;
            case (10, 3):
                // $script:0830173807010993$
                // - "But I couldn't kick him out. He seemed injured, and I was raised a gentleman. But letting him rest in my fields was a mistake. He pulled out a black bottle, grinned this sick little grin, then poured it all on the ground."
                return 10;
            case (10, 4):
                // $script:0830173807010994$
                // - "Everything happened quickly after that. The dark shadow that blossomed out of the liquid..."
                return 10;
            case (10, 5):
                // $script:0830173807010995$
                // - "My livestock were engulfed by darkness. They cried out as they transformed into monsters. The fields and streams turned black as ink. Even the people living on the farm became twisted."
                return 10;
            case (10, 6):
                // $script:0830173807010996$
                // - "I tried to outrun the darkness, but I sense my time is short. I can feel the corruption of this forsaken ground crawling up my legs, slowly transforming me..."
                return 10;
            case (10, 7):
                // $script:0830173807010997$
                // - "If you can read this, flee! Flee at once! This land is cursed. If you stay, in the end, you'll become... like me... IT IS TOO LATE!"
                return 10;
            case (10, 8):
                // $script:0830174907010998$
                // - <font color="#909090">(Strange letters appear beneath that. You can't decipher them, but they send a chill down your spine.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Next,
            (10, 5) => NpcTalkButton.Next,
            (10, 6) => NpcTalkButton.Next,
            (10, 7) => NpcTalkButton.Next,
            (10, 8) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
