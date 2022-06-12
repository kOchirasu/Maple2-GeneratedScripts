using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000044: Katvan
/// </summary>
public class _11000044 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000209$
    // - Let's get to business.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000212$
                // - I'll admit, not everyone in Dark Wind was happy when I took over. Many were loyal to Captain Winn, not the organization. After he passed away, $npcName:11000006[gender:0]$ took some of our best agents and left.
                return 30;
            case (30, 1):
                // $script:0831180407000213$
                // - But I have my own principles to follow and I intend to lead Dark Wind in my own way. Winn Stilton was a great man, but we won't live in his shadow.
                return 30;
            case (30, 2):
                // $script:0831180407000214$
                // - The others may not be on board yet, but they'll come around. Eventually.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
