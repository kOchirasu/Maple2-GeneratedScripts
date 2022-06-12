using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004314: Schatten
/// </summary>
public class _11004314 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0928133807011354$
    // - I am the shadow that evil fears.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0928133807011355$
                // - My agents can't get past the insane AI that's controlling most of Kritias! I feel so... frustrated.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
