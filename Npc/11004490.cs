using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004490: Valens
/// </summary>
public class _11004490 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012318$
    // - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012319$
                // - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
                return 10;
            case (10, 1):
                // $script:1227192907012320$
                // - Here to admire the architecture? It's breathtaking, isn't it?
                switch (selection) {
                    // $script:1227192907012321$
                    // - Not really.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012322$
                // - Balderdash! Surely even a hardened adventurer like you is moved by such grandeur. There's nothing like this in all of Maple World!
                return 11;
            case (11, 1):
                // $script:1227192907012323$
                // - Why, this building is a testament to the power of science. Even though I'm standing here, I feel as if I'm witnessing some impossible dream.
                return 11;
            case (11, 2):
                // $script:1227192907012324$
                // - Dr. $npcName:11004499[gender:0]$ will be over the moon when he sees this!
                switch (selection) {
                    // $script:0114162107012708$
                    // - Good luck with that.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114162107012709$
                // - Thank you!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
