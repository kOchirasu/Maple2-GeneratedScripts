using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000232: George
/// </summary>
public class _11000232 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000983$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000985$
                // - Dark Wind has changed since $npcName:11000044[gender:0]$ took charge. Now its members are more interested in getting ahead than protecting $map:02000100$ like they used to.
                return 30;
            case (30, 1):
                // $script:0831180407000986$
                // - And the people of $map:02000100$ are walking on eggshells around them.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
