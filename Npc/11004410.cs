using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004410: Schatten
/// </summary>
public class _11004410 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011837$
    // - I am the shadow that evil fears.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011838$
                // - I get the feeling things are gonna get worse before they get better.
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
