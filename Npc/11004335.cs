using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004335: Brighton
/// </summary>
public class _11004335 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011590$
    // - Now, isn't this something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011591$
                // - I've gotta admit, I'm impressed.
                return 10;
            case (10, 1):
                // $script:1010140307011592$
                // - This whole place is, like, the opposite of Maple World. No wonder the boss was so eager to check it out.
                return 10;
            case (10, 2):
                // $script:1010140307011593$
                // - I didn't believe a word of it, of course. But $npcName:11004334[gender:1]$ insisted, and... Wow. Just wow.
                return 10;
            case (10, 3):
                // $script:1010140307011594$
                // - $npcName:11003191[gender:0]$ doesn't know what he's missing!
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
