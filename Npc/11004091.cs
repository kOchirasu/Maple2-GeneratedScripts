using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004091: Lucky Whale
/// </summary>
public class _11004091 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010325$
    // - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010326$
                // - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
                return 10;
            case (10, 1):
                // $script:0622133907010327$
                // - <font color="#909090">(The local fishermen consider this whale lucky. They say that you'll catch a huge fish if you kiss the whale's cheek before heading out.)</font>
                return 10;
            case (10, 2):
                // $script:0622133907010328$
                // - <font color="#909090">(It's also lucky for the villagers. If you have a dream about this whale, buy a lottery ticket the next day and you'll surely win. At least, that's what they tell you.)</font>
                return 10;
            case (10, 3):
                // $script:0622133907010329$
                // - <font color="#909090">(Some people assume that this whale's name is Coco, given the name of the island. However, the creator of the whale insists that it isn't true.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
