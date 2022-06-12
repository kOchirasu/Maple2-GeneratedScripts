using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001409: Fubo
/// </summary>
public class _11001409 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005406$
    // - No exceptions. Not even for humans!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005486$
                // - You want to be strong, like the Meerkat Patrol? Then join our training!
                switch (selection) {
                    // $script:1222203907005487$
                    // - That sounds <i>adorable</i>. Sign me up!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005488$
                // - Don't underestimate us. If you cry and give up halfway through, you'll never live it down!
                switch (selection) {
                    // $script:1222203907005489$
                    // - I can handle anything you throw at me!
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1222203907005490$
                // - Heh... I'll see to it that you run away with your tail between your legs!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
