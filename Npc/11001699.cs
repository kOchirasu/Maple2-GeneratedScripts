using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001699: Tinchai
/// </summary>
public class _11001699 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0711210007006724$
    // - Mm? Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006903$
                // - How can I help you?
                switch (selection) {
                    // $script:0727223007006904$
                    // - $npcName:11001557[gender:0]$ is a tough teacher.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006905$
                // - You don't need to tell <i>me</i> that. He's the reason some of our old students left!
                return 40;
            case (40, 1):
                // $script:0727223007006906$
                // - $npcName:11001557[gender:0]$ cares about only one thing, and that's training. He expects everyone to keep up with him, and the problem with that should be obvious.
                return 40;
            case (40, 2):
                // $script:0727223007006907$
                // - I will say, he has a talent for crushing confidence, and that's important when you get arrogant students. His heart's in the right place, it's just... cold and unfeeling, you know?
                return 40;
            case (40, 3):
                // $script:0727223007006908$
                // - If you ask him why all those students left, he'd tell you they were too soft. Even if he's right, he's not helping them by driving them away!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
