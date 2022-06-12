using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004370: Claus
/// </summary>
public class _11004370 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011783$
    // - If you're looking for a classic holiday tree, go evergreen or go home.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011784$
                // - If you're looking for a classic holiday tree, go evergreen or go home.
                switch (selection) {
                    // $script:1120173007011855$
                    // - Ooh, an evergreen?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1120173007011856$
                // - There's nothing quite like it! Tall, bushy, and wonderfully scented... And if you're looking for the most beautiful tree, you'd need to get a Korean fir tree.
                switch (selection) {
                    // $script:1120173007011857$
                    // - The Korean fir tree, you say? Hmm...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1120173007011858$
                // - It grows on Mount Halla, and it's simply divine. A shame they're becoming harder to find these days. Climate change, you know.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
