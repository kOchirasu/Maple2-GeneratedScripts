using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001915: Lennon
/// </summary>
public class _11001915 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1116181807007416$
    // - I'm glad you're here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1116181807007418$
                // - I can't believe it...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
