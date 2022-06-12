using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004566: Pathos
/// </summary>
public class _11004566 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014544$
    // - Ah...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014545$
                // - Huh?
                return 10;
            case (10, 1):
                // $script:0220211107014546$
                // - I have nothing to say to you. We can work out our differences in the ring.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
