using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000009: Rolling Thunder
/// </summary>
public class _11000009 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000055$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000058$
                // - Have you heard of $map:02000051$? The cliffs there are so treacherous that most people wouldn't dare climb it.
                return 30;
            case (30, 1):
                // $script:0831180407000059$
                // - If you have the chance, you should visit $map:02000051$ and visit my dad. Tell him you're $npcName:11000009[gender:0]$'s friend and you'll be like one of the family.
                switch (selection) {
                    // $script:0831180407000060$
                    // - Who is your father?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000061$
                // - Oh, don't worry. You'll know him when you see him.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
