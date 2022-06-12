using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001006: Edith
/// </summary>
public class _11001006 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003429$
    // - I haven't seen any strangers here for a long time.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003432$
                // - Most people steer clear of this place because of the monsters.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
